# -*- coding: utf-8 -*-

#import pymysql.cursors
import sqlite3
import re

# ISBN is "signature"... I changed my mind during programing ;/ 

class DataBaseAccess():
    def regexp(self, expr, item):
        reg = re.compile(expr)
        return reg.search(item) is not None    
    
    #sqlTable = {"getUser" : "SELECT * FROM users WHERE user == "}
    connection = sqlite3.connect("db.sql")
    def __init__(self):
        # adding my own function to sqlite3; I use it later 
        self.__class__.connection.create_function("REGEXP", 2, self.regexp)
        #connection = 
        #pass
    def connect(self):
        cur = self.__class__.connection.cursor()
        return cur

    def getAllUsers(self):
        sql = "SELECT * FROM users"
        a = None

        try:
            cur = self.connect()
            cur.execute(sql)
            a = cur.fetchall()
            
            return a
        except:
            f = open("DBG.txt", "a")
            f.write("JEVAC\n")
            return []

    def validUser(self, login, passwd):
        #f = open("debug.txt", "a")
        
        try:
            sql = "SELECT * FROM users WHERE login = '%s' AND passwd = '%s'" % (login, passwd)
            
            cur = self.connect()

            cur.execute(sql)

            a = cur.fetchall()

            admin = False
            if a[0][3] == 'True' or a[0][3] == 1:
                admin = True
            
            if len(a) != 0:
                self.__class__.connection.commit()
                return (True), (admin)

            else:
                self.__class__.connection.commit()
                return (False), (False)

        except:
            #sf.write("nie\n")
            return (False), (False)

    def isUser(self, ID, login):
        # get all users 
        getAllSQL = "SELECT login, pesel FROM users"
        cur = self.connect()

        cur.execute(getAllSQL)
        allUsers = cur.fetchall()
        self.__class__.connection.commit()
        #f = open("users.txt", "a")
        #f.write(str(allUsers))

        for i in allUsers:
            if i[0] == login or i[1] == ID:
                return False
        return True

    def isUserSecond(self, ID, login):
        # get all users 
        getAllSQL = "SELECT login, pesel FROM users"
        cur = self.connect()

        cur.execute(getAllSQL)
        allUsers = cur.fetchall()
        self.__class__.connection.commit()
        
        counter = 0

        for i in allUsers:
            
            if i[1] != ID and i[0] == login:
                counter +=1

        
        if counter >= 1:
            return False

        return True

    def addUser(self, ID, login, passwd, admin, email, name, surname):
        #f = open("db.txt", "a")
        sql = "INSERT INTO users (pesel, login, passwd, admin, mail, name, surname) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s')" % (ID, login, passwd, admin, email, name, surname)
        cur = self.connect()

        #f.write("connected!\n")
        cur.execute(sql)
        #f.write("exe!\n")
        self.__class__.connection.commit()

    def editUser(self, ID, login, passwd, admin, email, name, surname):
        sql = "UPDATE users SET pesel = '%s',login = '%s',passwd = '%s',admin = '%s',mail = '%s', name = '%s', surname = '%s' WHERE pesel = '%s'" % (ID, login, passwd, admin, email, name, surname, ID)  
        cur = self.connect()

        cur.execute(sql)
        
        self.__class__.connection.commit()


    def delUser(self, ID):
        sql = "DELETE FROM users WHERE pesel = '%s'" % ID

        cur = self.connect()

        cur.execute(sql)
        self.__class__.connection.commit()

	
    def getAllBooksToDisplay(self):
        sql = "SELECT DISTINCT ISBN, title, author, year FROM books"
        cur = self.connect()
		
        cur.execute(sql)
		
        ret = cur.fetchall()
        self.__class__.connection.commit()
		
        return ret
        
    def getUsersBooksToDisplay(self, ID):
        #f = open("kk.txt", "a")
        #f.write(ID)
        # SELECT DISTINCT ???
        sql = "SELECT ISBN, title, author, year FROM books WHERE user = '%s'" % ID
        cur = self.connect()
        
        cur.execute(sql)
        
        ret = cur.fetchall()
        #f.write("\n")
        #f.write(str(ret))
        #f.close()
        self.__class__.connection.commit()
		
        return ret
     
    def returnBook(self, ID, ISBN):
        cur = self.connect()
        ret = []

        sql = "SELECT date FROM books where ISBN = '%s'" % ISBN
        try:
            cur.execute(sql)
            ret = cur.fetchall()

            sql = "UPDATE books SET user = '', date = '' WHERE ISBN = '%s' AND user = '%s';" % (ISBN, ID)
            cur.execute(sql)
        
        #ret = cur.fetchall()
        
            self.__class__.connection.commit()

        except:
            return False

        return ret    

    def getAllBooks(self):
        sql = "SELECT ISBN, title, author, year, user, date FROM books"

        ret = []

        cur = self.connect()
        cur.execute(sql)

        ret = cur.fetchall()
        return ret

    def validBook(self, ISBN):
        books = self.getAllBooks()

        for i in books:
            if i[4] == '' and i[0] == ISBN:
                return True

        return False

    def borrowBook(self, ID, ISBN, date):
        #f = open("date.txt", "a")
        #f.write(date)
        #date = "12-12-12"
        sql = "UPDATE books SET user = '%s', date = '%s' WHERE ISBN = '%s' AND user = '';" % (ID, date, ISBN)

        if not self.validBook(ISBN):
            return False
        
        #f.write(ID + " " + ISBN + " " + date)
        #f.write(sql + '\n')

        cur = self.connect()
        try:
            cur.execute(sql)
            #ret = cur.fetchall()
        
            self.__class__.connection.commit()
            return True
        except:
            pass
            #return False  

    def userSearch(self, part):
        sql = "SELECT * FROM users WHERE pesel REGEXP '%s/*' OR name REGEXP '%s/*' OR surname REGEXP '%s/*'" % (part, part, part)
   
        ret = []

        cur = self.connect()

        try:
            cur.execute(sql)
            ret = cur.fetchall()
        
            return ret

        except:
            f = open("Errors.txt", "a")
            f.write("Gówno")
            return []

    def getUsersBooksToDisplaySearch(self, part, ID):
        sql = "SELECT DISTINCT ISBN, title, author, year FROM books WHERE (ISBN REGEXP '%s/*' OR title REGEXP '%s/*' OR author REGEXP '%s/*' OR year REGEXP '%s/*') AND user = '%s'" % (part, part, part, part, ID)        

        ret = []
        cur = self.connect()

        try:
            cur.execute(sql)
            ret = cur.fetchall()

            return ret

        except:
            return []

    def getBooksSearch(self, part):
        sql = "SELECT DISTINCT * FROM books WHERE (ISBN REGEXP '%s/*' OR title REGEXP '%s/*' OR author REGEXP '%s/*' OR year REGEXP '%s/*')" % (part, part, part, part)

        ret = []
        cur = self.connect()

        try:
            cur.execute(sql)
            ret = cur.fetchall()

            return ret

        except:
            return []

    def del_book(self, ISBN):
        cur = self.connect()

        sql = "SELECT * FROM books WHERE ISBN = '%s' AND user = ''" % ISBN
        cur.execute(sql)
        if len(cur.fetchall()) == 0:
            return False
        
        sql = "DELETE FROM books WHERE ISBN = '%s' AND user = ''" % ISBN

        try:
            cur.execute(sql)
            self.__class__.connection.commit()

            return True
        except:
            return False

    def add_book(self, ISBN, title, author, year):
        sql = "INSERT INTO books (ISBN, title, author, year, user, date) VALUES ('%s', '%s', '%s', '%s', '', '');" % (ISBN, title, author, year)
        f = open("query.txt", "a")
        f.write(sql+ '\n')
        cur = self.connect()

        try:
            cur.execute(sql)
            self.__class__.connection.commit()
            return True
        except:
            return False

    def get_free_books(self):
        sql = "SELECT ISBN, title, year, author FROM books WHERE user = ''"

        cur = self.connect()
        ret = []

        try:
            cur.execute(sql)
            ret = cur.fetchall()

            return ret

        except:
            return ret    
    def getUserBooksSearch(self, part, ID):
        sql = "SELECT ISBN, title, author, year FROM books WHERE (ISBN REGEXP '%s/*' OR title REGEXP '%s/*' OR author REGEXP '%s/*' OR year REGEXP '%s/*') AND user = '%s'" % (part, part, part, part, ID)

        ret = []
        cur = self.connect()

        try:
            cur.execute(sql)
            ret = cur.fetchall()
            
            return ret

        except:
           return []

    def getUserLogin(self, login):
        sql = "SELECT pesel FROM users WHERE login = '%s'" % login

        ret = 0
        cur = self.connect()
        try:
            cur.execute(sql)
            ret = cur.fetchall()[0]

            return ret

        except:
            return 0    
    
    def getUserId(self, ID):
        sql = "SELECT * FROM users WHERE pesel = '%s'" % ID

        cur = self.connect()

        try:
            cur.execute(sql)
            ret = cur.fetchall()

            return ret[0]
        except:
            return []