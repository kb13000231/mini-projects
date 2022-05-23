import curses
from curses import wrapper
import random
import time

ofile = open('quotes.txt', 'r')
sentences = [sentence.strip() for sentence in ofile.readlines()]
ofile.close()


def start_screen(stdscr):
    stdscr.clear()
    stdscr.addstr("Welcome to speed typing test!")
    stdscr.addstr("\nPress any key to begin!")
    stdscr.refresh()
    stdscr.getkey()


def display_text(stdscr, target, current, wpm=0):
    stdscr.addstr(target)
    stdscr.addstr(f"\nWPM:{wpm}", curses.color_pair(3))

    for i, char in enumerate(current):
        correct_char = target[i]
        color = curses.color_pair(1)
        if char != correct_char:
            color = curses.color_pair(2)
        stdscr.addstr(0, i, char, color)


def wpm_test(stdscr):
    target_text = random.choice(sentences)
    current_text = []
    wpm = 0
    start = time.time()
    stdscr.nodelay(True)

    while True:
        elapsed = max(time.time() - start, 1)  # To avoid div by 0 error
        wpm = round((len(current_text)/(elapsed/60))/5)
        stdscr.clear()
        display_text(stdscr, target_text, current_text, wpm)
        stdscr.refresh()

        if ''.join(current_text) == target_text:
            stdscr.nodelay(False)
            break

        try:
            key = stdscr.getkey()
        except Exception as ex:
            continue
            ex

        if ord(key) == 27:
            break
        if key in ("KEY_BACKSPACE", "\b", '\x7f'):
            if len(current_text) > 0:
                current_text.pop()
        elif len(current_text) < len(target_text):
            current_text.append(key)


def main(stdscr):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_CYAN, curses.COLOR_BLACK)
    start_screen(stdscr)
    while True:
        wpm_test(stdscr)
        stdscr.addstr(
            "\nYou've completed the test! Press any key to continue...")
        key = stdscr.getkey()
        if ord(key) == 27:
            break


wrapper(main)
