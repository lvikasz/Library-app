# -*- coding: utf=8 -*-

from ActionUserPage import ActionUserPage

class AddUserPage(ActionUserPage):
    def create(self):
        super(AddUserPage, self).create()
        self.commit.name = "Add"

    def makeAcction(self, pesel, login, passwd, admin, email, name, surname):
        self.db.addUser(pesel, login, passwd, admin, email, name, surname)

    def ok(self, pesel, login):
        return self.db.isUser(pesel, login)    