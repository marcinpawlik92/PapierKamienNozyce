from kivy.uix.widget import Widget
from kivy.app import App
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivymd.uix.textfield import MDTextField
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.utils.fpsmonitor import FpsMonitor
from kivy.core.window import Window
from kivymd.icon_definitions import md_icons
from kivymd.uix.button import MDRectangleFlatButton
from kivy.uix.image import Image
import random
from kivy.uix.button import Button



class PKNApp(MDApp):
    def build(self):

        pass
    def get_data(self):
        player_input = self.root.ids.first.ids.username.text #id ekranu pierwszego i id TextFieldu + text przypisane do zmiennej
        self.root.ids.second.ids.lab.text = player_input #id ekranu drugiego i id Labelu + text równa sie inputowi użytkownika
    def draw_computer(self): # metoda losująca obrazek dla przycisuku o id 'computer_button' pod labelem Computer
        # self.root.ids.second.ids.papier.text
        self.root.ids.second.ids.computer_button.background_normal = random.choice(['scissors.png', 'paper.png', 'rock.png']) #id ekranu drugiego i id przycisku + jego background zmieniają się po wciśnieciu przycisku papier (losuje obrazek dla przycisku)
        if self.root.ids.second.ids.computer_button.background_normal == 'scissors.png':
            self.root.ids.second.ids.computer_button.size = 160, 200
        elif self.root.ids.second.ids.computer_button.background_normal == 'paper.png':
            self.root.ids.second.ids.computer_button.size = 200, 300
        else: self.root.ids.second.ids.computer_button.size = 150, 120



    def player_choice_rock(self):
        if self.root.ids.second.ids.computer_button.background_normal == self.root.ids.second.ids.kamien.background_normal:     # jesli obrazek wybrany przez gracza równa się obrazkowi wylosowanemy przez komputer wypisz REMIS
            self.root.ids.second.ids.remis.text = 'REMIS'
        elif self.root.ids.second.ids.computer_button.background_normal == 'scissors.png' and self.root.ids.second.ids.kamien.background_normal == 'rock.png':  # jesli background przycisku komputera rowna się obrazkowi kamienia i użytkownik wybrał obrazek nożyczek to gracz przegrywa
            self.root.ids.second.ids.remis.text = "Wygrywasz! Kamień tępi nożyce"
        elif self.root.ids.second.ids.computer_button.background_normal == 'paper.png' and self.root.ids.second.ids.kamien.background_normal == 'rock.png':          #jesli background przycisku komputera rowna się obrazkowi papieru i użytkownik wybrał obrazek kamienia to gracz przegrywa
            self.root.ids.second.ids.remis.text = "Przegrywasz! Papier przykrywa kamień"

    def player_choice_paper(self):
        if self.root.ids.second.ids.computer_button.background_normal == self.root.ids.second.ids.papier.background_normal:     # jesli obrazek wybrany przez gracza równa się obrazkowi wylosowanemy przez komputer wypisz REMIS
            self.root.ids.second.ids.remis.text = 'REMIS'
        elif self.root.ids.second.ids.computer_button.background_normal == 'rock.png' and self.root.ids.second.ids.papier.background_normal == 'paper.png':  # jesli background przycisku komputera rowna się obrazkowi papieru i użytkownik wybrał obrazek kamienia to gracz przegrywa
            self.root.ids.second.ids.remis.text = "Wygrywasz! Papier przykrywa kamień"
        elif self.root.ids.second.ids.computer_button.background_normal == 'scissors.png' and self.root.ids.second.ids.papier.background_normal == 'paper.png':  # jesli background przycisku komputera rowna się obrazkowi nozyczek i użytkownik wybrał obrazek papieru to gracz przegrywa
            self.root.ids.second.ids.remis.text = "Przegrywasz! Nożyczki tną papier"

    def player_choice_scissors(self):
        if self.root.ids.second.ids.computer_button.background_normal == self.root.ids.second.ids.nozyce.background_normal:     # jesli obrazek wybrany przez gracza równa się obrazkowi wylosowanemy przez komputer wypisz REMIS
            self.root.ids.second.ids.remis.text = 'REMIS'
        elif self.root.ids.second.ids.computer_button.background_normal == 'rock.png' and self.root.ids.second.ids.nozyce.background_normal == 'scissors.png':  # jesli background przycisku komputera rowna się obrazkowi nozyczek i użytkownik wybrał obrazek papieru to gracz przegrywa
            self.root.ids.second.ids.remis.text = "Przegrywasz! Kamień tępi nożyczki"
        elif self.root.ids.second.ids.nozyce.background_normal == 'scissors.png' and self.root.ids.second.ids.computer_button.background_normal == 'paper.png':
            self.root.ids.second.ids.remis.text = "Wygrywasz! Nożyczki tną papier"











PKNApp().run()

    # def get_data(self):
    #     #player_name = self.root.ids.username.text #bierze siebie, pozniej root i jego id (username) i text tego id
    #     widg = PKNGame()
    #     return widg


        # self.theme_cls.primary_palette = "Purple"  # "Purple", "Red"
        # self.theme_cls.primary_hue = "500"  # "500"
        # self.theme_cls.theme_style = "Light"  # "Light"
        # username = MDTextField(text="Enter player name", mode="rectangle", icon_right="scissors-cutting", pos_hint={'center_x': 0.5, 'center_y': 0.5}, size_hint_x=None, width=300)
        # fbutton = MDRectangleFlatButton(text="Submit", pos_hint={'center_x': .5, 'center_y': 0.4}, on_press=username.ids.userdata.text)
        # monitor = FpsMonitor()
        # monitor.start()
        # screen.add_widget(username)
        # screen.add_widget(monitor)
        # screen.add_widget(fbutton)

        #return screen



# class PKNApp(MDApp):
#     def build(self):
#         screen = PKNGame()
#         username = MDTextField(text="Enter player name", pos_hint={'center_x': 0.5, 'center_y': 0.5}, size_hint=(0.5,1))
#         screen.add_widget(username)
#         return screen

# class PKNApp(App):
#     def build(self):
#         game = PKNGame()
#
#         return game




# from kivy.app import App
# from kivy.lang import Builder
# from kivy.uix.screenmanager import ScreenManager, Screen
#
# # Create both screens. Please note the root.manager.current: this is how
# # you can control the ScreenManager from kv. Each screen has by default a
# # property manager that gives you the instance of the ScreenManager used.
# Builder.load_string("""
# <MenuScreen>:
#     BoxLayout:
#         Button:
#             text: 'Goto settings'
#             on_press: root.manager.current = 'settings'
#         Button:
#             text: 'Quit'
#
# <SettingsScreen>:
#     BoxLayout:
#         Button:
#             text: 'My settings button'
#         Button:
#             text: 'Back to menu'
#             on_press: root.manager.current = 'menu'
# """)
#
# # Declare both screens
# class MenuScreen(Screen):
#     pass
#
# class SettingsScreen(Screen):
#     pass
#
# class TestApp(App):
#
#     def build(self):
#         # Create the screen manager
#         sm = ScreenManager()
#         sm.add_widget(MenuScreen(name='menu'))
#         sm.add_widget(SettingsScreen(name='settings'))
#
#         return sm
#
# if __name__ == '__main__':
#     TestApp().run()