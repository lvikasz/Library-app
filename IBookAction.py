# -*- coding: utf=8 -*-

import npyscreen
from DataBase import DataBaseAccess
import datetime

RELX = 25
RELY = 13

class IBookAction(npyscreen.ActionForm):
    def create(self):
        self.db = DataBaseAccess()
        

        self.userID = self.add(npyscreen.TitleText, relx = RELX, rely = RELY, name = "PESEL: ")
        self.bookISBN = self.add(npyscreen.TitleText, relx = RELX, rely = RELY  + 2, name = "ISBN: ")
        
        self.commitButton = self.add(npyscreen.ButtonPress, relx = RELX - 1, rely = RELY + 4, name = "Borrow")
        self.commitButton.whenPressed = self.on_ok

    def on_cancel(self):
        self.parentApp.switchForm("AdminMainPage")

    def on_ok(self):
        self.ID = self.userID.value
        self.ISBN = self.bookISBN.value
        self.date = str(datetime.date.today())        