"""
User input and text box
===========================
Capturing user input and displaying text box

Note: Press `ctrl + G` to exit out of text box
"""

import curses
from curses import wrapper
from curses.textpad import Textbox, rectangle
import time


def main(stdscr):
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_YELLOW)  # (id or pair no, foreground color, background color)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_RED, curses.COLOR_WHITE)
    _blue_and_yellow = curses.color_pair(1)
    _green_and_black = curses.color_pair(2)
    _red_and_white = curses.color_pair(3)

    win = curses.newwin(3, 18, 2, 2)  # creating the window same size as rectangle
    box = Textbox(win)

    rectangle(stdscr, 1, 1, 5, 20)
    stdscr.refresh()

    box.edit()  # ctrl + G to exit
    text = box.gather().strip().replace("\n", '')
    stdscr.addstr(10, 40, text)

    stdscr.getch()


wrapper(main)
