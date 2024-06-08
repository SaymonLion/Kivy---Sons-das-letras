from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.layout import Layout
from kivy.core.audio import SoundLoader

Window.clearcolor = [0.9, 0.9, 0.9, 1]

Window.size = (320, 500)

class TelaInicial(Screen):
    pass

class TelaAlfabeto(Screen):
    pass
    #def inserir_letras(self):
    #    grid_letras = self.root.ids.grade
    #    for letra in alfabeto:
    #        btn = Button(text=str(letra), size_hint_y=None, height=40)
    #        grid_letras.add_wiget(btn)

class TelaBrincar(Screen):
    pass

class TelaCriar(Screen):
    somA = None
    somB = None
    def digitar_silaba(self, button, somA):
        if somA == None:
            self.somA = SoundLoader.load('audio/a.mp3')
        self.somA.play()
        label = self.root.ids.digitar
        novo_texto = f"{label.text}{button.text}".strip()
        label.text = novo_texto
    

class Auxiliar(ScreenManager):
    pass

class Carregar(App):
    def build(self):
        return Builder.load_file("kivy2.kv")
    
Carregar().run()