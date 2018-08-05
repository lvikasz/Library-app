# -*- coding: utf=8 -*-
	
import npyscreen
#from DataBase import DataBaseAccess
from Data import Data 
from IShowBooksPage import IShowBooksPage 

class ShowUsersBooksPage(IShowBooksPage):
    def create(self):
         self.text = self.add(npyscreen.TitleText, name = "R - oddaj ksiazke ", editable = False)
         super(ShowUsersBooksPage, self).create()
         self.__class__.CANCEL_BUTTON_TEXT = "Refresh"
         self.__class__.OK_BUTTON_TEXT = "Exit"
         self.grid.add_handlers({ord('r') : self.on_rec,
                                 ord('R') : self.on_rec,})
		
    def getData(self):
        o = Data.ID
        #f = open("dbg.txt", "a")
        #f.write(o + '\n')
        #f.write(Data.ID + '\n')
        
        return self.db.getUsersBooksToDisplay(o)    
        
    def on_search(self, input):
        o = Data.ID
        self.grid.values = self.db.getUsersBooksToDisplaySearch(self.search.value, o)
        self.grid.update()

    def on_rec(self, input):
        cell_edit = self.grid.edit_cell[0]
        self.db.returnBook(Data.ID, self.grid.values[cell_edit][0])
        self.grid.values = self.getData()
        #super(ShowUsersBooksPage, self).grid.update()
    
    def on_ok(self):
        self.parentApp.switchForm("ShowUsersPage")

    def on_cancel(self):
        pass
          