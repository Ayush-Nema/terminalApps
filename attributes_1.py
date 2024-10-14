"""
Attributes and colors
=======================

Exploring text styling with attributes and colors in `curses`.

Note: some of the attributes does not work on all OS platforms!
"""

import curses
from curses import wrapper


def main(stdscr):
    # adding colors by creating a color palette. ID references col combos.
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_YELLOW)  # (id or pair no, foreground color, background color)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_MAGENTA)
    _blue_and_yellow = curses.color_pair(1)
    _green_and_magenta = curses.color_pair(2)

    stdscr.clear()  # clears the terminal screen

    # let us add some text to app
    stdscr.addstr(0, 0, "Bold text", curses.A_BOLD)
    stdscr.addstr(1, 0, "Blinking text", curses.A_BLINK)  # does not work in macOS
    stdscr.addstr(2, 0, "Reversed text", curses.A_REVERSE)  # reverses the background and foreground of the text
    stdscr.addstr(3, 0, "Dim text", curses.A_BLINK)  # does not work in macOS
    stdscr.addstr(4, 0, "Standout text", curses.A_STANDOUT)  # works same as `A_REVERSE`
    stdscr.addstr(5, 0, "Underlined text", curses.A_UNDERLINE)

    # add the colors
    stdscr.addstr(7, 0, "Plain colored text -1", _blue_and_yellow)
    stdscr.addstr(8, 0, "Plain colored text -2", _green_and_magenta)

    # combine the attributes
    stdscr.addstr(10, 0, "Bold colored text", _blue_and_yellow | curses.A_BOLD | curses.A_REVERSE)

    stdscr.refresh()  # updates the status of new screen
    stdscr.getch()  # gives the characters which user types; will be used in later demos


wrapper(main)  # calls the app
