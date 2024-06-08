from kivy.app import App
from kivy.lang import Builder
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
import numpy as np

Window.size = (400, 600)

class TelaInicial(ScrollView):
    pass

class Carregar(App):
    def build(self):
        return Builder.load_file("kivy.kv")
    
Carregar().run()

