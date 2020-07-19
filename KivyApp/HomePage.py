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

import sqlite3

# Creating a database to keep the record of the UserInput
connection = sqlite3.connect('Transit_User.db')
cur = connection.cursor()
connection.commit()

# Set window size
#   Pixel dimensions for a Samsung Galaxy S9 are 1440 x 2960,
#   scaled window by a factor of 0.25 to get 360 x 740
Window.size = (360, 740)
#Config.set('graphics', 'width', '360')
#Config.set('graphics', 'height', '740')

# Username (TestInput)
# Password (TestInput)
# Sign_in  (Button)
# Create_account (Button)
class HomeScreen(Screen):
    username = ObjectProperty(None)
    password = ObjectProperty(None)
    sign_in = ObjectProperty(None)
    create_account = ObjectProperty(None)

    def signing_in(self):
        print("Username: " + self.username.text + "\n" + "Password: " + self.password.text)
        # here we want to verify the record in our database
        # if it exist, we take the user to his profile
        # if not we display an error message
        self.username.text = ""
        self.password.text = ""

        # If verification is successful, return true
        #if...
        return true

    def create_new_account(self):
        print("I am here")

        # here we want to take the user credentials and save them into to our database
        # when the new account is created, we take them back to the login screen
        # if credentials are good, we show the user profile.
    pass
# Welcome (Label)
# Thank you (Label)
# let's set up (Label)
# Username (TestInput)
# Password (TestInput)
# Confirm (TestInput)
# Create! (button)
class CreateAccountScreen(Screen):
    go_back: ObjectProperty(None)
    username: ObjectProperty(None)
    password: ObjectProperty(None)
    confirmation: ObjectProperty(None)
    create: ObjectProperty(None)
    pass

class MainScreen(Screen):
    pass

class ProfileScreen(Screen):
    pass

# Recently(Label)
# 3 Buttons listing the transport
# See more button
# Information (Label)
class TransportationHistoryScreen(Screen):
    pass

# go_back (Button)
# Describe(Label)
# Item Description (TextInput)
# Best Way to contact you (Label)
# SMS Text(Button)
# Phone Call(Button)
# Email(Button)
class ItemDescriptionScreen(Screen):
    pass

class TransitionAppManagement(ScreenManager):
    pass

class ImageButton(ButtonBehavior, Image):
    pass

# Loading the Kivy file
kv = Builder.load_file("Transit.kv")

# Main class of this app
class TransitApp(App):
    def build(self):
        # Coloring the Background of the windows
        Window.clearcolor = (0.2, 0.6, 1, 1)
        return kv


# Running the application
if __name__ == '__main__':
    TransitApp().run()
