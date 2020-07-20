import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar
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
import mysql.connector
import time



# Creating a database to keep the record of the UserInput
UserDataBase = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="password13",
    database="users"
)
mycursor = UserDataBase.cursor()
# This query will help us insert the username and the password into the database
InsetionFormula = "INSERT INTO users (username, password, Recent_Transits) VALUE(%s,%s)"

# This query will help us while searching for the username and the corresponding password in our database
SearchFormula = "SELECT * FROM users WHERE username = %s"

# Set window size
#   Pixel dimensions for a Samsung Galaxy S9 are 1440 x 2960,
#   scaled window by a factor of 0.25 to get 360 x 740
Window.size = (375, 667)


# Username (TestInput)
# Password (TestInput)
# Sign_in  (Button)
# Create_account (Button)
class HomeScreen(Screen):
    username = ObjectProperty(None)
    password = ObjectProperty(None)
    sign_in = ObjectProperty(None)
    create_account = ObjectProperty(None)
    authentification_status = ObjectProperty(None)

    def signing_in(self):
        # here we want to verify the record in our database
        # if it exist, we take the user to his profile
        # if not we display an error message
        mycursor.execute(SearchFormula, (self.username.text,))
        user = mycursor.fetchone()
        if user is None:
            errorMessage= "An invalid username was specified"
            self.authentification_status.text = errorMessage
            return False
        else:
            if user[1] == self.password.text:
                print("Login Sucessful!")
                self.authentification_status.text = " "
                return True
            else:
                errorMessage = "An invalid password was specified"
                self.authentification_status.text = errorMessage
                return False
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

    def NewAccountCreation(self):
        # here we want to take the user credentials and save them into to our database
        # when the new account is created, we take them back to the login screen
        # if credentials are good, we show the user profile.
        if self.username.text != "" and self.password.text != "" and self.confirmation.text != "":
            if self.password.text == self.confirmation.text:
                NewUser = (self.username.text,self.password.text)
                mycursor.execute(InsetionFormula,NewUser)
                UserDataBase.commit()
                self.username.text = "Username"
                self.password.text = "Password"
                self.confirmation.text = "Confirm Password"
                return True
        else:
            print("Fill the blank field(s)")
            return False
    pass

class MainScreen(Screen):
    pass

class ProfileScreen(Screen):
    pass

class ScannerScreen(Screen):

    pass

class ImageButton(ButtonBehavior, Image):
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