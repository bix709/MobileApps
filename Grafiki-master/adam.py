from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
import pickle
import os


class Metoda():
    def __init__(self, name, code):
        self.name = name
        self.code = code


tablica = []


def zapis():
    with open('data.adam', 'wb') as output:
        for x in tablica:
            pickle.dump(x, output, pickle.HIGHEST_PROTOCOL)


def odczyt():
    with open('data.adam', 'rb') as input:
        try:
            while True:
                tablica.append(pickle.load(input))
        except EOFError:
            pass


class StartUp(GridLayout):
    def __init__(self, **kwargs):
        super(StartUp, self).__init__(**kwargs)
        self.rows = 3
        odczyt()
        i = 0
        buttony = []
        for x in tablica:
            buttony.append(Button(text=x.name, id=str(i), on_press=lambda a: self.przekieruj(a)))
            self.add_widget(buttony[i])
            i += 1

    def przekieruj(self, sth):
        # os.system(str(sth))
        print(self.parent.ids.sth.text)


class MyApp(App):
    def build(self):
        return StartUp()


if __name__ == '__main__':
    MyApp().run()
