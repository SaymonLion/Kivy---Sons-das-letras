from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager,Screen
Window.size = (400, 600)

class TelaInicial(Screen):
    def sair(self):
        App.get_running_app().stop()
        Window.close()

class TelaAlfabeto(Screen):
    def tela_alfabeto(self):
        pass

class TelaBrincar(Screen):
    def tela_brincar(self):
        pass

class TelaCriar(Screen):
    def tela_criar(self):
        pass

class Auxiliar(ScreenManager):
    pass

class Bingo(App):
    def build(self):
        return Builder.load_file('tela.kv')

Bingo().run()