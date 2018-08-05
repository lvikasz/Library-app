# -*- coding: utf=8 -*-

import npyscreen
from IBookAction import IBookAction


RELX = 25
RELY = 13

class ReturnBookPage(IBookAction):
    def create(self):
        super(ReturnBookPage, self).create()
        self.note = self.add(npyscreen.TitleText, relx = RELX, rely = 10, name = "Boorow book", editable = False, labelColor = "CAUTION")

    def on_ok(self):
        pass
