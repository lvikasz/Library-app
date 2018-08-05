# -*- coding: utf=8 -*-

import npyscreen
from DataBase import DataBaseAccess

import time

RELX = 20
RELY = 2

class ActionUserPage(npyscreen.Form):
    #def __init__(self, *args, **keywords)
    
    def create(self):
        self.__class__.OK_BUTTON_TEXT = "Exit"
        self.db = DataBaseAccess()
        
        self.pesel = self.add(npyscreen.TitleText, relx = RELX, rely = RELY, name = "PESEL")
        self.name = self.add(npyscreen.TitleText, relx = RELX, rely= RELY + 2, name = "Name: ")
        self.surname = self.add(npyscreen.TitleText, relx = RELX, rely= RELY + 4, name = "Surname: ")
        self.login = self.add(npyscreen.TitleText, relx = RELX, rely = RELY + 6, name = "Login")
        self.passwd = self.add(npyscreen.TitlePassword, relx = RELX, rely = RELY + 8, name = "Passwd")
        self.passwd2 = self.add(npyscreen.TitlePassword, relx = RELX, rely = RELY + 10, name = "Passwd again")
        self.mail = self.add(npyscreen.TitleText, relx = RELX, rely = RELY + 12, name = "Email: ")
        self.admin = self.add(npyscreen.Checkbox, relx = RELX, rely = RELY + 14, name = "Admin?")

        self.commit = self.add(npyscreen.ButtonPress, relx = RELX, rely = RELY + 18)
        self.commit.cursor_color = 'CURSOR_INVERSE'
        self.commit.whenPressed = self.on_commit_pressed
        
    def on_cancel(self):
        self.clear()
        self.parentApp.switchFormPrevious()

    def on_ok(self):
        self.parentApp.switchForm("ShowUsersPage")

    def afterEditing(self):
        self.parentApp.switchForm("ShowUsersPage")

    def PopUpAlertPrint(self, message):
        npyscreen.notify_confirm(message, "Cannot add user!")
    
    def makeAcction(self, pesel, login, passwd, admin, email, name, surname):
        pass
    
    def ok(self, pesel, login):
        pass

    def on_commit_pressed(self):
        pesel = self.pesel.value
        login = self.login.value
        passwd = self.passwd.value
        passwd2 = self.passwd2.value
        email = self.mail.value
        admin = self.admin.value
        name = self.name.value
        surname = self.surname.value

        if admin == "":
            admin = "0"

        if pesel == "" or login == "" or passwd == "" or passwd2 == "" or admin == "" or name == '' or surname == '':
            self.PopUpAlertPrint("Please fill all fields!")
            return 

        if passwd != passwd2:
            self.PopUpAlertPrint("Passwd diffrent")
            return 

        if len(pesel) != 11:
            self.PopUpAlertPrint("Pesel invalid")
            return

        if email == "":
            self.PopUpAlertPrint("Fill email!")
            return

        allOk = self.ok(pesel, login)
        if allOk:
            self.makeAcction(pesel, login, passwd, admin, email, name, surname)
            self.on_ok()

        else:
            self.PopUpAlertPrint("Invalid login or pesel")  

    def clear(self):
        self.pesel.value = ""
        self.login.value = ""
        self.passwd.value = ""
        self.passwd2.value = "" 
        self.admin.value = ""
        self.name.value = ""
        self.surname.value = ""