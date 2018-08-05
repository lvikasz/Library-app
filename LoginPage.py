# -*- coding: utf=8 -*-

import npyscreen
from LoginValidate import LoginValidate
from Data import Data
from DataBase import DataBaseAccess

#acionForm?
class LoginPage(npyscreen.ActionForm):
    def create(self):
        self.db = DataBaseAccess()

        self.__class__.OK_BUTTON_TEXT = "Exit"
        self.__class__.CANCEL_BUTTON_TEXT = "Login"
        self.__class__.CANCEL_BUTTON_BR_OFFSET = (2,13)
        self.RELX = 50
        self.login = LoginValidate()
        # creating login page's layout
        self.loginInput = self.add(npyscreen.TitleText, relx = self.RELX, rely = 13, name = "Login: ")
        self.passwdInput = self.add(npyscreen.TitlePassword, relx = self.RELX, rely = 15, name = "Password: ")
    
    def on_ok(self):
        self.parentApp.switchForm(None)
    
    def on_cancel(self):
        allow, mode = self.login.validate(self.loginInput.value, self.passwdInput.value)
        if allow:
            if mode:
                self.parentApp.setNextForm("AdminMainPage")
            
            else:
                d = Data()
                d.__class__.ID = self.db.getUserLogin(self.loginInput.value)
                self.parentApp.setNextForm("UserMainPage")

        else:
            self.parentApp.setNextForm("InvalidPasswd")
        
            