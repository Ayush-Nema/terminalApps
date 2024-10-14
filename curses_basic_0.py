"""
Basics of `curses`
===================
Building a basic application for demonstrating features of `curses`.

The `curses` module comes preinstalled in macOS and Linux-based system. But needs to be installed in Windows.
For windows use `python -m pip install windows-curses`

Terms:
- `stdscr`: Standard output Screen. Standard output is a stream to which a program writes its output data.

Note:
- To run the application, use terminal: `python curses_basic_0.py` (use separate terminal window; does not seem to work in
Pycharm default terminal)
- Once the app starts, press any key to exit
"""

import curses
from curses import wrapper


def main(stdscr):
    stdscr.clear()  # clears the terminal screen

    # let us add some text to app
    stdscr.addstr("Hello world!", curses.A_UNDERLINE)  # prints at (0, 0) with underline
    stdscr.addstr(10, 10, "Shifted Hello world!")  # shifts the print argument at (10, 10)

    stdscr.refresh()  # updates the status of new screen
    stdscr.getch()  # gives the characters which user types; will be used in later demos


wrapper(main)  # calls the app
