# -*- coding: utf-8 -*-

import npyscreen
from DataBase import DataBaseAccess
import time

RELX = 25
RELY = 3

class AddBookPage(npyscreen.ActionForm):
    def create(self):
        self.__class__.OK_BUTTON_TEXT = "Add"

        self.db = DataBaseAccess()

        self.ISBNF = self.add(npyscreen.TitleText, relx = RELX, rely = RELY, name = "Signature: ")
        self.titleF = self.add(npyscreen.TitleText, relx = RELX, rely = RELY + 2 , name = "Title: ")
        self.authorF = self.add(npyscreen.TitleText, relx = RELX, rely = RELY + 4, name = "Author: ")
        self.yearF = self.add(npyscreen.TitleText, relx = RELX, rely = RELY + 6, name = "Year: ")
        
        self.commit = self.add(npyscreen.ButtonPress, relx = RELX, rely = RELY + 8, name = "Add")
        self.commit.whenPressed = self.on_commit_pressed

    def on_commit_pressed(self):
        self.getVals()
        if self.valid():
            return

    def getVals(self):
        self.ISBN = self.ISBNF.value
        self.title = self.titleF.value
        self.author = self.authorF.value
        self.year = self.yearF.value

    def valid(self):
        
        if self.ISBN == "" or self.title == "" or self.author == "" or self.year == "":
            self.notify_error()
            return False

        try:
            int(self.year)
        except:
            self.notify_error()
            return False

        if self.db.add_book(self.ISBN, self.title, self.author, self.year):
            self.on_cancel()
            return

        self.notify_error()

    def notify_error(self):
        npyscreen.notify_confirm(message = "Cannot add book!", title = "Error")
        
    
    def on_cancel(self):
        self.parentApp.switchFormPrevious()

    def on_ok(self):
        self.on_commit_pressed()



