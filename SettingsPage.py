# -*- coding: utf-8 -*-

import npyscreen
from Data import Data
from Settings import Settings
import curses

from Theme import ManageTheme

#from Theme import WhiteTheme

RELX = 30
RELY = 10


class SettingsPage(npyscreen.ActionForm):
    def create(self):
        self.__class__.OK_BUTTON_TEXT = "Save"
        self.__class__.CANCEL_BUTTON_TEXT = "Quit"

        self.s = Settings()
        self.d = Data()
        self.m = ManageTheme()
        
        th = self.s.getTheme()
        co = str(self.s.getCost())
        au = self.s.getAutoSave()
        d = open("dea.txt", "a")
        #d.write(au + '\n')
        if au == '0':
            au = False

        else:
            au = True    
        
        th = th[0].upper() + th[1:]
        
        self.vals = ["Default", "Blue", "White", "Green", "Cyan", "Black"]
        p = 0
        try:
            p = self.vals.index(th)
        
        except:
            p = 0
        
        self.theme = self.add(npyscreen.TitleSelectOne, name = "Theme", scroll_exit=True, value = p, values = self.vals, max_height=6, relx = RELX, rely = RELY)
        self.cost = self.add(npyscreen.TitleText, name = "Cost: ", value = co, relx = RELX, rely = RELY + 7)
        self.auto = self.add(npyscreen.Checkbox, name = "Autosave: ", relx = RELX, rely = RELY + 9)
        self.auto.value = au


    def on_ok(self):
        try:
            float(self.cost.value)

        except:
            self.cost.value = self.d.__class__.COST
        
        self.s.setCost(self.cost.value)
        self.s.setTheme(self.vals[self.theme.value[0]])
        self.s.setAutoSave(self.auto.value)
        self.s.save()
        self.m.manage()
        self.parentApp.switchForm("AdminMainPage")
    def on_cancel(self):
        self.parentApp.switchForm("AdminMainPage")