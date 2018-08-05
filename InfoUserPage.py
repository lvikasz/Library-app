# -*- coding: utf-8 -*-

import npyscreen
from ActionUserPage import ActionUserPage

class InfoUserPage(ActionUserPage):
    def create(self):
        super(InfoUserPage, self).create()
        
        self.passwd.hidden = True
        self.passwd2.hidden = True
        self.commit.hidden = True
        
        self.pesel.editable = False
        self.name.editable = False
        self.login.editable = False
        self.surname.editable = False
        self.mail.editable = False
        self.admin.editable = False
        
        self.pesel.rely += 2
        self.name.rely += 2
        self.surname.rely += 2
        self.login.rely += 2
        self.mail.rely += 2
        self.admin.rely += 2
        
        #a = self.admin.value
        
        #f = open("JLB", "a")
        #f.write(str(a))
        #f.close()
        
        RELX = self.admin.relx
        RELY = self.admin.rely
        
        self.admin.name = ""
        self.admin.hidden = True
        self.admin = self.add(npyscreen.Checkbox, relx = RELX, rely = RELY - 2, name = "Admin? ", editable = False)
        
        #self.a                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      dmin.update()
        #self.admin.hidden = True
        
        #self.admin1 = self.add(npyscreen.Checkbox, relx = RELX, rely = RELY -2, name = "Admin?")
        #self.admin1.value = a
        self.mail.rely -= 4
