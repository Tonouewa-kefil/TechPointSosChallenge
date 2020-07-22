import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Color, Rectangle
from kivy.uix.widget import Widget
from kivy.uix.button import Button, ButtonBehavior
from kivy.uix.image import Image
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty


class SymptomHistoryScreen(Screen):
    ob1 = ObjectProperty(None)
    ob2 = ObjectProperty(None)
    pass

Window.size = (375, 667)
kv = Builder.load_file("symlog.kv")


class SymlogApp(App):
    def build(self):

        return kv

if __name__ == '__main__':
    SymlogApp().run()