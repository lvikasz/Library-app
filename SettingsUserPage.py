# -*- coding: utf=8 -*-
	
import npyscreen
from SettingsPage import SettingsPage

class SettingsUserPage(SettingsPage):
    def create(self):
        self.__class__.OK_BUTTON_TEXT = "Save"
        self.__class__.CANCEL_BUTTON_TEXT = "Quit"

        super(SettingsUserPage, self).create()
        self.cost.hidden = True
        self.auto.hidden = True
    
    def on_ok(self):
        self.s.setTheme(self.vals[self.theme.value[0]])
        self.s.save()
        self.m.manage()
        self.parentApp.switchForm("UserMainPage")

    def on_cancel(self):
        self.parentApp.switchForm("UserMainPage")   