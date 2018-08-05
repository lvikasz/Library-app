# -*- coding: utf-8 -*-

from DataBase import DataBaseAccess

class LoginValidate():
    def __init__(self):
        self.db = DataBaseAccess()

    def validate(self, login, passwd):
        if not isinstance(login, str) or not isinstance(passwd, str):
            return (False), (False)
        
        return self.db.validUser(login, passwd)
