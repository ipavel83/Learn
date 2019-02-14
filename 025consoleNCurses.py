#!/usr/bin/env python
#https://docs.python.org/3/howto/curses.html
#https://docs.python.org/2/library/curses.html

import curses #python -m pip install windows-curses
#import curses.textpad
#import time

stdscr = curses.initscr()
#curses.noecho() #To turn off mirroring pressed keys
#curses.echo()

GRAY_BASE = 15 #15 is max color without error
GRAY_pair = 50
RED_pair = 40

curses.start_color()
stdscr.addstr("Type q to exit ", curses.color_pair(1)) #by default all color pares are default 
stdscr.addstr("Type p to print string, and c to print char ", curses.color_pair(1)) #by default all color pares are default 
stdscr.addstr("Type s to supress display pressed buttons", curses.color_pair(1)) #by default all color pares are default 


curses.init_color( GRAY_BASE, 500, 500, 500 ) #color (0-15), R,G,B (0-1000)
curses.init_pair(  GRAY_pair, GRAY_BASE, curses.COLOR_BLACK )
stdscr.addstr(2,0, "RED ALERT!", curses.color_pair(GRAY_pair))

curses.init_pair(  RED_pair, GRAY_BASE, curses.COLOR_RED )
stdscr.addstr(3,0, "RED ALERT! 2", curses.color_pair(RED_pair))

curses.curs_set(0) #make cursor invisible

#Applications will also commonly need to react to keys instantly, without requiring the Enter key to be pressed;
# this is called cbreak mode, as opposed to the usual buffered input mode.
#curses.cbreak()

#begin_x = 20
#begin_y = 7
#height = 5
#width = 40
#win = curses.newwin(height, width, begin_y, begin_x)
#tb = curses.textpad.Textbox(win)
#text = tb.edit()
stdscr.addstr(8,1,'initial')#text.encode('utf_8')

#hw = "Hello world!"

wHeight= 8
wWidth =40
begY = 4
begX = 20
win = curses.newpad(wHeight*10, wWidth) #newwin is fixed and gives err if text is bigger than window

i = 0
while 1:
    c = stdscr.getch()
    if c == ord('o'):
        win.addstr(f'{i}some Str ')
        
        win.refresh(i //20, 0, begY, begX, begY+wHeight, begX+wWidth) #[PadStartRow, PadStartCol, DispStartRow, DispStartcol, DispEndRow, DispEndCol]
        #if window is not a pad, just windowwin.refresh()
        i+=1
    elif c == ord('c'):
        win.clear()
        i=0
        win.refresh(i //20, 0, begY, begX, begY+wHeight, begX+wWidth)
    elif c == ord('s'):
        stdscr.addch(1,20,curses.ACS_HLINE)
        stdscr.addch(2,20,curses.ACS_PLUS)
        stdscr.addch(3,20,curses.ACS_LRCORNER)
        stdscr.addch(4,20,curses.ACS_DARROW)
        
        stdscr.addch(5,20,curses.ACS_LARROW)
        stdscr.addch(5,21,curses.ACS_LRCORNER)
    elif c == ord('p'):
        stdscr.addstr(10 +(i*2), 30, 'hel_\u21B2_lo')
        stdscr.addstr(10 +(i*2), 40, 'При\nвет')
        i+=1
    elif c == ord('c'):
        stdscr.addch('H')
    elif c == ord('s'):
        curses.noecho()
    elif c == ord('q'): break # Exit the while()
    elif c == curses.KEY_HOME: x = y = 0

curses.endwin()

