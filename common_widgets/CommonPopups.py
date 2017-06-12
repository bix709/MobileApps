# -*- coding: utf-8 -*-
"""
    author: Tomasz Teter
    copyright : 5517 Company
"""
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.dropdown import DropDown
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput

from adventureskiing.Config.config import privileges
from adventureskiing.Database.Callbacks import PasswordChange, CreateUser, UsersToChoose, RemoveUser, ChangePermissions
from adventureskiing.Utils.Users import UserButton
from common_callbacks.Callbacks import schedule_task
from common_widgets.FittingLabels import FontFittingButton, FontFittingLabel


class CommonPopup(Popup):
    def __init__(self, **kwargs):
        super(CommonPopup, self).__init__(size_hint_x=0.8, size_hint_y=0.9, auto_dismiss=True, **kwargs)
        self.main_layout = BoxLayout(orientation='vertical')
        self.add_widget(self.main_layout)
        self.setup_widgets()

    def setup_widgets(self):
        esc_layout = BoxLayout(size_hint_x=0.2, pos_hint={"x": 0.8})
        esc_layout.add_widget(FontFittingButton(text="X", on_press=lambda a: self.dismiss()))
        self.main_layout.add_widget(esc_layout)

    def focus_input(self, input_id):
        self.get_child(input_id).focus = True

    def get_child(self, input_id):
        return list(filter(lambda a: a.id == input_id, self.main_layout.children))[0]

    def unfocus_all_inputs(self):
        for text_input in [child for child in self.main_layout.children if isinstance(child, TextInput)]:
            text_input.focus = False


class UserModifyingPopup(CommonPopup):
    def __init__(self, **kwargs):
        super(UserModifyingPopup, self).__init__(**kwargs)
        self.choosen = None
        self.confirm_button = None

    def setup_widgets(self):
        super(UserModifyingPopup, self).setup_widgets()
        schedule_task(UsersToChoose(), instance=self)

    def assign_users(self, users):
        user_chooser = DropDown()
        for user in users:
            user_chooser.add_widget(UserButton(text="{}".format(users[user].__str__()), user=users[user],
                                               size_hint_y=None, height=user_chooser.height,
                                               on_release=lambda a: user_chooser.select(a)))
        self.choosen = UserButton(id='chooser', text="Wybierz uzytkownika", size_hint=(1, 1), user=None)
        self.choosen.bind(on_release=lambda a: user_chooser.open(self.choosen))
        user_chooser.bind(on_select=lambda instance, pressed_button: self.update_user_chooser(self.choosen,
                                                                                              pressed_button))
        self.main_layout.add_widget(self.choosen)

    def update_user_chooser(self, choosen, pressed_button):
        setattr(choosen, 'user', pressed_button.user)
        setattr(choosen, 'text', pressed_button.text)

    def display_results(self, success, success_msg, failure_msg):
        if success and self.modified_logged_user():
            self.bind(on_dismiss=App.get_running_app().root.logout)
            self.confirm_button.bind(on_press=lambda a: self.dismiss(), on_release=lambda a: self.dismiss())
        color, msg = ('00FF00', success_msg) if success else ('FF0000', failure_msg)
        self.main_layout.clear_widgets()
        self.main_layout.add_widget(FontFittingLabel(markup=True,
                                                     text="[b][color={}]{}![/color][/b]".format(color, msg)))
        self.setup_widgets()
        self.refresh_user_possibilities()

    def modified_logged_user(self):
        return True if self.choosen.user.__dict__ == App.get_running_app().root.logged_user.__dict__ else False

    def refresh_user_possibilities(self):
        App.get_running_app().root.refresh_userchooser()


class PasswordChanger(CommonPopup):
    def __init__(self, **kwargs):
        super(PasswordChanger, self).__init__(title="Zmien haslo", **kwargs)

    def setup_widgets(self):
        super(PasswordChanger, self).setup_widgets()
        self.setup_input_fields()
        self.main_layout.add_widget(FontFittingButton(text="Zatwierdz", on_press=lambda a: self.confirm()))

    def setup_input_fields(self):
        self.main_layout.add_widget(FontFittingLabel(text="Stare haslo:"))
        self.main_layout.add_widget(TextInput(id='old', focus=False, password=True, multiline=False,
                                              on_text_validate=lambda a: self.focus_input('new')))
        self.focus_input('old')
        self.main_layout.add_widget(FontFittingLabel(text="Nowe haslo:"))
        self.main_layout.add_widget(TextInput(id='new', focus=False, password=True, multiline=False,
                                              on_text_validate=lambda a: self.focus_input('repeated')))
        self.main_layout.add_widget(FontFittingLabel(text="Powtorz Nowe haslo:"))
        self.main_layout.add_widget(TextInput(id='repeated', focus=False, password=True, multiline=False,
                                              on_text_validate=lambda a: self.confirm()))

    def confirm(self):
        self.unfocus_all_inputs()
        if not self.get_child('new').text == self.get_child('repeated').text:
            self.on_wrong_attempt()
        else:
            schedule_task(PasswordChange(old_pw=hash(self.get_child('old').text),
                              new_pw=hash(self.get_child('new').text),
                              user=App.get_running_app().root.logged_user), instance=self)

    def on_successful_change(self):
        self.main_layout.clear_widgets()
        self.main_layout.add_widget(FontFittingLabel(text="[color=00FF00]Hasło zostało zmienione poprawnie.[/color]",
                                                     markup=True))
        self.bind(on_dismiss=App.get_running_app().root.logout)
        self.main_layout.add_widget(FontFittingButton(text="Ok", on_release=lambda a: self.dismiss()))

    def on_wrong_attempt(self):
        self.main_layout.clear_widgets()
        self.setup_widgets()
        self.main_layout.add_widget(FontFittingLabel(text="[b][color=FF0000]Nie poprawne dane![/color][/b]",
                                                     markup=True))


class UserAddingPopup(CommonPopup):
    def __init__(self, **kwargs):
        super(UserAddingPopup, self).__init__(title='Utwórz konto', **kwargs)

    def setup_widgets(self):
        super(UserAddingPopup, self).setup_widgets()
        self.setup_input_fields()
        self.main_layout.add_widget(FontFittingButton(text="Zatwierdz",
                                                      on_press=lambda a: schedule_task(
                                                          CreateUser(firstname=self.get_child('firstname').text,
                                                                     lastname=self.get_child('lastname').text,
                                                                     login=self.get_child('login').text),
                                                          instance=self)))

    def setup_input_fields(self):
        self.main_layout.add_widget(FontFittingLabel(text="Login:"))
        self.main_layout.add_widget(TextInput(id='login', focus=False, multiline=False,
                                              on_text_validate=lambda a: self.focus_input('firstname')))
        self.focus_input('login')
        self.main_layout.add_widget(FontFittingLabel(text="Imie:"))
        self.main_layout.add_widget(TextInput(id='firstname', focus=False, multiline=False,
                                              on_text_validate=lambda a: self.focus_input('lastname')))
        self.main_layout.add_widget(FontFittingLabel(text="Nazwisko:"))
        self.main_layout.add_widget(TextInput(id='lastname', focus=False, multiline=False,
                                              on_text_validate=lambda a: schedule_task(schedule_task(
                                                  CreateUser(firstname=self.get_child('firstname').text,
                                                             lastname=self.get_child('lastname').text,
                                                             login=self.get_child('login').text),
                                                  instance=self))))

    def display_results(self, created_successfully):
        self.unfocus_all_inputs()
        self.main_layout.clear_widgets()
        messages = {
            None: ('Nie można utworzyć konta. Wprowadź poprawne dane!', 'FF0000'),
            False: ('Użytkownik juz istnieje.', 'FF0000'),
            True: ('Konto zostało założone poprawnie!', '00FF00')
        }
        message, color = messages[created_successfully]
        self.main_layout.add_widget(FontFittingLabel(text="[b][color={}]{}![/color][/b]".format(color, message),
                                                     markup=True))
        self.setup_widgets()
        self.refresh_user_chooser()

    def refresh_user_chooser(self):
        """ Updates user chooser (currently added / removed user ). """
        App.get_running_app().root.refresh_userchooser()


class UserRemovingPopup(UserModifyingPopup):
    def __init__(self, **kwargs):
        super(UserRemovingPopup, self).__init__(title='Usuń konto', **kwargs)

    def assign_users(self, users):
        self.main_layout.add_widget(FontFittingLabel(text='Wybierz użytkownika:'))
        super(UserRemovingPopup, self).assign_users(users)
        self.confirm_button = FontFittingButton(text="Usuń konto", size_hint=(1, 1),
                                                on_press=lambda a:
                                                ConfirmationPopup(confirmed_function=self.remove_choosen,
                                                                  func_args=tuple([self.choosen])).open())
        self.main_layout.add_widget(self.confirm_button)

    def remove_choosen(self, choosen_user_button):
        schedule_task(callback=RemoveUser(choosen_user_button.user), instance=self)

    def display_results(self, removed_successfully, *args):
        failure_msg = 'Nie udało się usunąć konta' if removed_successfully is False else 'Wybierz odpowiedniego uzytkownika'
        super(UserRemovingPopup, self).display_results(success=removed_successfully,
                                                       success_msg='Konto zostało usunięte',
                                                       failure_msg=failure_msg)


class PermissionChanger(UserModifyingPopup):
    def __init__(self, **kwargs):
        super(PermissionChanger, self).__init__(title='Zmień uprawnienia', **kwargs)
        self.choosen_privilege = None

    def assign_users(self, users):
        self.main_layout.add_widget(FontFittingLabel(text='Wybierz uzytkownika i uprawnienia'))
        super(PermissionChanger, self).assign_users(users)
        self.assign_permissions()

    def assign_permissions(self):
        privilege_chooser = DropDown()
        for privilege in privileges:
            privilege_chooser.add_widget(FontFittingButton(text="{}".format(privilege),
                                                           size_hint_y=None, height=privilege_chooser.height,
                                                           on_release=lambda a: privilege_chooser.select(a.text)))
        self.choosen_privilege = FontFittingButton(id='privilege_chooser', text="Wybierz uprawnienia", size_hint=(1, 1),
                                                   user=None)
        self.choosen_privilege.bind(on_release=lambda a: privilege_chooser.open(self.choosen_privilege))
        privilege_chooser.bind(on_select=lambda instance, choosen: setattr(self.choosen_privilege, 'text', choosen))
        self.main_layout.add_widget(self.choosen_privilege)
        self.confirm_button = FontFittingButton(text="Zmień uprawnienia", size_hint=(1, 1),
                                                on_press=lambda a:
                                                ConfirmationPopup(
                                                    confirmed_function=schedule_task,
                                                    func_args=ChangePermissions(self.choosen.user,
                                                                                self.choosen_privilege.text),
                                                    func_kwargs={'instance': self}).open())
        self.main_layout.add_widget(self.confirm_button)

    def display_results(self, changed_successfully, *args):
        msg = 'Wybierz odpowiednie uprawnienia i uzytkownika' if changed_successfully is None \
            else 'Nie udało się zmienić uprawnień'
        super(PermissionChanger, self).display_results(success=changed_successfully,
                                                       success_msg='Uprawnienia zostały zmienione',
                                                       failure_msg=msg)


class ConfirmationPopup(CommonPopup):
    def __init__(self, confirmed_function, func_args=None, func_kwargs=None, **kwargs):
        super(ConfirmationPopup, self).__init__(**kwargs)
        self.confirmed_function = confirmed_function
        self.function_args = func_args if func_args else tuple()
        self.function_kwargs = func_kwargs if func_kwargs else dict()

    def setup_widgets(self):
        super(ConfirmationPopup, self).setup_widgets()
        self.main_layout.add_widget(FontFittingLabel(text='Jestes pewien?'))
        self.main_layout.add_widget(FontFittingButton(text='Tak', on_press=lambda a: self.confirm()))
        self.main_layout.add_widget(FontFittingButton(text='Nie', on_press=lambda a: self.dismiss()))

    def confirm(self):
        self.dismiss()
        self.confirmed_function(*self.function_args, **self.function_kwargs)
