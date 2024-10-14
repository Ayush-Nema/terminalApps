"""
Build a simple timer
=======================

Building a flashing timer
"""

import curses
import time
from curses import wrapper


def main(stdscr):
    # adding colors by creating a color palette. ID references col combos.
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_YELLOW)  # (id or pair no, foreground color, background color)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
    _blue_and_yellow = curses.color_pair(1)
    _green_and_black = curses.color_pair(2)

    total_steps = 100  # total 10 secs (100 units updating in 0.1 secs each)
    sleep_time = 0.1
    total_time = total_steps * sleep_time

    for i in range(total_steps):
        stdscr.clear()
        color = _blue_and_yellow

        if i % 2 == 0:
            color = _green_and_black

        stdscr.addstr(f"Time: {(i + 1) / total_time:.1f} / {total_time}secs", color)
        stdscr.refresh()
        time.sleep(sleep_time)

    stdscr.getch()


wrapper(main)
