from kivy.uix.widget import Widget
from kivy.graphics import Rectangle, Ellipse, Color
from kivy.animation import Animation
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.app import App
from kivy.clock import Clock
from kivy.uix.actionbar import ActionBar, ActionPrevious, ActionButton, ActionDropDown, ActionView, ActionSeparator, \
    ActionItem
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import SlideTransition, FadeTransition, SwapTransition
import time
from kivy.uix.tabbedpanel import TabbedPanel, TabbedPanelHeader, TabbedPanelItem
from kivy.uix.carousel import Carousel
from kivy.uix.image import AsyncImage
import kivy
from kivy.uix.dropdown import DropDown
from kivy.uix.popup import Popup

# --------------------------------------------------------------------------------------------------
DniTygodnia = {1: "Poniedzialek", 2: "Wtorek", 3: "Sroda",
               4: "Czwartek", 5: "Piatek", 6: "Sobota", 7: "Niedziela"}
DniMiesiaca = {1: 31, 2: 29, 3: 31, 4: 30, 11: 30, 12: 31, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31}
MiesiacRoku = {1: "Styczeń", 2: "Luty", 3: "Marzec", 4: "Kwiecień", 5: "Maj", 6: "Czerwiec", 7: "Lipiec",
               8: "Sierpień", 9: "Wrzesień", 10: "Październik", 11: "Listopad", 12: "Grudzień"}
ObecneGrafiki = {}
Userzy = {}
# --------------------------------------------------------------------------------------------------
Builder.load_string('''
#: import FadeTransition kivy.uix.screenmanager.FadeTransition
<CustomLayout>:
    orientation:'vertical'

<mainScreenManager>:
    LoginScreen:
        name:"scLogin"
        canvas.before:
            Rectangle:
                pos:self.pos
                size:self.size
                source:"tlo2.jpg"
        CustomLayout:
            size_hint_x:0.2
            size_hint_y:0.1
            pos_hint:{"x":0.5 ,"y":0.01}
            Zegarek:
        CustomLayout:
            size_hint_x:0.2
            size_hint_y:0.4
            pos_hint:{"x":0.35,"y":0.5}
            Label:
                color:1,1,1,1
                font_size:30
                text:"Username:"
            TextInput:
                multiline:False
                id:user
                focus:True
                on_text_validate: app.root.ids.passw.focus = True
            Label:
                color:1,1,1,1
                font_size:30
                text:"Password:"
            TextInput:
                multiline:False
                id:passw
                password: True
                focus:False
                on_text_validate: app.root.handler()
        CustomLayout:
            size_hint_x:0.2
            size_hint_y:0.2
            pos_hint:{"x":0.35,"y":0.25}
            Button:
                background_normal:"b3.png"
                text:"Zaloguj!"
                color:1,1,1,1
                font_size:30
                on_press: app.root.handler()
    Relogin:
        name:"WrongLogin"
        canvas.before:
            Rectangle:
                pos:self.pos
                size:self.size
                source:"tlo1.jpg"
        CustomLayout:
            size_hint_x:0.2
            size_hint_y:0.1
            pos: 570,-10
            Zegarek:
        CustomLayout:
            size_hint_x:1
            size_hint_y:1
            pos:100,250
            Button:
                background_color:0,0,0,0
                color:0,0,0,1
                font_size:45
                markup:True
                text_size:self.size
                text:"Zle haslo! Nacisnij aby wrocic do logowania! "
                on_press: app.root.current = "scLogin"
<ScreenMenu>:
    name:"Menu"
    BoxLayout:
        orientation:'vertical'
        ActionBar:
            background_image:'jzielony.png'
            ActionView:
                ActionPrevious:
                    size_hint:0.5,1
                ActionSeparator:
                    background_image:"zielony.png"
                ActionButton:
                    size_hint:1.2 ,1
                    id:tab0
                    state:"down"
                    background_down:'b5.png'
                    color:0,0,0,1
                    text:"Moje Grafiki"
                    on_press: root.ids.caro.load_slide(root.ids.caro.slides[0])
                ActionSeparator:
                    background_image:"zielony.png"
                ActionButton:
                    size_hint:1.5 ,1
                    id:tab1
                    background_down:'b5.png'
                    color:0,0,0,1
                    text:"Dzisiaj"
                    on_press:root.ids.caro.load_slide(root.ids.caro.slides[1])
                ActionSeparator:
                    background_image:"zielony.png"
                ActionButton:
                    id:tab2
                    background_down:'b5.png'
                    color:0,0,0,1
                    text:"Zapisz Lekcje"
                    on_press:root.ids.caro.load_slide(root.ids.caro.slides[2])
                ActionSeparator:
                    background_image:"zielony.png"
                ActionButton:
                    id:tab3
                    background_down:'b5.png'
                    color:0,0,0,1
                    text:"Rozliczenie"
                    on_press:root.ids.caro.load_slide(root.ids.caro.slides[3])
                ActionSeparator:
                    background_image:"zielony.png"
                ActionButton:
                    id:tab4
                    background_down:'b5.png'
                    color:0,0,0,1
                    text:"Panel"
                    on_press:root.ids.caro.load_slide(root.ids.caro.slides[4])
        Karuzela:
            id:caro
            MojeGrafikiS:
                id:mojegrafikis
                name:"MojeGrafiki"
                canvas.before:
                    Rectangle:
                        pos:self.pos
                        size:self.size
                        source:'tlo1.jpg'
                tab:tab0

            DzisiajS:
                id:dzisiajs
                name:"Dzisiaj"
                canvas.before:
                    Rectangle:
                        pos:self.pos
                        size:self.size
                        source:'tlo2.jpg'
                tab:tab1
            ZapiszS:
                name:"Zapisz"
                canvas.before:
                    Rectangle:
                        pos:self.pos
                        size:self.size
                        source:'b3.png'
                tab:tab2
            RozliczenieS:
                name:"Rozliczenie"
                canvas.before:
                    Rectangle:
                        pos:self.pos
                        size:self.size
                        source:'szary.png'
                tab:tab3
            AtlasS:
                name:"Atlas"
                canvas.before:
                    Rectangle:
                        pos:self.pos
                        size:self.size
                        source:'b3.png'
                tab:tab4
<ScreenAdminMenu>:
    name:"AdminMenu"
    BoxLayout:
        orientation:'vertical'
        ActionBar:
            background_image:'jzielony.png'
            ActionView:
                ActionPrevious:
                ActionSeparator:
                    background_image:"zielony.png"
                ActionButton:
                    size_hint:1.2 ,1
                    id:Atab0
                    state:"down"
                    background_down:'b5.png'
                    color:0,0,0,1
                    text:"Moje Grafiki"
                    on_press: root.ids.Acaro.load_slide(root.ids.Acaro.slides[0])
                ActionSeparator:
                    background_image:"zielony.png"
                ActionButton:
                    size_hint:1.5 ,1
                    id:Atab1
                    background_down:'b5.png'
                    color:0,0,0,1
                    text:"Dzisiaj"
                    on_press:root.ids.Acaro.load_slide(root.ids.Acaro.slides[1])
                ActionSeparator:
                    background_image:"zielony.png"
                ActionButton:
                    id:Atab2
                    background_down:'b5.png'
                    color:0,0,0,1
                    text:"Zapisz Lekcje"
                    on_press:root.ids.Acaro.load_slide(root.ids.Acaro.slides[2])
                ActionSeparator:
                    background_image:"zielony.png"
                ActionButton:
                    id:Atab3
                    background_down:'b5.png'
                    color:0,0,0,1
                    text:"Rozliczenie"
                    on_press:root.ids.Acaro.load_slide(root.ids.Acaro.slides[3])
                ActionSeparator:
                    background_image:"zielony.png"
                ActionButton:
                    id:Atab4
                    background_down:'b5.png'
                    color:0,0,0,1
                    text:"Panel"
                    on_press:root.ids.Acaro.load_slide(root.ids.Acaro.slides[4])
        Karuzela:
            id:Acaro
            MojeGrafikiS:
                id:amojegrafikis
                name:"AMojeGrafiki"
                canvas.before:
                    Rectangle:
                        pos:self.pos
                        size:self.size
                        source:'tlo1.jpg'
                tab:Atab0

            DzisiajS:
                name:"ADzisiaj"
                canvas.before:
                    Rectangle:
                        pos:self.pos
                        size:self.size
                        source:'tlo2.jpg'
                tab:Atab1
            ZapiszS:
                name:"AZapisz"
                canvas.before:
                    Rectangle:
                        pos:self.pos
                        size:self.size
                        source:'b3.png'
                tab:Atab2
            RozliczenieS:
                name:"ARozliczenie"
                canvas.before:
                    Rectangle:
                        pos:self.pos
                        size:self.size
                        source:'b4.png'
                tab:Atab3
            AtlasS:
                name:"AAtlas"
                canvas.before:
                    Rectangle:
                        pos:self.pos
                        size:self.size
                        source:'b3.png'
                tab:Atab4
<ZapiszPopup>:
    title:"Zapisz lekcje"
    id:zapispop
    size_hint:0.9,0.9
    auto_dismiss:True
    canvas.before:
        Rectangle:
            pos:self.pos
            size:self.size
            source:"tlo1.jpg"
    CustomLayout:
        id:popupmain
        size_hint:1,1
        pos:0,0
        CustomLayout:
            size_hint_x:0.2
            size_hint_y:0.1
            pos_hint:{"x":0.8 , "y":0.}
            Button:
                background_normal:"b4.png"
                color:0,0,0,1
                text:"Zamknij"
                on_release: root.dismiss()
        CustomLayout:
            size_hint_x:0.2
            size_hint_y:0.4
            pos_hint:{"x":0.3 , "y":0.}
            Label:
                font_size:30
                text:"Imie/Imiona:"
            TextInput:
                focus:True
                multiline:False
                id:imie
                on_text_validate: root.ids.nazwisko.focus = True
            Label:
                font_size:30
                text:"Nazwisko:"
            TextInput:
                focus:False
                multiline:False
                id:nazwisko
                on_text_validate: root.ids.age.focus = True
            Label:
                font_size:30
                text:"Wiek:"
            TextInput:
                focus:False
                multiline:False
                id:age
        CustomLayout:
            size_hint_x:0.2
            size_hint_y:0.1
            pos_hint:{"x":0.3 , "y":0.1}
            Button:
                id:confirm
                text:"Zatwierdz"
                background_normal:"b4.png"
                color:0,0,0,1
                on_release: app.root.zapiszDzisiejszy()

<RozliczeniePop>:
    title:"Szczegółowe rozliczenie"
    id:rozliczeniepop
    size_hint:0.9,0.9
    auto_dismiss:True
    canvas.before:
        Rectangle:
            pos:self.pos
            size:self.size
            source:"tlo1.jpg"
    CustomLayout:
        id:mpop
        size_hint:1,1
        pos:0,0
        CustomLayout:
            size_hint_x:0.2
            size_hint_y:0.1
            pos_hint:{"x":0.8 , "y":0.}
            Button:
                background_normal:"b4.png"
                color:0,0,0,1
                text:"Zamknij"
                on_release: root.dismiss()

<LabelTlo>:
    canvas.before:
        Rectangle:
            source:"czerwony.png"
            pos:self.pos
            size:self.size

''')


# --------------------------------------------------------------------------------------------------
class User():
    def __init__(self, name, password, perm):
        self.name = name
        self.password = hash(password)
        self.permission = perm
        self.miesieczne = {}  # zarobki z kazdego miesiaca
        self.innyGrafik = {}  # grafik inny niz z tego tygodnia
        self.dzisiejszy = {}  # Grafik na dzis "9":"ON"
        self.grafiki = []  # Nazwy utworzonych grafikow(moich)
        self.calyGrafik = {}  # zapisuje caly grafik Pon:{} Wt:{} Sr:{}
        self.Inni = {}  # "Link" : "Nazwa obecnego grafiku"
        self.wyswietlany = {}  # Wczytany grafik do wyswietlenia ( nie moj )
        self.dostepni = {}  # "9" : [tab. dostepnych osob o 9]
        self.licznik = {}  # Ilosc lekcji z dziś {"Tomek" : 5}
        self.inneGrafiki = []
        self.ceny = {
            1: 60,
            2: 90,
            3: 120,
            4: 140,
            5: 150
        }

    def gread(self, nazwa):

        plik = open(nazwa, "r")
        zarobki = {}
        for x in range(1, 8):
            line = plik.readline()
            temp = line.strip().split("||")
            arg = temp[0].split("//")[1]
            zarobki[arg] = 0
            for y in range(9, 21):
                line = plik.readline()
                try:
                    if ("||ON" not in line):
                        zarobki[arg] += self.ceny[int(line[line.index("#") + 1])] / 2
                except(ValueError):
                    zarobki[arg] += 0
        plik.close()
        for x in zarobki:
            date = x.split("-")
            m = int(date[1])
            y = int(date[2])
            if ("%s-%s" % (m, y) not in self.miesieczne):
                self.miesieczne["%s-%s" % (m, y)] = 0

            self.miesieczne["%s-%s" % (m, y)] += zarobki[x]

    def zarobki_admin(self):
        tm = 0
        p1m = 0
        p2m = 0
        ts = 0
        p1s = 0
        p2s = 0
        for x in Users:
            self.miesieczne = {}
            self.wczytaj_zarobki(inne=x.name)
            tm += self.tm
            p1m += self.p1m
            p2m += self.p2m
            ts += self.ts
            p1s += self.p1s
            p2s += self.p2s
        self.tm = tm
        self.p1m = p1m
        self.p2m = p2m
        self.ts = ts
        self.p1s = p1s
        self.p2s = p2s

    def wczytaj_zarobki(self, **kwargs):
        self.tm = 0
        self.p1m = 0
        self.p2m = 0
        self.ts = 0
        self.p1s = 0
        self.p2s = 0
        # zmiana test
        mon = time.gmtime().tm_mon
        yr = time.gmtime().tm_year
        if ("inne" in kwargs):
            self.wczytaj_spis(obcy=kwargs["inne"])
            for x in self.inneGrafiki:
                self.gread(x)
        else:
            for x in self.grafiki:
                self.gread(x)
        for x in self.miesieczne:
            date = x.split("-")
            m = int(date[0])
            y = int(date[1])
            # Obecny miesiac
            if (mon > 8):
                if (m > 8):
                    if (y == yr):
                        if (m == mon):
                            self.tm = self.miesieczne[x]
                        if (m == mon - 1):
                            self.p1m = self.miesieczne[x]
                        if (m == mon - 2):
                            self.p2m = self.miesieczne[x]
                        self.ts += self.miesieczne[x]
                    if (y == yr - 1):
                        self.p1s += self.miesieczne[x]
                    if (y == yr - 2):
                        self.p2s += self.miesieczne[x]
                else:
                    if (y == yr):
                        self.p1s += self.miesieczne[x]
                    if (y == yr - 1):
                        self.p2s += self.miesieczne[x]
            else:
                if (mon == 1):
                    if (m == 1 and y == yr):
                        self.tm = self.miesieczne[x]
                    elif (m == 12 and y == yr - 1):
                        self.p1m = self.miesieczne[x]
                    elif (m == 11 and y == yr - 1):
                        self.p2m = self.miesieczne[x]
                elif (mon == 2):
                    if (m == 2 and y == yr):
                        self.tm = self.miesieczne[x]
                    elif (m == 1 and y == yr):
                        self.p1m = self.miesieczne[x]
                    elif (m == 12 and y == yr - 1):
                        self.p2m = self.miesieczne[x]
                elif (mon > 2):
                    if (y == yr):
                        if (m == mon):
                            self.tm = self.miesieczne[x]
                        if (m == mon - 1):
                            self.p1m = self.miesieczne[x]
                        if (m == mon - 2):
                            self.p2m = self.miesieczne[x]
                if (m > 8):
                    if (y == yr - 1):
                        self.ts += self.miesieczne[x]
                    if (y == yr - 2):
                        self.p1s += self.miesieczne[x]
                    if (y == yr - 3):
                        self.p2s += self.miesieczne[x]
                else:
                    if (y == yr):
                        self.ts += self.miesieczne[x]
                    if (y == yr - 1):
                        self.p1s += self.miesieczne[x]
                    if (y == yr - 2):
                        self.p2s += self.miesieczne[x]

    def sprawdzDostepnych(self):
        for x in range(9, 21):
            self.dostepni[x] = []
        for x in self.Inni.items():
            plik = open(x[1].strip("\n"), "r")
            self.licznik[x[0]] = 0
            for line in plik:
                if (DniTygodnia[time.gmtime().tm_wday + 1] in line):
                    for i in range(9, 21):
                        if ("ON\n" in plik.readline()):
                            self.dostepni[i].append(x[0])
                        else:
                            self.licznik[x[0]] += 1
                    break
            plik.close()
        cHour = time.gmtime().tm_hour + 2
        tab = []
        for x in self.dostepni.keys():
            if (x < cHour):
                tab.append(x)
        for x in tab:
            del self.dostepni[x]

    def zapisz_inny_grafik(self, nazwa):
        plik = open(nazwa.strip("\n"), "w")
        for x in self.innyGrafik:
            plik.write("%s||ON\n" % x)
            for i in range(9, 21):
                plik.write("%s.00-%s.50||%s\n" % (i, i, self.innyGrafik[x][i].strip()))
        plik.close()

    def wczytaj_inny_grafik(self, nazwa):
        plik = open(nazwa.strip("\n"), "r")
        self.innyGrafik = {}
        try:
            if ("przyszly" in nazwa):
                for line in plik:
                    m = line.strip().split("||")
                    dictt = {}
                    for x in range(9, 21):
                        temp = plik.readline()
                        temp = temp.split("||")
                        dictt[x] = temp[1]
                    self.innyGrafik[m[0]] = dictt
                plik.close()
            else:
                for day in range(7):
                    m = plik.readline().strip().split("||")
                    dictt = {}
                    for x in range(9, 21):
                        temp = plik.readline()
                        temp = temp.split("||")
                        dictt[x] = temp[1]
                    self.innyGrafik[m[0]] = dictt
                plik.close()
        except(IndexError):
            self.innyGrafik = {}
            plik.close()
            return

    def wczytaj(self):  # wczytuje dzisiejszy i caly grafik (tylko bierzacy tydzien)
        plik = open(self.obecny.strip(), "r")
        for day in range(1, 8):
            m = plik.readline().strip().split("||")
            dictt = {}
            for x in range(9, 21):
                temp = plik.readline()
                temp = temp.split("||")
                dictt[x] = temp[1]
            self.calyGrafik[m[0]] = dictt
        dzis = "%s-%s-%s" % (time.gmtime().tm_mday, time.gmtime().tm_mon, time.gmtime().tm_year)
        self.dzisiejszy = self.calyGrafik["%s//%s" % (DniTygodnia[time.gmtime().tm_wday + 1], dzis)]
        plik.close()

    def zapiszStan(self):
        plik = open("Userzy.txt", "r")
        temp = []
        for line in plik:
            temp.append(line)
        plik.close()
        plik = open("Userzy.txt", "w")
        for x in temp:
            if (self.name in x):
                temp2 = x.split("||")
                x = "%s||%s||%s\n" % (temp2[0], temp2[1], self.obecny)
            plik.write(x)
        plik.close()

    def wczytajInni(self):
        plik = open("Userzy.txt", "r")
        for line in plik:
            temp = line.split("||")
            self.Inni[temp[0]] = temp[2]
        plik.close()

    def wczytajObecny(self):
        plik = open("Userzy.txt", "r")
        for line in plik:
            temp = line.split("||")
            if (self.name in temp[0]):
                self.obecny = temp[2]
                break

    def aktualizujGrafik(self):
        plik = open(self.obecny.strip(), "w")
        dzis = "%s-%s-%s" % (time.gmtime().tm_mday, time.gmtime().tm_mon, time.gmtime().tm_year)
        self.dzisiejszy = self.calyGrafik["%s//%s" % (DniTygodnia[time.gmtime().tm_wday + 1], dzis)]
        for x in self.calyGrafik:
            plik.write("%s||ON\n" % x)
            for i in range(9, 21):
                plik.write("%s.00-%s.50||%s\n" % (i, i, self.calyGrafik[x][i].strip()))
        plik.close()

    def aktualizuj_przyszly(self):
        self.wczytaj()
        plik = open(self.obecny.strip(), "r")
        daty = []
        usun = []
        self.przyszly = {}
        try:
            for line in plik:
                if ("//" in line):
                    daty.append(line.split("||")[0].split("//")[1])
            plik.close()
            plik = open("G%s-przyszly.txt" % self.name, "r")
            for day in range(7):
                m = plik.readline().strip().split("||")
                dictt = {}
                for x in range(9, 21):
                    temp = plik.readline()
                    temp = temp.split("||")
                    dictt[x] = temp[1]
                self.przyszly[m[0]] = dictt
            plik.close()
        except:
            plik.close()
            return

        for x in self.przyszly:
            if (x in daty):
                usun.append(x)
                for i in range(9, 21):
                    self.calyGrafik[x][i] = self.przyszly[x][i]
        for x in usun:
            del self.przyszly[x]

        plik = open("G%s-przyszly.txt" % self.name, "w")
        for x in self.przyszly:
            plik.write("%s||ON\n" % x)
            for i in range(9, 21):
                plik.write("%s.00-%s.50||%s\n" % (i, i, self.innyGrafik[x][i].strip()))
        plik.close()
        self.aktualizujGrafik()

    def dodaj_do_przyszly(self, nazwa, data, godzina, tresc):
        self.przyszly = {}
        plik = open("G%s-przyszly.txt" % nazwa, "r")
        for day in range(1, 8):
            m = plik.readline().strip().split("||")
            dictt = {}
            for x in range(9, 21):
                temp = plik.readline()
                temp = temp.split("||")
                dictt[x] = temp[1]
            self.przyszly[m[0]] = dictt
        plik.close()
        self.przyszly[data][godzina] = tresc
        plik = open("G%s-przyszly.txt" % self.name, "w")
        for x in self.przyszly:
            plik.write("%s||ON\n" % x)
            for i in range(9, 21):
                plik.write("%s.00-%s.50||%s\n" % (i, i, self.innyGrafik[x][i].strip()))
        plik.close()

    def aktualizuj(self):
        self.wczytajObecny()
        self.wczytaj_spis()
        self.obecny = self.obecny.strip()
        # Wykonuje sie co 5 min, Co poniedzialek tworzy grafik i zapisuje jego nazwe jako Obecny
        x = "G%s_%s-%s-%s.txt" % (self.name, time.gmtime().tm_mday - time.gmtime().tm_wday,
                                  time.gmtime().tm_mon, time.gmtime().tm_year)
        # Pierwszy warunek == 0 - poniedzialek, teraz zmienione na wtorek do testu

        if (self.obecny != x):
            self.nowy()
            self.obecny = x
            self.zapiszStan()
            self.aktualizuj_przyszly()

        self.wczytaj()  # Caly grafik , dzisiejszy
        self.wczytajInni()
        self.sprawdzDostepnych()

        # Grafik.aktualizuj()

    def wczytaj_spis(self, **kwargs):
        if ("obcy" in kwargs):
            self.inneGrafiki = {}
            name = kwargs["obcy"]
        else:
            name = self.name
        plik = open("SpisGrafikow.txt", "r")
        for line in plik:
            if (name in line):
                line.strip()
                temp = line.split(":")
                temp[1].strip(" ")
                temp[1] = temp[1][2:temp[1].__len__() - 2]
                if (temp[1][temp[1].__len__() - 1] == "'"):
                    temp[1] = temp[1][:temp[1].__len__() - 1]
                self.grafiki = temp[1].split("', '")
        plik.close()
        if ("obcy" in kwargs):
            self.inneGrafiki = self.grafiki
            self.wczytaj_spis()

    def dodaj_grafik(self, nazwa):
        self.grafiki.append(nazwa)
        plik = open("SpisGrafikow.txt", "r+")
        temp = []
        for line in plik:
            temp.append(line)
        plik.close()
        plik = open("SpisGrafikow.txt", "w")
        for x in temp:
            if (self.name in x):
                x = "%s:%s" % (self.name, self.grafiki)
                plik.write("%s\n" % x)
                continue
            plik.write("%s" % x)

        plik.close()

    def nowy(self):
        x = "G%s_%s-%s-%s.txt" % (self.name, time.gmtime().tm_mday - time.gmtime().tm_wday,
                                  time.gmtime().tm_mon, time.gmtime().tm_year)
        self.dodaj_grafik(x)
        plik = open(x, "w")
        d = time.gmtime().tm_mday - time.gmtime().tm_wday
        m = time.gmtime().tm_mon
        for i in range(1, 8):
            if (d > DniMiesiaca[m]):
                d = 1
                if (m == 12):
                    m = 1
                else:
                    m += 1
            plik.write("%s//%s-%s-%s||ON \n" % (DniTygodnia[i], d, m, time.gmtime().tm_year))
            d += 1
            for j in range(9, 21):
                plik.write("%s.00-%s.50||ON\n" % (j, j))
        plik.close()


# --------------------------------------------------------------------------------------------------
Users = [User("Link", "Link", "User"), User("Suchy", "Suchy", "User"), User("Tomek", "Tomek", "User"),
         User("Mati", "Mati", "User"), User("Joker", "Joker", "User"),
         User("Waldek", "Waldek", "User"), User("Bronia", "Bronia", "Admin")]
previousScr = None
Current_User = Users[0]
last_used = None
Current_Popup = None


# -------------------------------------------------------------------------------------------------
class LabelTlo(Label):
    pass


class ScreenMenu(Screen):
    pass


class ScreenAdminMenu(Screen):
    pass


class ZapiszPopup(Popup):
    def __init__(self):
        super(ZapiszPopup, self).__init__()
        self.dd = DropDown()
        for x in range(6):
            a = Button(text="%s" % x, size_hint_y=None, height=33)
            a.bind(on_release=lambda a: self.dd.select(a.text))
            self.dd.add_widget(a)
        self.ilebutton = Button(text="Ile osob", size_hint=(0.2, 0.1))
        self.ilebutton.bind(on_release=self.dd.open)
        self.ids.popupmain.add_widget(self.ilebutton)
        self.dd.bind(on_select=lambda instance, z: setattr(self.ilebutton, 'text', z))
        self.anulujbutton = Button(text="Anuluj", size_hint=(0.2, 0.1), background_normal="czerwony.png")
        self.anulujbutton.bind(on_release=lambda a: App.get_running_app().root.anuluj())
        self.ids.popupmain.add_widget(self.anulujbutton)


class Zegarek(Label):
    def __init__(self, **kwargs):
        super(Zegarek, self).__init__(**kwargs)
        self.pos = (200, 200)
        self.size = (500, 500)
        self.font_size = 25
        self.text = time.asctime()
        Clock.schedule_interval(self.refresh, 1)

    def refresh(self, *args):
        self.text = time.asctime()


class Kalendarz(BoxLayout):
    def __init__(self):
        super(Kalendarz, self).__init__()
        self.orientation = "vertical"
        self.cy = time.gmtime().tm_year
        Miesiac = BoxLayout(orientation="horizontal", size_hint=(1, None), height=33)
        self.m = time.gmtime().tm_mon
        Miesiac.add_widget(Button(text="Wstecz", on_release=lambda a: self.zmniejsz()))
        self.mon = Label(text="%s %s" % (MiesiacRoku[self.m], self.cy))
        Miesiac.add_widget(self.mon)
        Miesiac.add_widget(Button(text="Dalej", on_release=lambda a: self.zwieksz()))
        self.add_widget(Miesiac)
        self.Dni = GridLayout(cols=7)
        self.first = time.gmtime().tm_mday - time.gmtime().tm_wday
        self.Dni.clear_widgets()
        while (True):
            if (self.first > 7):
                self.first -= 7
            else:
                pm = 7 - self.first
                if (self.m > 1):
                    self.first = DniMiesiaca[self.m - 1] - pm
                    ile = (DniMiesiaca[self.m] + DniMiesiaca[self.m - 1] - self.first + 1) / 7
                else:
                    self.first = DniMiesiaca[12] - pm
                    ile = (DniMiesiaca[self.m] + DniMiesiaca[12] - self.first + 1) / 7
                break

        if (round(ile) < ile):
            self.i = (round(ile) + 1) * 7
        else:
            self.i = round(ile) * 7

        cd = self.first
        if (self.m > 1):
            cm = self.m - 1
        else:
            cm = 12
        for x in ["Pon", "Wt", "Sr", "Czw", "Pt", "Sob", "Nd"]:
            self.Dni.add_widget(Label(text=x))
        counter = 0
        odczyt = self.first
        odczytm = self.m - 1
        dzien = 0
        for x in range(0, self.i):
            if (dzien >= 7):
                dzien = 1
            else:
                dzien += 1
            if (cm != self.m):
                if (App.get_running_app().root.opcja != "Admin"):
                    self.Dni.add_widget(Button(id="%s//%s-%s" % (DniTygodnia[dzien], odczyt, odczytm), text="%s" % cd,
                                               background_color=(1, 1, 1, 0.75),
                                               on_release=lambda a: self.otworz(a.id)))
                else:
                    self.Dni.add_widget(Button(id="%s//%s-%s" % (DniTygodnia[dzien], odczyt, odczytm), text="%s" % cd,
                                               background_color=(1, 1, 1, 0.75), on_release=lambda a: self.wybor(a.id)))
            else:
                if (App.get_running_app().root.opcja != "Admin"):
                    self.Dni.add_widget(Button(id="%s//%s-%s" % (DniTygodnia[dzien], odczyt, odczytm), text="%s" % cd,
                                               background_color=(1, 1, 1, 1), on_release=lambda a: self.otworz(a.id)))
                else:
                    self.Dni.add_widget(Button(id="%s//%s-%s" % (DniTygodnia[dzien], odczyt, odczytm), text="%s" % cd,
                                               background_color=(1, 1, 1, 1), on_release=lambda a: self.wybor(a.id)))

            self.last = cd
            if (cd == DniMiesiaca[cm]):
                cd = 1
                if (cm == 12):
                    cm = 1
                else:
                    cm += 1
            else:
                cd += 1
            counter += 1
            if (counter % 7 == 0):
                if (odczytm < self.m):
                    odczytm += 1
                odczyt = cd

        self.add_widget(self.Dni)

    def ustaw_komu(self, name):
        App.get_running_app().root.komu = name

    # nie dziala dodawanie w innym grafiku niz z obecnego tygodnia
    def wybor(self, date):
        kto = BoxLayout(orientation="vertical")
        for x in Users:
            kto.add_widget(Button(id=x.name, text="%s" % x.name, on_press=lambda a: self.ustaw_komu(a.id),
                                  on_release=lambda a: self.otworz(date)))
        if (App.get_running_app().root.opcja != "Admin"):
            App.get_running_app().root.MenuScr.ids.mojegrafikis.clear_widgets()
            App.get_running_app().root.MenuScr.ids.mojegrafikis.add_widget(kto)
        else:
            App.get_running_app().root.AdminMenuScr.ids.amojegrafikis.clear_widgets()
            App.get_running_app().root.AdminMenuScr.ids.amojegrafikis.add_widget(kto)

    def otworz(self, date):
        global Current_User
        data = date.split("//")
        Grafik = {}
        if (App.get_running_app().root.opcja != "Admin"):
            nazwa = "G%s_%s-%s-%s.txt" % (Current_User.name, data[1].split("-")[0], data[1].split("-")[1], self.cy)
        else:
            nazwa = "G%s_%s-%s-%s.txt" % (
                App.get_running_app().root.komu, data[1].split("-")[0], data[1].split("-")[1], self.cy)
        if (App.get_running_app().root.opcja != "Admin"):
            if (nazwa not in Current_User.grafiki):
                if (int(data[1].split("-")[1]) >= time.gmtime().tm_mon):
                    nazwa = "G%s-przyszly.txt" % App.get_running_app().root.komu
                    for x in DniTygodnia:
                        if (DniTygodnia[x] == data[0]):
                            tmp = x - 1
                    tmp2 = "%s//%s" % (data[0], int(data[1].split("-")[0]) + tmp)
                    data[0] = tmp2
                else:
                    self.wroc()
                    return
        else:
            Current_User.wczytaj_spis(obcy=App.get_running_app().root.komu)
            if (nazwa not in Current_User.inneGrafiki):
                if (int(data[1].split("-")[1]) >= time.gmtime().tm_mon):
                    nazwa = "G%s-przyszly.txt" % App.get_running_app().root.komu
                    for x in DniTygodnia:
                        if (DniTygodnia[x] == data[0]):
                            tmp = x - 1
                    tmp2 = "%s//%s" % (data[0], int(data[1].split("-")[0]) + tmp)
                    data[0] = tmp2

                else:
                    self.wroc()
                    return
        Current_User.innyGrafik = {}
        Current_User.wczytaj_inny_grafik(nazwa)
        App.get_running_app().root.n = nazwa
        for x in Current_User.innyGrafik:
            if ("%s" % data[0] in x):
                Grafik = Current_User.innyGrafik[x]
                kiedy = x
        print(Grafik)
        if (Grafik == {}):
            if (int(data[1].split("-")[0]) < time.gmtime().tm_mday):
                kiedy = "%s-%s-%s" % (data[0], int(data[1].split("-")[1]) + 1, self.cy)
            else:
                kiedy = "%s-%s-%s" % (data[0], data[1].split("-")[1], self.cy)
            print(kiedy)
            for i in range(9, 21):
                Grafik[i] = "ON\n"

        L = BoxLayout(orientation="vertical", size_hint=(1, 0.9),
                      pos=(0, 0))
        L.add_widget(MyButton(id="back", text="Powrot", background_normal="b3.png",
                              on_release=lambda a: self.wroc()))

        for x in Grafik:
            if ("ON\n" in Grafik[x]):
                btn = MyButton(id="inny%s" % x, text="%s.00-%s.50 WOLNE" % (x, x),
                               background_color=(0, 1, 0, 1))
                btn.bind(on_press=lambda a: self.zapispop(a.id, kiedy))
                L.add_widget(btn)

            else:
                btn = MyButton(id="inny%s" % x, text="%s.00-%s.50 ,%s" % (x, x, Grafik[x]),
                               background_color=(1, 0, 0, 1))
                btn.bind(on_press=lambda a: self.zapispop(a.id, kiedy))
                L.add_widget(btn)

        Current_User.innyGrafik = {}
        if (App.get_running_app().root.opcja != "Admin"):
            App.get_running_app().root.MenuScr.ids.mojegrafikis.clear_widgets()
            App.get_running_app().root.MenuScr.ids.mojegrafikis.add_widget(L)
        else:
            App.get_running_app().root.AdminMenuScr.ids.amojegrafikis.clear_widgets()
            App.get_running_app().root.AdminMenuScr.ids.amojegrafikis.add_widget(L)

    def wroc(self):
        self.__init__()
        if (App.get_running_app().root.opcja == "Admin"):
            App.get_running_app().root.AdminMenuScr.ids.amojegrafikis.clear_widgets()
            App.get_running_app().root.AdminMenuScr.ids.amojegrafikis.add_widget(Kalendarz())
        else:
            App.get_running_app().root.MenuScr.ids.mojegrafikis.clear_widgets()
            App.get_running_app().root.MenuScr.ids.mojegrafikis.add_widget(Kalendarz())

    def zapispop(self, aid, kiedy):
        global last_used, Current_Popup
        App.get_running_app().root.mojegrafiki = True
        App.get_running_app().root.kiedy = kiedy
        last_used = aid
        Current_Popup = ZapiszPopup()
        Current_Popup.open()

    def zwieksz(self):
        if (self.m != 12 and self.m < time.gmtime().tm_mon + 1):
            self.m += 1
            self.mon.text = "%s %s" % (MiesiacRoku[self.m], self.cy)
            self.Dni.clear_widgets()
            if (self.last < 7):
                if (self.m > 1):
                    self.first = DniMiesiaca[self.m - 1] - (6 - self.last)
                else:
                    self.first = DniMiesiaca[12] - (6 - self.last)
            else:
                self.first = self.last - 6
            if (self.m > 1):
                ile = (DniMiesiaca[self.m] + DniMiesiaca[self.m - 1] - self.first + 1) / 7
            else:
                ile = (DniMiesiaca[self.m] + DniMiesiaca[12] - self.first + 1) / 7
            if (round(ile) < ile):
                self.i = (round(ile) + 1) * 7
            else:
                self.i = round(ile) * 7
            self.ustaw()
        elif (self.m == 12 and self.m < time.gmtime().tm_mon + 1):
            self.m = 1
            self.cy += 1
            self.mon.text = "%s %s" % (MiesiacRoku[self.m], self.cy)
            self.Dni.clear_widgets()
            if (self.last < 7):
                if (self.m > 1):
                    self.first = DniMiesiaca[self.m - 1] - (6 - self.last)
                else:
                    self.first = DniMiesiaca[12] - (6 - self.last)
            else:
                self.first = self.last - 6
            if (self.m > 1):
                ile = (DniMiesiaca[self.m] + DniMiesiaca[self.m - 1] - self.first + 1) / 7
            else:
                ile = (DniMiesiaca[self.m] + DniMiesiaca[12] - self.first + 1) / 7
            if (round(ile) < ile):
                self.i = (round(ile) + 1) * 7
            else:
                self.i = round(ile) * 7
            self.ustaw()

    def zmniejsz(self):
        if (self.m != 1 and self.m > time.gmtime().tm_mon - 1):
            self.m -= 1
            self.mon.text = "%s %s" % (MiesiacRoku[self.m], self.cy)
            self.Dni.clear_widgets()
            while (True):
                if (self.first > 7):
                    self.first -= 7
                else:
                    pm = 7 - self.first
                    if (self.m > 1):
                        self.first = DniMiesiaca[self.m - 1] - pm
                        ile = (DniMiesiaca[self.m] + DniMiesiaca[self.m - 1] - self.first + 1) / 7
                    else:
                        self.first = DniMiesiaca[12] - pm
                        ile = (DniMiesiaca[self.m] + DniMiesiaca[12] - self.first + 1) / 7
                    break
            if (round(ile) < ile):
                self.i = (round(ile) + 1) * 7
            else:
                self.i = round(ile) * 7
            self.ustaw()
        elif (self.m == 1 and self.m > time.gmtime().tm_mon - 1):
            self.cy -= 1
            self.m = 12
            self.mon.text = "%s %s" % (MiesiacRoku[self.m], self.cy)
            self.Dni.clear_widgets()
            while (True):
                if (self.first > 7):
                    self.first -= 7
                else:
                    pm = 7 - self.first
                    if (self.m > 1):
                        self.first = DniMiesiaca[self.m - 1] - pm
                        ile = (DniMiesiaca[self.m] + DniMiesiaca[self.m - 1] - self.first + 1) / 7
                    else:
                        self.first = DniMiesiaca[12] - pm
                        ile = (DniMiesiaca[self.m] + DniMiesiaca[12] - self.first + 1) / 7
                    break
            if (round(ile) < ile):
                self.i = (round(ile) + 1) * 7
            else:
                self.i = round(ile) * 7
            self.ustaw()

    def ustaw(self):
        cd = self.first
        if (self.m > 1):
            cm = self.m - 1
        else:
            cm = 12
        for x in ["Pon", "Wt", "Sr", "Czw", "Pt", "Sob", "Nd"]:
            self.Dni.add_widget(Label(text=x))
        counter = 0
        odczyt = self.first
        odczytm = self.m - 1
        dzien = 0
        for x in range(0, self.i):
            if (dzien >= 7):
                dzien = 1
            else:
                dzien += 1
            if (cm != self.m):
                if (App.get_running_app().root.opcja != "Admin"):
                    self.Dni.add_widget(Button(id="%s//%s-%s" % (DniTygodnia[dzien], odczyt, odczytm), text="%s" % cd,
                                               background_color=(1, 1, 1, 0.75),
                                               on_release=lambda a: self.otworz(a.id)))
                else:
                    self.Dni.add_widget(Button(id="%s//%s-%s" % (DniTygodnia[dzien], odczyt, odczytm), text="%s" % cd,
                                               background_color=(1, 1, 1, 0.75), on_release=lambda a: self.wybor(a.id)))
            else:
                if (App.get_running_app().root.opcja != "Admin"):
                    self.Dni.add_widget(Button(id="%s//%s-%s" % (DniTygodnia[dzien], odczyt, odczytm), text="%s" % cd,
                                               background_color=(1, 1, 1, 1), on_release=lambda a: self.otworz(a.id)))
                else:
                    self.Dni.add_widget(Button(id="%s//%s-%s" % (DniTygodnia[dzien], odczyt, odczytm), text="%s" % cd,
                                               background_color=(1, 1, 1, 1), on_release=lambda a: self.wybor(a.id)))

            self.last = cd
            if (cd == DniMiesiaca[cm]):
                cd = 1
                if (cm == 12):
                    cm = 1
                else:
                    cm += 1
            else:
                cd += 1
            counter += 1
            if (counter % 7 == 0):
                if (odczytm < self.m):
                    odczytm += 1
                odczyt = cd


class CustomLayout(BoxLayout):
    pass


class MyButton(Button):
    def __init__(self, **kwargs):
        super(MyButton, self).__init__(**kwargs)
        self.color = (1, 1, 1, 1)
        self.text_size = Window.width, self.height - 30
        self.halign = "center"
        self.valign = "middle"


class RozliczeniePop(Popup):
    def __init__(self, **kwargs):
        super(RozliczeniePop, self).__init__(**kwargs)
        Current_User.miesieczne.clear()
        if (App.get_running_app().root.opcja != "Admin"):
            Current_User.wczytaj_zarobki()
        else:
            Current_User.zarobki_admin()
        self.ids.mpop.add_widget(Label(text="Obecny miesiąc: \nNa czysto: %szł" % Current_User.tm))
        self.ids.mpop.add_widget(Label(text="Poprzedni miesiąc: \nNa czysto: %szł" % Current_User.p1m))
        self.ids.mpop.add_widget(Label(text="Dwa miesiące temu: \nNa czysto: %szł" % Current_User.p2m))
        self.ids.mpop.add_widget(Label(text="Ten sezon: \nNa czysto: %szł" % Current_User.ts))
        self.ids.mpop.add_widget(Label(text="Poprzedni sezon: \nNa czysto: %szł" % Current_User.p1s))
        self.ids.mpop.add_widget(Label(text="Dwa sezony temu: \nNa czysto: %szł" % Current_User.p2s))


# -------------------------------------------------------------------------------------------------
class mainScreenManager(ScreenManager):
    opcja = ""
    indeksy = {
        "MojeGrafiki": 0, "Dzisiaj": 1, "Zapisz": 2, "Rozliczenie": 3, "Atlas": 4,
        "AMojeGrafiki": 0, "ADzisiaj": 1, "AZapisz": 2, "ARozliczenie": 3, "AAtlas": 4,
    }

    def handler(self):
        global Current_User
        self.mojegrafiki = False
        self.kiedy = None
        for x in Users:
            if (x.name == App.get_running_app().root.ids.user.text):
                if (x.password == hash(App.get_running_app().root.ids.passw.text)):
                    Current_User = x
                    self.komu = Current_User.name
                    Current_User.aktualizuj()

                    if (x.permission == "User"):
                        self.opcja = "User"
                        self.MenuScr = ScreenMenu()
                        self.add_widget(self.MenuScr)
                        Clock.schedule_interval(self.Odswiez, 120)
                        App.get_running_app().root.current = "Menu"
                    else:
                        self.opcja = "Admin"
                        self.AdminMenuScr = ScreenAdminMenu()
                        self.add_widget(self.AdminMenuScr)
                        Clock.schedule_interval(self.AdminOdswiez, 120)
                        App.get_running_app().root.current = "AdminMenu"
                    return
        App.get_running_app().root.current = "WrongLogin"

    def Odswiez(self, *args):
        self.komu = Current_User.name
        self.mojegrafiki = False
        self.kiedy = None
        Current_User.aktualizuj()
        temp = self.MenuScr.ids.caro.current_slide
        temp = temp.name
        self.MenuScr.__init__()
        self.MenuScr.ids.caro.load_slide(self.MenuScr.ids.caro.slides[self.indeksy[temp]])

    def AdminOdswiez(self, *args):
        self.komu = Current_User.name
        self.mojegrafiki = False
        self.kiedy = None
        Current_User.aktualizuj()
        temp = self.AdminMenuScr.ids.Acaro.current_slide
        temp = temp.name
        self.AdminMenuScr.__init__()
        self.AdminMenuScr.ids.Acaro.load_slide(self.AdminMenuScr.ids.Acaro.slides[self.indeksy[temp]])

    def zapiszDzisiejszy(self):
        global last_used, Current_Popup, Current_User
        try:
            dzis = "%s-%s-%s" % (time.gmtime().tm_mday, time.gmtime().tm_mon, time.gmtime().tm_year)
            hr = last_used[4:]
            hr = int(hr)
            nazwa = Current_Popup.ids.imie.text
            wiek = Current_Popup.ids.age.text

            if (self.komu == Current_User.name):
                if (Current_Popup.ids.imie.text == ""):
                    if (self.mojegrafiki == True):
                        Current_User.wczytaj_inny_grafik(self.n)
                        temp = Current_User.innyGrafik["%s" % self.kiedy][hr]
                    else:
                        temp = Current_User.calyGrafik["%s//%s" % (DniTygodnia[time.gmtime().tm_wday + 1], dzis)][hr]
                    try:
                        nazwa = temp[0:temp.index("(")]
                        wiek = temp[temp.index("(") + 1:temp.index(")")]
                        wiek = wiek.strip(" lat")
                    except:
                        Current_User.aktualizujGrafik()
                        if (self.opcja == "User"):
                            self.Odswiez()
                        if (self.opcja == "Admin"):
                            self.AdminOdswiez()
                        self.mojegrafiki = False
                        Current_Popup.dismiss()
                        return
                if (self.mojegrafiki == True):
                    if (self.kiedy in Current_User.calyGrafik):
                        Current_User.calyGrafik["%s" % self.kiedy][hr] = "%s(%s lat) #%s os.\n" % (
                            nazwa, wiek, Current_Popup.ilebutton.text)
                    else:
                        Current_User.wczytaj_inny_grafik(self.n)
                        if (self.kiedy not in Current_User.innyGrafik):
                            Current_User.innyGrafik["%s" % self.kiedy] = {}
                            for i in range(9, 21):
                                Current_User.innyGrafik["%s" % self.kiedy][i] = "ON\n"
                        Current_User.innyGrafik["%s" % self.kiedy][hr] = "%s(%s lat) #%s os.\n" % (
                            nazwa, wiek, Current_Popup.ilebutton.text)
                        Current_User.zapisz_inny_grafik(self.n)
                        Current_User.innyGrafik.clear()
                    self.mojegrafiki = False
                else:
                    Current_User.calyGrafik["%s//%s" % (DniTygodnia[time.gmtime().tm_wday + 1], dzis)][
                        hr] = "%s(%s lat) #%s os.\n" % (nazwa, wiek, Current_Popup.ilebutton.text)
            else:
                if (self.mojegrafiki == False):
                    Current_User.wczytaj_inny_grafik(Current_User.Inni[self.komu])
                    print(Current_User.innyGrafik)
                else:
                    if (self.opcja == "Admin"):
                        Current_User.wczytaj_inny_grafik(self.n)
                        print(Current_User.innyGrafik)
                if (Current_Popup.ids.imie.text == ""):
                    if (self.mojegrafiki == True):
                        temp = Current_User.innyGrafik["%s" % self.kiedy][hr]
                    else:
                        temp = Current_User.innyGrafik["%s//%s" % (DniTygodnia[time.gmtime().tm_wday + 1], dzis)][hr]
                    try:
                        nazwa = temp[0:temp.index("(")]
                        wiek = temp[temp.index("(") + 1:temp.index(")")]
                        wiek = wiek.strip(" lat")
                    except:
                        Current_User.aktualizujGrafik()
                        if (self.opcja == "User"):
                            self.Odswiez()
                        if (self.opcja == "Admin"):
                            self.AdminOdswiez()
                        self.mojegrafiki = False
                        Current_Popup.dismiss()
                        return
                if (self.mojegrafiki == True):
                    print("%s1" % Current_User.innyGrafik)
                    if (self.kiedy not in Current_User.innyGrafik):
                        Current_User.innyGrafik["%s" % self.kiedy] = {}
                        for i in range(9, 21):
                            Current_User.innyGrafik["%s" % self.kiedy][i] = "ON\n"
                    Current_User.innyGrafik["%s" % self.kiedy][hr] = "%s(%s lat) #%s os.\n" % (
                        nazwa, wiek, Current_Popup.ilebutton.text)
                    print("%s2" % Current_User.innyGrafik)
                    Current_User.zapisz_inny_grafik(self.n)
                else:
                    Current_User.innyGrafik["%s//%s" % (DniTygodnia[time.gmtime().tm_wday + 1], dzis)][
                        hr] = "%s(%s lat) #%s os.\n" % (nazwa, wiek, Current_Popup.ilebutton.text)
                    Current_User.zapisz_inny_grafik(Current_User.Inni[self.komu])
            Current_User.aktualizujGrafik()
            if (self.opcja == "User"):
                self.Odswiez()
            if (self.opcja == "Admin"):
                self.AdminOdswiez()
            self.mojegrafiki = False
            Current_Popup.dismiss()
        except:
            Current_User.aktualizujGrafik()
            if (self.opcja == "User"):
                self.Odswiez()
            if (self.opcja == "Admin"):
                self.AdminOdswiez()
            self.mojegrafiki = False
            Current_Popup.dismiss()
            return

    def anuluj(self):  # nie usuwa z mojegrafiki admin
        global last_used, Current_Popup, Current_User
        hr = last_used[4:]
        dzis = "%s-%s-%s" % (time.gmtime().tm_mday, time.gmtime().tm_mon, time.gmtime().tm_year)
        hr = int(hr)
        if (self.mojegrafiki == True):
            if (self.kiedy in Current_User.calyGrafik and self.komu == Current_User.name):
                Current_User.calyGrafik["%s" % self.kiedy][hr] = "ON\n"
            else:
                Current_User.wczytaj_inny_grafik(self.n)
                Current_User.innyGrafik["%s" % self.kiedy][hr] = "ON\n"
                Current_User.zapisz_inny_grafik(self.n)
        else:
            Current_User.calyGrafik["%s//%s" % (DniTygodnia[time.gmtime().tm_wday + 1], dzis)][hr] = "ON\n"
        Current_User.aktualizujGrafik()
        if (self.opcja == "User"):
            self.Odswiez()
        if (self.opcja == "Admin"):
            self.AdminOdswiez()
        Current_Popup.dismiss()
        self.mojegrafiki = False


# -------------------------------------------------------------------------------------------------
class Relogin(Screen):
    pass


class LoginScreen(Screen):
    pass


class Scroll(ScrollView):
    def __init__(self, **kwargs):
        super(Scroll, self).__init__(**kwargs)
        self.size_hint = (None, None)
        self.size = Window.size


class Karuzela(Carousel):
    def __init__(self, **kwargs):
        super(Karuzela, self).__init__(**kwargs)

    def on_index(self, *args):
        super(Karuzela, self).on_index(*args)
        temp = self.current_slide.tab
        if (App.get_running_app().root.opcja == "User"):
            for x in ['tab0', 'tab1', 'tab2', 'tab3', 'tab4']:
                App.get_running_app().root.MenuScr.ids[x].state = 'normal'
            temp.state = 'down'
        if (App.get_running_app().root.opcja == "Admin"):
            for x in ['Atab0', 'Atab1', 'Atab2', 'Atab3', 'Atab4']:
                App.get_running_app().root.AdminMenuScr.ids[x].state = 'normal'
            temp.state = 'down'


class MojeGrafikiS(Screen):
    def __init__(self, **kwargs):
        super(MojeGrafikiS, self).__init__(**kwargs)
        self.add_widget(Kalendarz())


class DzisiajS(Screen):
    def __init__(self, **kwargs):
        global Current_User
        super(DzisiajS, self).__init__(**kwargs)
        L = BoxLayout(orientation="vertical", size_hint=(1, 0.9),
                      pos=(0, 0))
        L.add_widget(MyButton(id="refresh", text="Odswiez", background_normal="b3.png",
                              on_release=lambda a: self.refresh()))
        for x in Current_User.dzisiejszy:
            if ("ON\n" in Current_User.dzisiejszy[x]):
                btn = MyButton(id="dzis%s" % x, text="%s.00-%s.50 WOLNE" % (x, x),
                               background_color=(0, 1, 0, 1))
                btn.bind(on_press=lambda a: self.ustaw_sobie(), on_release=lambda a: self.zapispop(a.id))
                L.add_widget(btn)

            else:
                btn = MyButton(id="dzis%s" % x, text="%s.00-%s.50 ,%s" % (x, x, Current_User.dzisiejszy[x]),
                               background_color=(1, 0, 0, 1))
                btn.bind(on_press=lambda a: self.ustaw_sobie(), on_release=lambda a: self.zapispop(a.id))
                L.add_widget(btn)
        self.add_widget(L)

    def ustaw_sobie(self):
        App.get_running_app().root.komu = Current_User.name

    def zapispop(self, aid):
        global last_used, Current_Popup
        last_used = aid
        Current_Popup = ZapiszPopup()
        Current_Popup.open()

    def refresh(self):
        if (App.get_running_app().root.opcja == "User"):
            App.get_running_app().root.Odswiez()
        if (App.get_running_app().root.opcja == "Admin"):
            App.get_running_app().root.AdminOdswiez()


class ZapiszS(Screen):
    def __init__(self, **kwargs):
        super(ZapiszS, self).__init__(**kwargs)
        Lay = BoxLayout(orientation="vertical")
        self.ddm = DropDown(auto_dismiss=True)
        cHour = time.gmtime().tm_hour + 2
        for i in range(cHour, 21):
            Lay.add_widget(Button(id=str(i), markup=True, text="[color=000000]%s.00 - %s.50[/color]" % (i, i),
                                  background_color=(123, 123, 123, 1), on_press=lambda a: self.dostepnosc(a),
                                  on_release=self.ddm.open))

        self.add_widget(Lay)

    def dostepnosc(self, instance):
        # DO ZAMIANY TEXT BUTTONOW NA %(X,ILOSC LEKCJI)
        Current_User.aktualizuj()
        godzina = int(instance.id)
        self.ddm.clear_widgets()
        self.confirm_Pop = ZapiszPopup()
        for x in Current_User.dostepni[godzina]:
            if (x == Current_User.name):
                self.ddm.add_widget(Button(id=str(x), size_hint_y=None, height=33
                                           , text="[color=FF0000][b]%s : %s[/b][/color]" % (x, Current_User.licznik[x]),
                                           markup=True, background_color=(0, 1, 0, 1)
                                           , on_release=lambda b: self.do_kogo(b, godzina)))
            else:
                self.ddm.add_widget(Button(id=str(x), size_hint_y=None, height=33
                                           , text="%s : %s" % (x, Current_User.licznik[x]), markup=True,
                                           background_color=(0, 1, 0, 1)
                                           , on_release=lambda b: self.do_kogo(b, godzina)))

    def do_kogo(self, instance, godzina):
        global last_used, Current_Popup
        App.get_running_app().root.komu = instance.id
        self.ddm.dismiss()
        last_used = "dzis%s" % godzina
        Current_Popup = self.confirm_Pop
        Current_Popup.open()


class RozliczenieS(
    Screen):  # Trzeba zrobic dodawanie automatyczne grafikow, bo gdy ktos nie ma grafiku to nadpisuje stan poprzedniego ziomka
    ceny = {
        1: 60,
        2: 90,
        3: 120,
        4: 140,
        5: 150
    }

    def __init__(self, **kwargs):
        super(RozliczenieS, self).__init__(**kwargs)
        Layoucik = CustomLayout()
        self.roz_dd = DropDown()
        self.cweek = DropDown()
        self.userzy_dd = DropDown()
        self.more_popup = RozliczeniePop()

        btn = Button(markup=True, id="%d" % (time.gmtime().tm_wday + 1),
                     text="[color=000000]Rozliczenie z dziś[/color]",
                     background_color=(123, 123, 123, 1), color=(1, 1, 1, 1))
        if (App.get_running_app().root.opcja != "Admin"):
            btn.bind(on_press=lambda a: self.rozliczenie(a, 0), on_release=self.roz_dd.open)
        else:
            btn.bind(on_press=lambda a: self.pokaz_rozliczenia(a, 0), on_release=self.userzy_dd.open)
        Layoucik.add_widget(btn)
        Layoucik.add_widget(Button(markup=True, id="cweek", text="[color=000000]Bierzacy tydzien[/color]",
                                   background_color=(123, 123, 123, 1), color=(1, 1, 1, 1),
                                   on_press=lambda a: self.dodaj(a), on_release=self.cweek.open))
        Layoucik.add_widget(Button(markup=True, id="p1week", text="[color=000000]Poprzedni tydzien[/color]",
                                   background_color=(123, 123, 123, 1), color=(1, 1, 1, 1),
                                   on_press=lambda a: self.dodaj(a), on_release=self.cweek.open))
        Layoucik.add_widget(Button(markup=True, id="p2week", text="[color=000000]Dwa tygodnie temu[/color]",
                                   background_color=(123, 123, 123, 1), color=(1, 1, 1, 1),
                                   on_press=lambda a: self.dodaj(a), on_release=self.cweek.open))
        Layoucik.add_widget(Button(markup=True, id="more", text="[color=000000][b]Wiecej...[/b][/color]",
                                   background_color=(123, 123, 123, 1), color=(1, 1, 1, 1),
                                   on_release=lambda a: self.otworz_wiecej()))
        self.add_widget(Layoucik)

    def pokaz_rozliczenia(self, instance, wstecz):
        self.userzy_dd.clear_widgets()
        for x in Users:
            self.userzy_dd.add_widget(Button(size_hint_y=None, height=50, markup=True, id="%s" % x.name,
                                             text="[color=000000]%s[/color]" % x.name,
                                             background_color=(123, 123, 123, 1), color=(1, 1, 1, 1),
                                             on_press=lambda a: self.rozliczenie(instance, wstecz, obcy=a.id),
                                             on_release=self.roz_dd.open))

    def otworz_wiecej(self):
        self.more_popup.open()

    def dodaj(self, instance):
        self.cweek.clear_widgets()
        if (App.get_running_app().root.opcja != "Admin"):
            if (instance.id == "cweek"):
                for x in DniTygodnia:
                    if (x != time.gmtime().tm_wday + 1):
                        self.cweek.add_widget(MyButton(size_hint_y=None, height=50,
                                                       markup=True, id="%d" % x,
                                                       text='[color=000000]%s[/color]' % DniTygodnia[x],
                                                       background_color=(123, 123, 123, 1), color=(1, 1, 1, 1),
                                                       on_press=lambda a: self.rozliczenie(a, 0)
                                                       , on_release=self.roz_dd.open))
            if (instance.id == "p1week"):
                for x in DniTygodnia:
                    self.cweek.add_widget(MyButton(size_hint_y=None, height=50,
                                                   markup=True, id="%d" % x,
                                                   text='[color=000000]%s[/color]' % DniTygodnia[x],
                                                   background_color=(123, 123, 123, 1), color=(1, 1, 1, 1),
                                                   on_press=lambda a: self.rozliczenie(a, -1)
                                                   , on_release=self.roz_dd.open))
            if (instance.id == "p2week"):
                for x in DniTygodnia:
                    self.cweek.add_widget(MyButton(size_hint_y=None, height=50,
                                                   markup=True, id="%d" % x,
                                                   text='[color=000000]%s[/color]' % DniTygodnia[x],
                                                   background_color=(123, 123, 123, 1), color=(1, 1, 1, 1),
                                                   on_press=lambda a: self.rozliczenie(a, -2)
                                                   , on_release=self.roz_dd.open))
        else:
            if (instance.id == "cweek"):
                for x in DniTygodnia:
                    if (x != time.gmtime().tm_wday + 1):
                        self.cweek.add_widget(MyButton(size_hint_y=None, height=50,
                                                       markup=True, id="%d" % x,
                                                       text='[color=000000]%s[/color]' % DniTygodnia[x],
                                                       background_color=(123, 123, 123, 1), color=(1, 1, 1, 1),
                                                       on_press=lambda a: self.rozlicz_all(a, 0)
                                                       , on_release=self.roz_dd.open))
            if (instance.id == "p1week"):
                for x in DniTygodnia:
                    self.cweek.add_widget(MyButton(size_hint_y=None, height=50,
                                                   markup=True, id="%d" % x,
                                                   text='[color=000000]%s[/color]' % DniTygodnia[x],
                                                   background_color=(123, 123, 123, 1), color=(1, 1, 1, 1),
                                                   on_press=lambda a: self.rozlicz_all(a, -1)
                                                   , on_release=self.roz_dd.open))
            if (instance.id == "p2week"):
                for x in DniTygodnia:
                    self.cweek.add_widget(MyButton(size_hint_y=None, height=50,
                                                   markup=True, id="%d" % x,
                                                   text='[color=000000]%s[/color]' % DniTygodnia[x],
                                                   background_color=(123, 123, 123, 1), color=(1, 1, 1, 1),
                                                   on_press=lambda a: self.rozlicz_all(a, -2)
                                                   , on_release=self.roz_dd.open))

    def rozlicz_all(self, instance, wstecz):
        counter = 0
        for x in Users:
            self.rozliczenie(instance, wstecz, obcy=x.name)
            counter += self.suma

        self.roz_dd.clear_widgets()
        self.roz_dd.add_widget(LabelTlo(size_hint_y=None,
                                        height=1))
        # -------------------------------------------------
        self.roz_dd.add_widget(LabelTlo(size_hint_y=None, text="Zarobione lacznie: %s zl" % counter,
                                        height=33))
        self.roz_dd.add_widget(LabelTlo(size_hint_y=None, text="Zarobione na czysto: %s zl" % (counter / 2),
                                        height=33))

    def rozliczenie(self, instance, wstecz, **kwargs):
        global Current_User
        self.roz_dd.clear_widgets()
        self.suma = 0
        Graph = {}
        if ("obcy" in kwargs):
            Current_User.wczytaj_spis(obcy=kwargs["obcy"])

            if (wstecz == 0):
                if (Current_User.inneGrafiki.__len__() >= 1):
                    Current_User.wczytaj_inny_grafik(Current_User.inneGrafiki[Current_User.inneGrafiki.__len__() - 1])
                    print(Current_User.inneGrafiki[Current_User.inneGrafiki.__len__() - 1])
                    Graph = Current_User.innyGrafik

                else:
                    return
            elif (wstecz == -1):
                if (Current_User.inneGrafiki.__len__() >= 2):
                    Current_User.wczytaj_inny_grafik(Current_User.inneGrafiki[Current_User.inneGrafiki.__len__() - 2])
                    print(Current_User.inneGrafiki[Current_User.inneGrafiki.__len__() - 2])
                    Graph = Current_User.innyGrafik
                else:
                    return
            elif (wstecz == -2):
                if (Current_User.inneGrafiki.__len__() >= 3):
                    Current_User.wczytaj_inny_grafik(Current_User.inneGrafiki[Current_User.inneGrafiki.__len__() - 3])
                    print(Current_User.inneGrafiki[Current_User.inneGrafiki.__len__() - 3])
                    Graph = Current_User.innyGrafik
                else:
                    return
        else:
            if (wstecz == 0):
                Graph = Current_User.calyGrafik
            elif (wstecz == -1):
                if (Current_User.grafiki.__len__() >= 2):
                    Current_User.wczytaj_inny_grafik(Current_User.grafiki[Current_User.grafiki.__len__() - 2])
                    Graph = Current_User.innyGrafik
                else:
                    return
            elif (wstecz == -2):
                if (Current_User.grafiki.__len__() >= 3):
                    Current_User.wczytaj_inny_grafik(Current_User.grafiki[Current_User.grafiki.__len__() - 3])
                    Graph = Current_User.innyGrafik
                else:
                    return
        dzien = DniTygodnia[int(instance.id)]
        n = ""
        for x in Graph:
            if (dzien in x):
                n = x
        print(Graph[n])
        for x in Graph[n]:
            try:
                if ("ON\n" not in Graph[n][x]):
                    i = Graph[n][x]
                    self.suma += self.ceny[int(i[i.index("#") + 1:i.index("#") + 3].strip())]
                    print(self.suma)
            except(ValueError):
                self.roz_dd.add_widget(LabelTlo(size_hint_y=None, text="Zle wybrane ilosci osob",
                                                height=33))
        # Tutaj wrzucam jeden label, bo pierwszego nie widać , do poprawki !
        self.roz_dd.add_widget(LabelTlo(size_hint_y=None,
                                        height=1))
        # -------------------------------------------------
        self.roz_dd.add_widget(LabelTlo(size_hint_y=None, text="Zarobione lacznie: %s zl" % self.suma,
                                        height=33))
        self.roz_dd.add_widget(LabelTlo(size_hint_y=None, text="Zarobione na czysto: %s zl" % (self.suma / 2),
                                        height=33))


class AtlasS(Screen):
    def __init__(self, **kwargs):
        super(AtlasS, self).__init__(**kwargs)
        L = BoxLayout(orientation="vertical", size_hint=(0.5, 0.5))
        L.add_widget(Button(text="Wyloguj", on_press=lambda a: self.wyloguj()))
        self.add_widget(L)

    def wyloguj(self):
        global Current_User
        App.get_running_app().root.clear_widgets()
        Current_User = None
        App.get_running_app().root.current = "scLogin"


def zapisz():
    pass


def utworz():
    for x in Users:
        plik = open("G%s_%s-%s-%s.txt" % (x.name, time.gmtime().tm_mday, time.gmtime().tm_mon, time.gmtime().tm_year),
                    'w')
        for i in DniTygodnia.values():
            plik.write("%s||ON\n" % i)
            for j in range(9, 21):
                plik.write("%s.00-%s.50||ON\n" % (j, j))
        plik.close()


def wczytaj():
    for x in Users:
        plik = open("G%s_%s-%s-%s.txt" % (x, time.gmtime().tm_mday, time.gmtime().tm_mon, time.gmtime().tm_year), 'r')
        map = {}
        Grafiki = []
        Stany = []
        for y in plik:
            y.lstrip()
            temp = y.split("||")
            Grafiki.append(temp[0])
            Stany.append(temp[1])
        map[x] = []
        map[x].append(Grafiki)
        map[x].append(Stany)
    del Grafiki, Stany


def wczytajUserow():
    global ObecneGrafiki, Userzy
    plik = open("Userzy.txt", "r")
    for line in plik:
        temp = line.split("||")
        ObecneGrafiki[temp[0]] = temp[2]
        Userzy[temp[0]] = temp[1]
    plik.close()


def utworzUserow():
    plik = open("Userzy.txt", "w")
    for x in Users:
        plik.write("%s||%s||G%s_1-6-2016.txt\n" % (x.name, x.password, x.name))
    plik.close()


# --------------------------------------------------------------------------------------------------
class FinanseWidget(Widget):
    pass


class FinanseApp(App):
    def build(self):
        wczytajUserow()
        F = mainScreenManager()
        return F


if (__name__ == "__main__"):
    FinanseApp().run()
    # --------------------------------------------------------------------------------------------------
    # PRZYPOMNIENIA
    # ZROBIC WIECEJ_POPUP W rozliczeniach, pokazujacy
    # kase z tego miesiaca, 2 poprzednich, tego sezonu, i 2 poprzednich.
