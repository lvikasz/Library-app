# -*- coding: utf=8 -*-
	
import npyscreen
from DataBase import DataBaseAccess
from Data import Data
from IShowBooksPage import IShowBooksPage

class ShowBooksUser(IShowBooksPage):

    def create(self):
        self.d = Data()
        super(ShowBooksUser, self).create()
        self.__class__.CANCEL_BUTTON_TEXT = "Refresh"
        self.__class__.OK_BUTTON_TEXT = "Exit"
        self.grid.rely -= 2
        
        #self.on_cancel()
    
    def getData(self):
        #f = open("ID.txt", "a")
        #f.write(self.d.__class__.ID + '\n')
        return self.db.getUsersBooksToDisplay(self.d.__class__.ID)

    def on_search(self, input):
        o = Data.ID
        vas = self.db.getUserBooksSearch(self.search.value, o[0])
        
        self.grid.values = vas
        self.grid.update()

    def on_ok(self):
        self.parentApp.switchForm("UserMainPage")
        
    def on_cancel(self):
        pass
        
