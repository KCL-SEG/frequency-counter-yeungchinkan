"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

from curses.has_key import has_key


def frequencies(items):
    frequencies = {}
    for i in items:
        
        if str(i) in frequencies == False and i in frequencies == False:
            frequencies[str(i)] = 1
        else:
            frequencies[str(i)] += 1
    # Your code goes here
    return frequencies
