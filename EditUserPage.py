# -*- coding: utf=8 -*-

from ActionUserPage import ActionUserPage

class EditUserPage(ActionUserPage):
    def create(self):
        super(EditUserPage, self).create()
        self.pesel.editable = False
        self.commit.name = "Edit"

    def makeAcction(self, pesel, login, passwd, admin, email, name, surname):
        self.db.editUser(pesel, login, passwd, admin, email, name, surname)

    def ok(self, pesel, login):
        return self.db.isUserSecond(pesel, login)