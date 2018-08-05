# -*- coding: utf=8 -*-
	
import npyscreen
from ShowBooksPage import ShowBooksPage

class ShowBooksPageUser(ShowBooksPage):
    def create(self):
        super(ShowBooksPageUser, self).create()
        self.__class__.CANCEL_BUTTON_TEXT = "Refresh"
        self.__class__.OK_BUTTON_TEXT = "Exit"
        self.text.hidden = True
        self.grid.rely -= 2
        self.search.rely -= 2

    def on_del(self, input):
        pass

    def del_book(self, input):
        pass

    def add_book(self, input):
        pass

    def on_ok(self):
        self.parentApp.switchForm("UserMainPage")

    def on_cancel(self):
        pass