"""
Pads and Windows - 1
======================
Windows ≡ screen
Create our own windows that are smaller and apart from the main window. Allowing us more control over text and refresh
each individual window.

Pad → It is special type of window. Allows certain amount of text to be shown on the screen at a time.
"""

import curses
import time
from curses import wrapper


def main(stdscr):
    # adding colors by creating a color palette. ID references col combos.
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_YELLOW)  # (id or pair no, foreground color, background color)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_RED, curses.COLOR_WHITE)
    _blue_and_yellow = curses.color_pair(1)
    _green_and_black = curses.color_pair(2)
    _red_and_white = curses.color_pair(3)

    counter_win = curses.newwin(1, 20, 10, 10)
    stdscr.addstr("Hello World!")
    stdscr.refresh()

    for i in range(1, 101):
        counter_win.clear()
        color = _blue_and_yellow

        if i % 2 == 0:
            color = _green_and_black

        counter_win.addstr(f"Count: {i}", color)
        counter_win.refresh()
        time.sleep(0.1)

    stdscr.getch()


wrapper(main)
