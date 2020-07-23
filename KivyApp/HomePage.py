import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar
import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.graphics import Color, Rectangle
from kivy.uix.widget import Widget
from kivy.uix.camera import Camera
from kivy.uix.button import Button, ButtonBehavior
from kivy.uix.image import Image
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
import mysql.connector
from kivy.uix.checkbox import CheckBox
import time
global The_user


# Creating a database to keep the record of the UserInput
UserDataBase = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="password13",
    database="IndyRiderProfile"
)
mycursor = UserDataBase.cursor()
# This query will help us insert the username and the password into the database
InsetionFormula = "INSERT INTO riders (email, password) VALUE(%s,%s)"

# This query will help us while searching for the username and the corresponding password in our database
SearchFormula = "SELECT * FROM riders WHERE email = %s"

# Set window size
#   Pixel dimensions for a Samsung Galaxy S9 are 1440 x 2960,
#   scaled window by a factor of 0.25 to get 360 x 740
Window.size = (375, 667)


# Username (TestInput)
# Password (TestInput)
# Sign_in  (Button)
# Create_account (Button)
class HomeScreen(Screen):
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    sign_in = ObjectProperty(None)
    create_account = ObjectProperty(None)
    authentification_status = ObjectProperty(None)

    def signing_in(self):
        # here we want to verify the record in our database
        # if it exist, we take the user to his profile
        # if not we display an error message
        mycursor.execute(SearchFormula, (self.email.text,))
        user = mycursor.fetchone()
        if user is None:
            errorMessage= "An invalid username was specified"
            self.authentification_status.text = errorMessage
            return False
        else:
            if user[1] == self.password.text:
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
    email: ObjectProperty(None)
    password: ObjectProperty(None)
    confirmation: ObjectProperty(None)
    create: ObjectProperty(None)
    isFieldBlanked: ObjectProperty(None)

    def NewAccountCreation(self):
        # here we want to take the user credentials and save them into to our database
        # when the new account is created, we take them back to the login screen
        # if credentials are good, we show the user profile.
        if self.email.text != "" and self.password.text != "" and self.confirmation.text != "":
            if self.password.text == self.confirmation.text:
                NewUser = (self.email.text,self.password.text)
                mycursor.execute(InsetionFormula,NewUser)
                UserDataBase.commit()
                self.email.text = "Email"
                self.password.text = "Password"
                self.confirmation.text = "Confirm Password"
                return True
            else:
                self.isFieldBlanked.text = "Your last two entries do not match"
                return False
        else:
            self.isFieldBlanked.text = "Fill the blank field(s)"
            return False
    pass

class MainScreen(Screen):
    pass

class ProfileScreen(Screen):
    greetings: ObjectProperty(None)
    userPhoneNumber: ObjectProperty(None)
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


class SymptomsScreen(Screen):
    sym1 : ObjectProperty(None)
    sym2 : ObjectProperty(None)
    sym3 : ObjectProperty(None)
    sym4 : ObjectProperty(None)
    sym5 : ObjectProperty(None)
    sym6 : ObjectProperty(None)
    symptomsList = []

    def insert_data_into_db(self):
        if self.sym1.active:
            self.symptomsList.append('Fever')
        if self.sym2.active:
            self.symptomsList.append('Cough')
        if self.sym3.active:
            self.symptomsList.append('Sore Throat')
        if self.sym4.active:
            self.symptomsList.append('Soreness')
        if self.sym5.active:
            self.symptomsList.append('Shortness of breath')
        if self.sym6.active:
            self.symptomsList.append('Loss of smell and/or taste')

    pass

class SymptomsHistoryScreen(Screen):
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