# -*- coding: utf=8 -*-

import npyscreen
from DataBase import DataBaseAccess
from Data import Data

COLOR = 'CURSOR_INVERSE'

class UserMainPage(npyscreen.ActionForm):
    def create(self):
        self.db = DataBaseAccess()
        self.d = Data()

        self.__class__.CANCEL_BUTTON_TEXT = "Refresh"
        self.__class__.OK_BUTTON_TEXT = "Exit"

        self.myBooksButton = self.add(npyscreen.ButtonPress, name = "My books")
        self.myBooksButton.cursor_color = COLOR
        self.myBooksButton.whenPressed = self.on_my_books_pressed

        self.books = self.add(npyscreen.ButtonPress, name = "All books")
        self.books.cursor_color = COLOR
        self.books.whenPressed = self.on_books_pressed

        self.settings = self.add(npyscreen.ButtonPress, name = "Settings")
        self.settings.cursor_color = COLOR
        self.settings.whenPressed = self.on_settings_pressed

        self.editData = self.add(npyscreen.ButtonPress, name = "Edit my data")
        self.editData.cursor_color = COLOR
        self.editData.whenPressed = self.on_editData_pressed

        self.logout = self.add(npyscreen.ButtonPress, name = "Logout")
        self.logout.cursor_color = COLOR
        self.logout.whenPressed = self.on_logout_pressed

    def on_my_books_pressed(self):
        self.parentApp.switchForm("ShowBooksUser")

    def on_books_pressed(self):
        self.parentApp.switchForm("ShowBooksPageUser")

    def on_settings_pressed(self):
        self.parentApp.switchForm("SettingsUserPage")

    def on_editData_pressed(self):
        val = self.db.getUserId(self.d.__class__.ID)

        self.parentApp.getForm("EditData").pesel.value = val[0]
        self.parentApp.getForm("EditData").login.value = val[1]
        self.parentApp.getForm("EditData").passwd.value = val[2]
        self.parentApp.getForm("EditData").passwd2.value = val[2]
        self.parentApp.getForm("EditData").name.value = val[5]
        self.parentApp.getForm("EditData").surname.value = val[6]
        self.parentApp.getForm("EditData").mail.value = val[4]
        
        self.parentApp.switchForm("EditData")

    def on_logout_pressed(self):
        self.parentApp.switchForm("MAIN")

    def on_ok(self):
        if npyscreen.notify_yes_no(message = "Are you sure?", title = "?"):
            self.parentApp.switchForm(None)