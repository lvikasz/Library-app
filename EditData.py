# -*- coding: utf=8 -*-

import npyscreen
from EditUserPage import EditUserPage

class EditData(EditUserPage, npyscreen.Form):
    def create(self):
        super(EditUserPage, self).create()
        self.admin.hidden = True
        self.commit.name = "Edit"
        self.commit.rely -= 4

    def on_cancel(self):
        self.parentApp.switchForm("UserMainPage")

    def on_ok(self):
        self.parentApp.switchForm("UserMainPage")

    def afterEditing(self):
        self.parentApp.switchForm("UserMainPage")