#The library of variables and functions that this program uses, including custom ones

from time import sleep
from random import choice

#A line of asterisks to break up sections
section_line = '*' * 30

#Modifies the print function to type text character by character, like it's being typed out
def print_slow(txt):
    for x in txt:
        print(x, end='', flush=True)
        sleep(0.025)
    print()
    