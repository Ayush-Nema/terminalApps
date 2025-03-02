"""
Other useful commands
=======================
Demonstration of few useful functions
"""

import curses
from curses import wrapper
from curses.textpad import rectangle


def main(stdscr):
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_YELLOW)  # (id or pair no, foreground color, background color)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_RED, curses.COLOR_WHITE)
    _blue_and_yellow = curses.color_pair(1)
    _green_and_black = curses.color_pair(2)
    _red_and_white = curses.color_pair(3)

    # 1. Change rectangle color (toggle attributes)
    stdscr.attron(_green_and_black)
    rectangle(stdscr, 1, 1, 5, 20)
    stdscr.addstr(5, 30, "Hello world!")
    stdscr.attroff(_green_and_black)

    # 2. Window border
    # stdscr.attron(_red_and_white)
    stdscr.border()
    # stdscr.attroff(_red_and_white)

    # 3. Change cursor location
    stdscr.move(10, 20)

    stdscr.refresh()
    stdscr.getch()

    # 4. Print user keystrokes
    curses.echo(True)
    while True:
        key = stdscr.getkey()
        if key == 'q':
            break


wrapper(main)
