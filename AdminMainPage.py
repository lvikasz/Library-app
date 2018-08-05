# -*- coding: utf=8 -*-

import npyscreen
#from Theme import Themer
import curses
from DataBase import DataBaseAccess

COLOR = 'CURSOR_INVERSE'

#zrob send mejl
#https://pl.wikipedia.org/wiki/International_Standard_Book_Number 10 lub 13 znaków

class AdminMainPage(npyscreen.ActionFormV2):
    def create(self):
        self.__class__.CANCEL_BUTTON_TEXT = "Refresh"
        self.__class__.OK_BUTTON_TEXT = "Exit"
        #self.ok_button.whenPressed = self.exit_application
        #self.ok_button.whenPressed = self.on_ok()
        #self.how_exited_handers[npyscreen.wgwidget.EXITED_ESCAPE]  = self.exit_application

        self.showUsersButton = self.add(npyscreen.ButtonPress, name = 'Users')
        self.showUsersButton.cursor_color = COLOR
        #self.debug_button.default_color = curses.COLOR_WHITE
        self.showUsersButton.whenPressed = self.on_show_pressed
		
        self.showBooksButton = self.add(npyscreen.ButtonPress, name = 'All books')
        self.showBooksButton.cursor_color = COLOR
        #self.debug_button.default_color = curses.COLOR_WHITE
        self.showBooksButton.whenPressed = self.on_books_pressed

        self.borrowBook = self.add(npyscreen.ButtonPress, name = 'Make action on book')
        self.borrowBook.cursor_color = COLOR
        self.borrowBook.whenPressed = self.on_borrow_book_pressed
		
        #self.showReturnButton = self.add(npyscreen.ButtonPress, name = 'Return books')
        #self.showReturnButton.cursor_color = COLOR
        #self.debug_button.default_color = curses.COLOR_WHITE
        #self.showReturnButton.whenPressed = self.on_Return_pressed
		
        self.showSettingsButton = self.add(npyscreen.ButtonPress, name = 'Settings')
        self.showSettingsButton.cursor_color = COLOR
		#self.debug_button.default_color = curses.COLOR_WHITE
        self.showSettingsButton.whenPressed = self.on_settings_pressed
					
        self.showLogoutButton = self.add(npyscreen.ButtonPress, name = 'Log out')
        self.showLogoutButton.cursor_color = COLOR
		#self.debug_button.default_color = curses.COLOR_WHITE
        self.showLogoutButton.whenPressed = self.on_logout_pressed
		
    
    def on_escape(self):
        self.set_editing(self.showLogoutButton)
        self.display()
        self.showLogoutButton.h_exit_down("")

    def on_show_pressed(self):
        self.parentApp.switchForm("ShowUsersPage")
		
    def on_logout_pressed(self):
	    self.parentApp.switchForm("MAIN")
	
    def on_borrow_book_pressed(self):
        self.parentApp.switchForm("BorrowBookPage")
		
    def on_settings_pressed(self):
	    self.parentApp.switchForm("SettingsPage")

    def on_books_pressed(self):
	    self.parentApp.switchForm("ShowBooksPage")
    
    def on_ok(self):
        if npyscreen.notify_yes_no(message = "Are you sure?", title = "?"):
            self.parentApp.switchForm(None)