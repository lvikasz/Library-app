# -*- coding: utf-8 -*-

import npyscreen
from LoginPage import LoginPage

class InvalidPasswdPage(LoginPage, npyscreen.Form):
    def create(self):
        super(InvalidPasswdPage, self).create()
        self.add(npyscreen.TitleText, name= "Invalid passwd or user", relx = self.RELX, rely = 11, editable = False, labelColor = 'CRITICAL')

    def on_ok(self):
        super(InvalidPasswdPage, self).on_ok()
        self.clear()
    
    def clear(self):
        self.loginInput.value = ""
        self.passwdInput.value = ""
