"""
Pads and Windows - 2
======================
Windows ≡ screen
Create our own windows that are smaller and apart from the main window. Allowing us more control over text and refresh
each individual window.

Pad → It is special type of window. Allows certain amount of text to be shown on the screen at a time.

[IMP] Getting max rows and columns based on current shell
```python
import curses
max_r, max_c = (curses.LINES -1, curses.COLS -1)
```
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

    pad = curses.newpad(100, 100)
    stdscr.refresh()

    for i in range(100):
        for j in range(26):
            char = chr(67 + j)
            pad.addstr(char, _green_and_black)

    """
    pad.refresh(x, y, x1, y1, x2, y2)
    (x, y) → (row, column) where we want to show the padded content
    (x1, y1) → (r, c) of top right hand corner where we want to display the content on the window
    (x2, y2) → (r, c) of bottom right hand corner of where we want to display the content
    """

    # pad.refresh(0, 0, 5, 5, 25, 75)
    # pad.refresh(0, 0, 5, 5, 25, 25)
    # pad.refresh(0, 0, 5, 5, 10, 75)
    # pad.refresh(5, 5, 5, 5, 10, 75)

    # adding the live update feature (comment above `pad.refresh` statement for running this)
    for k in range(50):
        stdscr.clear()
        stdscr.refresh()

        # pad.refresh(0, k, 5, 5, 10, 25)  # way-1: scrolling the content towards right (horizontal)
        # pad.refresh(0, 0, 5, k, 10, 25 + k)  # way-2: moving the pad itself
        # pad.refresh(0, k, 5, k, 10, 25 + k)  # way-3: scrolling through the content
        # pad.refresh(0, k, 5 + k, k, 10 + k, 25 + k)  # way-4: diagonal movement. Note: make `k` smaller here (≤ 35)
        pad.refresh(k, 0, 0, 0, 20, 20)  # way-4: vertical movement

        time.sleep(0.2)

    stdscr.getch()


wrapper(main)
