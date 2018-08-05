import npyscreen
import curses

from Settings import Settings
from Data import Data

_colors_to_define = (
('BLACK_WHITE', curses.COLOR_BLACK, curses.COLOR_WHITE),
('BLUE_BLACK', curses.COLOR_BLUE,curses.COLOR_BLACK),
('CYAN_BLACK', curses.COLOR_CYAN, curses.COLOR_BLACK),
('GREEN_BLACK', curses.COLOR_GREEN, curses.COLOR_BLACK),
('RED_BLACK', curses.COLOR_RED, curses.COLOR_BLACK),
('BLACK_RED', curses.COLOR_BLACK, curses.COLOR_RED),
('BLACK_GREEN', curses.COLOR_BLACK, curses.COLOR_GREEN),
('BLACK_YELLOW', curses.COLOR_BLACK, curses.COLOR_YELLOW),
('BLUE_WHITE', curses.COLOR_BLUE, curses.COLOR_WHITE),
('GREEN_WHITE', curses.COLOR_GREEN, curses.COLOR_WHITE),
('YELLOW_WHITE', curses.COLOR_YELLOW, curses.COLOR_WHITE),
('RED_WHITE', curses.COLOR_RED, curses.COLOR_WHITE),)

class DefaultTheme(npyscreen.ThemeManager):
    default_colors = {
    'DEFAULT'     : 'WHITE_BLACK',
    'FORMDEFAULT' : 'WHITE_BLACK',
    'NO_EDIT'     : 'BLUE_BLACK',
    'STANDOUT'    : 'CYAN_BLACK',
    'CURSOR'      : 'WHITE_BLACK',
    'CURSOR_INVERSE': 'BLACK_WHITE',
    'LABEL'       : 'GREEN_BLACK',
    'LABELBOLD'   : 'WHITE_BLACK',
    'CONTROL'     : 'WHITE_BLACK',
    'IMPORTANT'   : 'GREEN_BLACK',
    'SAFE'        : 'GREEN_BLACK',
    'WARNING'     : 'YELLOW_BLACK',
    'DANGER'      : 'RED_BLACK',
    'CRITICAL'    : 'BLACK_RED',
    'GOOD'        : 'GREEN_BLACK',
    'GOODHL'      : 'GREEN_BLACK',
    'VERYGOOD'    : 'BLACK_GREEN',
    'CAUTION'     : 'YELLOW_BLACK',
    'CAUTIONHL'   : 'BLACK_YELLOW',
    }

class BlueTheme(npyscreen.ThemeManager):
    # CURSOR_INVERSE
    # DEFAULT
    # CRITICAL
    default_colors = {
        'DEFAULT' : 'WHITE_BLACK',
        'CURSOR_INVERSE' : 'BLACK_GREEN',
        'CRITICAL' : 'BLACK_GREEN',
        'LABEL' : 'BLUE_BLACK',
        'STANDOUT' : 'GREEN_BLACK',
        'FORMDEFAULT' : 'BLUE_BLACK'
    }

class WhiteTheme(npyscreen.ThemeManager):
    default_colors = {
        'DEFAULT' : 'BLACK_WHITE',
        'CURSOR_INVERSE' : 'GREEN_WHITE',
        'CRITICAL' : 'RED_WHITE',
        'LABEL' : 'BLUE_WHITE',
        'STANDOUT' : 'GREEN_WHITE',#
        'FORMDEFAULT' : 'BLACK_WHITE'
    }

class GreenTheme(npyscreen.ThemeManager):
    default_colors = {
        'DEFAULT' : 'GREEN_BLACK',
        'CURSOR_INVERSE' : 'BLACK_GREEN',
        'CRITICAL' : 'RED_WHITE',
        'LABEL' : 'BLUE_BLACK',
        'STANDOUT' : 'BLUE_BLACK',
        'FORMDEFAULT' : 'GREEN_BLACK'
    }

class CyanTheme(npyscreen.ThemeManager):
    default_colors = {
        'DEFAULT' : 'CYAN_BLACK',
        'CURSOR_INVERSE' : 'BLACK_CYAN',
        'CRITICAL' : 'RED_BLACK',
        'LABEL' : 'CYAN_BLACK',
        'STANDOUT' : 'CYAN_BLACK',
        'FORMDEFAULT' : 'CYAN_BLACK',
        'CURSOR' : 'CYAN_BLACK',
        #'CONTROL' : 'BLACK_CYAN'
    }

class DarkTheme(DefaultTheme):
    pass

class ManageTheme():
    def manage(self):
        s = Settings()

        d = Data()
        theme = d.__class__.THEME
        
        if theme == "default":
            npyscreen.setTheme(DefaultTheme)

        elif theme == "blue":
            npyscreen.setTheme(BlueTheme)

        elif theme == "white":
            npyscreen.setTheme(WhiteTheme)

        elif theme == "green":
            npyscreen.setTheme(GreenTheme)

        elif theme == "cyan":
            npyscreen.setTheme(CyanTheme)   

        elif theme == "black":
            npyscreen.setTheme(DefaultTheme)   

        else:
            npyscreen.setTheme(DefaultTheme)          
