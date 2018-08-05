# -*- coding: utf=8 -*-

import npyscreen
import curses
import datetime
from Data import Data

from DataBase import DataBaseAccess

class BorrowBookPage(npyscreen.ActionForm, npyscreen.SplitForm):
    def create(self):
        self.add(npyscreen.TitleText, name = "ctr + h - pomoc", editable = False)
        #self.add(npyscreen.TitleText, name = "ctr + s - wyszukaj, s - przejdz do szukania", editable = False)
        self.__class__.OK_BUTTON_TEXT = "Exit"
        self.__class__.CANCEL_BUTTON_TEXT = "Confirm"
        d  = Data()
        self.cost = d.COST
        # some common stuff
        self.db = DataBaseAccess()
        self.RELY = self.get_half_way()
        
        # first part
        self.searchUser = self.search = self.add(npyscreen.TitleText, name = "Search: ", labelColor = "STANDOUT")
        self.gridUser = self.add(npyscreen.GridColTitles, rely = 6, slow_scroll = True, always_show_cursor = True, max_height = self.get_half_way() - 6, select_whole_line = True, col_titles = ['PESEL', 'Name', 'Surname'])
        self.gridUser.default_column_number = 3

        # second part 
        self.searchBook = self.add(npyscreen.TitleText, rely = self.RELY + 1, name = "Search: ", labelColor = "STANDOUT")
        self.gridBook = self.add(npyscreen.GridColTitles, rely = self.RELY + 3, slow_scroll = True, always_show_cursor = True, select_whole_line = True, exit_left = False, col_titles = ['Signature', 'Title', 'Author', "Year"])
        self.gridBook.default_column_number = 4

        # handlers 
        self.add_handlers({
            "^B" : self.borrow_book,
            "^R" : self.recive_book,
            "^Z" : self.on_back,
            "^H" : self.show_help,
        })

        self.gridUser.add_handlers({
            ord("s")         : self.gridUser.h_exit_up,
            ord("S")         : self.gridUser.h_exit_up,
            ord("b")         : self.on_enterUserBorrow,
            ord("B")         : self.on_enterUserBorrow,
            ord("r")         : self.on_enterUserRecive,
            ord("R")         : self.on_enterUserRecive,
            "^S"             : self.on_searchUser,
        })

        self.gridBook.add_handlers({
            ord("s") : self.gridBook.h_exit_up,
            ord("S") : self.gridBook.h_exit_up,
            ord("b") : self.borrow_book,
            ord("B") : self.borrow_book,
            ord("r") : self.recive_book,
            ord("R") : self.recive_book,
            "^S"     : self.on_searchBook,
            "^B"     : self.borrow_book,
        })

        self.searchUser.add_handlers({
            curses.KEY_ENTER : self.on_searchUser,
            "^S"             : self.on_searchUser,
            "^H"             : self.show_help, 
        })

        self.searchBook.add_handlers({
            curses.KEY_ENTER : self.on_searchBook,
            "^S"             : self.on_searchBook,
            "^H"             : self.show_help,
        })

        self.setDefaultData()
        self.gridBook.editable = False


    # init values     
    def setDefaultData(self): 
        self.gridBook.values = self.db.getBooksSearch("")
        self.gridUser.values = self.parseData(self.db.getAllUsers())
        self.gridBook.editable = False

    def setInitPos(self):
        self.gridBook.edit_cell = [0, 0]
        self.gridUser.update()

        self.gridUser.edit_cell = [0, 0]
        self.gridUser.update()
        

        # I know that it is stupid...
        self.gridBook.h_exit_up("")
        self.searchBook.h_exit_up("")                
        self.set_editing(self.gridUser)
        self.display()
        self.gridUser.h_exit_up("")

    def parseData(self, vals):
        data = []
        for i in vals:
            a = [i[0], i[5], i[6]]
            data.append(a)

        return data

    def on_cancel(self):
        self.setDefaultData()
        self.setInitPos()
        self.searchUser.value = ""
        self.searchBook.value = ""

    def on_ok(self):
        self.parentApp.switchForm("AdminMainPage")

    def get_half_way(self):
        return 19

    def on_searchUser(self, input) :
        self.gridUser.values = self.parseData(self.db.userSearch(self.searchUser.value))
        self.gridUser.update()
        
        #self.searchUser.h_exit_down("")
        #self.searchUser.update()
        #self.set_editing(self.gridUser)
        #self.display()
        
        #self.searchUser.editale = True
        #self.gridUser.h_exit_down("")
        #self.searchUser.h_exit_down("")
        #self.gridUser.h_exit_down("")
        
    def on_searchBook(self, input):
        self.cell = self.gridUser.values[0]

        self.gridBook.values = self.db.getUserBooksSearch(self.searchBook.value, self.cell[0])
        self.gridBook.update()

    def on_enterUserRecive(self, input):
        self.cell = self.gridUser.values[self.gridUser.edit_cell[0]]

        self.gridUser.values = [self.cell]
        self.gridBook.values = self.db.getUsersBooksToDisplay(self.cell[0])
        
        self.gridUser.update()
        self.gridBook.update()

        self.gridUser.h_exit_down("")
        self.gridBook.editable = True

    def on_enterUserBorrow(self, input):
        # wybiera uzytkownika i potem przechodzi do ksiaze
        self.cell = self.gridUser.values[self.gridUser.edit_cell[0]]
        self.gridUser.h_exit_down("")

        self.gridBook.values = self.db.get_free_books()
        self.gridBook.editable = True

    def borrow_book(self, input):
        self.book = self.gridBook.values[self.gridBook.edit_cell[0]]
        if not self.db.borrowBook(self.cell[0], self.book[0], str(datetime.date.today())):
            npyscreen.notify_confirm(message = "Cannot borrow book!", title = "Error!")
            return 
        
        self.setDefaultData()
        self.setInitPos()

        npyscreen.notify_confirm(message = "Success!", title = "Message")

    def recive_book(self, input):
        ISBN = self.gridBook.values[self.gridBook.edit_cell[0]][0]
        data = self.db.returnBook(self.gridUser.values[0][0], ISBN)
        
        data = datetime.datetime.strptime(data[0][0].replace("-", ""), "%Y%m%d").date()
        td = datetime.date.today() - data
        open("DATA.txt", "a").write(str(td.days))
        if (td.days - 31) > 0:
            npyscreen.notify_confirm(message = "Musisz zaplacic %f" % ((float(td.days) - 31.0) * self.cost), title = "Timeout")
        else:
            npyscreen.notify_confirm(message = "Success", title = "Success")

        self.setDefaultData()
        self.setInitPos() 

    def on_back(self, input):
        self.on_cancel()

    def show_help(self, input):
        npyscreen.notify_confirm(title =  "Help", message = "r - wybierz uzytkownika do oddania, \nb - wybierz uzytkownika do wypozyczenia, \nctr + r - oddaj, \nctr + b - wypozycz\nctr + s - szukaj\ns - przejdz do szukania")

