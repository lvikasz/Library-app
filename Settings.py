# -*- coding: utf=8 -*-

from Data import Data
# cost :2.5
# theme :dark
# autosave :1
class Settings():
    def __init__(self):
        self.lines = [""]
        self.d = Data()
        self.fileName = "settings.txt"
        
        self.refresh()
        
    def update(self):
        self.d.__class__.COST = self.getCost()
        self.d.__class__.THEME = self.getTheme()

    def refresh(self):
        self.f = open(self.fileName, "r")
        self.lines = self.f.readlines()
        self.f.close()

        self.update()
        
    def save(self):
        self.f = open(self.fileName, "w")
        #self.f.writelines(self.lines)
        #self.f.write(str(self.lines))
        for i in self.lines:
            self.f.write(i + '\n')
        self.f.close()

        self.update()

    def getCost(self):
        for i in self.lines:
            if i[0:4] == "cost":
                a = i.split(':')
                return float(a[1].replace('\n', ''))
        return 2.5
    
    def setCost(self, cost):
        try:
            cost = str(cost)
        except:
            cost = self.d.__class__.COST
        
        it = 0
        for i in self.lines:
            if i[0:4] == "cost":
                self.lines[it] = self.lines[it][0:6] + cost
                break

            it += 1
        
        #self.save()
    
    def getTheme(self):
        for i in self.lines:
            if i[0:5] == "theme":
                a = i.split(':')
                return a[1].replace('\n', '').lower()

        return "default"        

    def setTheme(self, theme):
        theme = str(theme)
        it = 0

        for i in self.lines:
            if i[0:5] == "theme":
                self.lines[it] = self.lines[it][0:7] + theme
                break
            it += 1

        #self.save()

    def getAutoSave(self):
        for i in self.lines:
            if i[0:8] == "autosave":
                a = i.split(':')
                return a[1].replace('\n', '').lower()
        return '0'


    def setAutoSave(self, auto):
        try:
            if bool(auto):
                auto = '1'

            else:
                auto = '0'    
        except:
            auto = '0'

        it = 0
        for i in self.lines:
            if i[0:8] == "autosave":
                self.lines[it] = self.lines[it][0:10] + auto
                break
            it += 1
        #self.save() 