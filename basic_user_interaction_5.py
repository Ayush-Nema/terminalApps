"""
Introduction to basic user interaction
==========================================
Understanding how to interact with user input
"""

import curses
from curses import wrapper


def main(stdscr):
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_YELLOW)  # (id or pair no, foreground color, background color)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_RED, curses.COLOR_WHITE)
    _blue_and_yellow = curses.color_pair(1)
    _green_and_black = curses.color_pair(2)
    _red_and_white = curses.color_pair(3)

    stdscr.nodelay(True)  # precedes over stdscr.getkey()

    x, y = 0, 0
    str_x = 0
    while True:
        try:
            key = stdscr.getkey()  # waits for the user to give some input
        except:
            key = None

        if key == "KEY_LEFT":
            x -= 1
        elif key == "KEY_RIGHT":
            x += 1
        elif key == "KEY_UP":
            y -= 1
        elif key == "KEY_DOWN":
            y += 1

        stdscr.clear()

        str_x += 1
        stdscr.addstr(0, str_x // 500, "hello world")

        stdscr.addstr(y, x, "0")
        stdscr.refresh()


wrapper(main)
