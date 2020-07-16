import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.config import Config

# Set window size
#   Pixel dimensions for a Samsung Galaxy S9 are 1440 x 2960,
#   scaled window by a factor of 0.25 to get 360 x 740
Config.set('graphics', 'width', '360')
Config.set('graphics', 'height', '740')

# Load in the style document named 'Transit.kv'
Builder.load_file( 'Transit.kv' )

# Username (TestInput)
# Password (TestInput)
# Sign in  (Button)
# Create Account (Button)
class Login(Screen):
    pass

# Welcome (Label)
# Thank you (Label)
# let's set up (Label)
# Username (TestInput)
# Password (TestInput)
# Confirm (TestInput)
# Create! (button)
class CreateAccount(Screen):
    pass

# Create the screen manager
sm = ScreenManager()
sm.add_widget(Login(name='Login'))
sm.add_widget(CreateAccount(name='CreateAccount'))

class TransitApp(App):
    def build(self):
        return sm

if __name__ == '__main__':
    TransitApp().run()
