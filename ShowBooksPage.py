# -*- coding: utf=8 -*-
	
import npyscreen
#from DataBase import DataBaseAccess
from IShowBooksPage import IShowBooksPage 
	
class ShowBooksPage(IShowBooksPage):
    def create(self):
        self.text = self.add(npyscreen.TitleText, name = "CTR + A or a - add book; d - delete book", editable = False)
        super(ShowBooksPage, self).create()
        
        self.__class__.CANCEL_BUTTON_TEXT = "Refresh"
        self.__class__.OK_BUTTON_TEXT = "Exit"

        self.add_handlers({
            ord("a") : self.add_book,
            ord("A") : self.add_book,
            "^A" :     self.add_book,
        })
        
        self.grid.add_handlers({
            ord("a") : self.add_book,
            ord("A") : self.add_book,
            "^A" :     self.add_book,
            ord("d") : self.del_book,
            ord("D") : self.del_book,
        })

        #self.grid.rely -= 2
		
    def getData(self):
        return self.db.getAllBooksToDisplay()
	
    def on_search(self, input):
        self.grid.values = self.db.getBooksSearch(self.search.value)
        self.grid.update()

    def on_del(self, title):
        return npyscreen.notify_yes_no(message = ("Are you sure you want to delete %s?" % (title)))
		#npyscreen
		
    def del_book(self, input):
        idx = self.grid.edit_cell[0]
        if self.on_del(self.grid.values[idx][1]):
            if self.db.del_book(self.grid.values[idx][0]):
                self.on_search("")

            else:
                npyscreen.notify_confirm(message = "Cannot delete book!", title = "Error!")    
    
    def add_book(self, input):
        self.parentApp.switchForm("AddBookPage")
    
    def on_ok(self):
        self.parentApp.switchForm("AdminMainPage")