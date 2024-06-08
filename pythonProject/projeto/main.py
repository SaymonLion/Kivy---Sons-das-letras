from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.layout import Layout

Window.size = (320, 500)
alfabeto = ["A", "B", "C", "D", "E", "F", "G", "H", 
          "I", "J", "K", "L", "M", "N", "O", "P", 
          "Q", "R", "S", "T", "U", "V", "W", "X", 
          "Y", "Z"]

class TelaInicial(Screen):
    pass

class TelaAlfabeto(Screen):
    pass

class TelaBrincar(Screen):
    pass

class TelaCriar(Screen):
    pass
    #def inserir_letras(self):
    #    grid_letras = self.root.ids.grade
    #    for letra in alfabeto:
    #        btn = Button(text=str(letra), size_hint_y=None, height=40)
    #        grid_letras.add_wiget(btn)

class Auxiliar(ScreenManager):
    pass

class Carregar(App):
    def build(self):
        return Builder.load_file("kivy.kv")
    
Carregar().run()