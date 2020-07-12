import kivy
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

# Username (TestInput)
# Password (TestInput)
# Sign in  (Button)
# Create Account (Button)
class HomePage(Widget):
    pass

# Welcome (Label)
# Thank you (Label)
# let's set up (Label)
# Username (TestInput)
# Password (TestInput)
# Confirm (TestInput)
# Create! (button)
class CreateAccount(Widget):
    pass

class TransitApp(App):
    def build(self):
        return HomePage()


if __name__ == '__main__':
    TransitApp().run()
