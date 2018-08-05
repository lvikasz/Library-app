# -*- coding: utf-8 -*-

import npyscreen
import curses
import re
from DataBase import DataBaseAccess
from Data import Data 

RELY = 3

class ShowUsersPage(npyscreen.ActionForm):#, npyscreen.FormWithMenus):
    def create(self):
        self.__class__.CANCEL_BUTTON_TEXT = "Exit"
        self.__class__.OK_BUTTON_TEXT = "Refresh"
        self.__class__.CANCEL_BUTTON_BR_OFFSET = (2, 15)

        self.add_handlers({
            ord("s") : self.on_search,
            ord("S") : self.on_search,
            "^A" :     self.add_user,
        })

        self.add(npyscreen.TitleText, name= "CTR + A or a - add; e - edit;  d - delete; i - info; b - show books;CTR + S - search; m - send mail", editable = False)
	
        self.db = DataBaseAccess()
		
        self.search = self.add(npyscreen.TitleText, name = "Search: ", labelColor = "STANDOUT")
        self.search.add_handlers({
            curses.KEY_ENTER : self.on_search,
            "^S"             : self.on_search, 
        })
        
        
        self.grid = self.add(npyscreen.GridColTitles, rely = RELY + 3, slow_scroll = True, always_show_cursor = False, select_whole_line = True, col_titles = ['PESEL', 'Name', 'Surname'])
        self.grid.default_column_number = 3
		
        self.grid.add_handlers({
            ord("e") : self.edit_cell,
            ord("E") : self.edit_cell,
            ord("a") : self.add_user,
            ord("A") : self.add_user,
            ord("d") : self.del_user,
            ord("D") : self.del_user,
            ord("i") : self.info_user,
            ord("I") : self.info_user,
            ord("b") : self.books_user,
            ord("B") : self.books_user,
            ord("s") : self.grid.h_exit_up,
            ord("S") : self.grid.h_exit_up,
            "^S"     : self.on_search,
        })
        
        #self.grid.columns = 1
        #self.grid.rows = 10

        # Add menus
        #self.menu = self.add_menu(name = "Main menu", shortcut = "^M")
        #self.menu.addItemsFromList([
        #    ("Add user", self.add_user)
        #])


        self.getData()
        

    def on_cancel(self):
        self.parentApp.switchForm("AdminMainPage")

    def add_user(self, input):
        self.parentApp.switchForm("AddUserPage")

    def on_del(self, name, surname):
        return npyscreen.notify_yes_no(message = ("Are you sure you want to delete %s %s?" % (name, surname)))
		#npyscreen
		
    def del_user(self, input):
        if self.on_del(self.vals[self.grid.edit_cell[0]][5], self.vals[self.grid.edit_cell[0]][6]):
            self.db.delUser(self.vals[self.grid.edit_cell[0]][0])
            self.getData()

    def edit_cell(self, input):
        cell_edit = self.grid.edit_cell

        self.parentApp.getForm("EditUserPage").pesel.value = self.vals[cell_edit[0]][0]
        self.parentApp.getForm("EditUserPage").login.value = self.vals[cell_edit[0]][1]
        self.parentApp.getForm("EditUserPage").passwd.value = self.vals[cell_edit[0]][2]
        self.parentApp.getForm("EditUserPage").passwd2.value = self.vals[cell_edit[0]][2]
        self.parentApp.getForm("EditUserPage").name.value = self.vals[cell_edit[0]][5]
        self.parentApp.getForm("EditUserPage").surname.value = self.vals[cell_edit[0]][6]

        adm = False
        if self.vals[cell_edit[0]][3] == 'True' or self.vals[cell_edit[0]][3] == 1:
            adm = True
        self.parentApp.getForm("EditUserPage").admin.value = adm
        self.parentApp.getForm("EditUserPage").mail.value = self.vals[cell_edit[0]][4]

        #f = open("EDIT.txt", "a")
        #f.write(str(self.parentApp.getForm("AddUserPage").val) + '\n')
        self.parentApp.switchForm("EditUserPage")
    
    def info_user(self, input):
        cell_edit = self.grid.edit_cell
        
        self.parentApp.getForm("InfoUserPage").pesel.value = self.vals[cell_edit[0]][0]
        self.parentApp.getForm("InfoUserPage").login.value = self.vals[cell_edit[0]][1]
        #self.parentApp.getForm("InfoUserPage").passwd.value = self.vals[cell_edit[0]][2]
        #self.parentApp.getForm("InfoUserPage").passwd2.value = self.vals[cell_edit[0]][2]
        self.parentApp.getForm("InfoUserPage").name.value = self.vals[cell_edit[0]][5]
        self.parentApp.getForm("InfoUserPage").surname.value = self.vals[cell_edit[0]][6]

        adm = False
        if self.vals[cell_edit[0]][3] == 'True' or self.vals[cell_edit[0]][3] == 1:
            adm = True
        self.parentApp.getForm("InfoUserPage").admin.value = adm
        self.parentApp.getForm("InfoUserPage").mail.value = self.vals[cell_edit[0]][4]
    
        self.parentApp.switchForm("InfoUserPage")
    
    def books_user(self, input):
        Data.ID = self.vals[self.grid.edit_cell[0]][0]
        self.parentApp.switchForm("ShowUsersBooksPage")
    
    def parseData(self, vals):
        data = []
        for i in vals:
            a = [i[0], i[5], i[6]]
            data.append(a)

        return data    

    def getData(self):
        # I have to have self.vals because I use all info about user :/ 
        self.vals = self.db.getAllUsers()
        self.grid.values = self.parseData(self.vals)

    def on_search(self, input):
        self.vals = self.db.userSearch(self.search.value)
        self.grid.values = self.parseData(self.vals)
        self.grid.update()