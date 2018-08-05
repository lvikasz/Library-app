# -*- coding: utf=8 -*-
	
import npyscreen
import curses
from DataBase import DataBaseAccess

RELY = 3

class IShowBooksPage(npyscreen.ActionForm):
    def create(self):
        self.__class__.OK_BUTTON_TEXT = "Refresh"
        self.__class__.CANCEL_BUTTON_BR_OFFSET = (2, 12)
        self.add_handlers({
            ord("s") : self.on_search,
            ord("S") : self.on_search,
        })

        self.db = DataBaseAccess()

        self.search = self.add(npyscreen.TitleText, name = "Search: ", labelColor = "STANDOUT")
        self.search.add_handlers({
            curses.KEY_ENTER : self.on_search,
            "^S" :             self.on_search, 
        })

        self.grid = self.add(npyscreen.GridColTitles, rely = RELY + 3, always_show_cursor = False, select_whole_line = True, exit_left = False, exit_right = False, col_titles = ['Signature', 'Title', 'Author', "Year"])
        self.grid.default_column_number = 4
		
        self.grid.add_handlers({
            ord("s") : self.grid.h_exit_up,
            ord("S") : self.grid.h_exit_up,
            "^S" :     self.on_search,
        })
		
        self.grid.values = self.getData()
		
	# fill init values
    def getData(self):
          pass
          #return self.db.getAllBooksToDisplay()

    # fill values after searching process 
    def on_search(self, input):
        pass  
		  