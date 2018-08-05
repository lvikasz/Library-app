# -*- coding: utf-8 -*-

import npyscreen
import os

from LoginPage import LoginPage
from InvalidPasswd import InvalidPasswdPage
from AdminMainPage import AdminMainPage
from AddUserPage import AddUserPage
from ShowUsersPage import ShowUsersPage
from EditUserPage import EditUserPage
from ShowBooksPage import ShowBooksPage
from InfoUserPage import InfoUserPage
from ShowUsersBooksPage import ShowUsersBooksPage
from BorrowBookPage import BorrowBookPage
from AddBookPage import AddBookPage
from SettingsPage import SettingsPage
from UserMainPage import UserMainPage
from ShowBooksUser import ShowBooksUser
from ShowBooksPageUser import ShowBooksPageUser
from SettingsUserPage import SettingsUserPage
from EditData import EditData

from Settings import Settings

from DataBase import DataBaseAccess
from Data import Data

#from Theme import Themer
from Theme import DefaultTheme
from Theme import BlueTheme
from Theme import WhiteTheme
from Theme import GreenTheme
from Theme import CyanTheme

from Theme import ManageTheme

# LoginValidate potrzebne>?
# dataBaseAccess co dalej
# Walidacja loginów

class Application(npyscreen.NPSAppManaged):
    def onStart(self):
        m = ManageTheme()
        m.manage()

        npyscreen.ASCII_ONLY = False

        self.addFormClass("MAIN", LoginPage)
        self.addFormClass("InvalidPasswd", InvalidPasswdPage)
        self.addFormClass("AdminMainPage", AdminMainPage)
        self.addFormClass("AddUserPage", AddUserPage)
        self.addFormClass("ShowUsersPage", ShowUsersPage)
        self.addFormClass("ShowUsersBooksPage", ShowUsersBooksPage)
        self.addFormClass("ShowBooksPage", ShowBooksPage)
        self.addFormClass("BorrowBookPage", BorrowBookPage)
        self.addFormClass("AddBookPage", AddBookPage)
        self.addFormClass("SettingsPage", SettingsPage)
        self.addFormClass("UserMainPage", UserMainPage)
        self.addFormClass("ShowBooksUser", ShowBooksUser)
        self.addFormClass("ShowBooksPageUser", ShowBooksPageUser)
        self.addFormClass("SettingsUserPage", SettingsUserPage)

        self.registerForm("EditData", EditData())
        self.registerForm("EditUserPage", EditUserPage())
        self.registerForm("InfoUserPage", InfoUserPage())

if __name__ == "__main__":
    os.system("title = Library app")
    os.system("mode con: cols=120 lines=40")
    app = Application()
    app.run()


