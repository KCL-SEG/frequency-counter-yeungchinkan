"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

from curses.has_key import has_key


def frequencies(items):
    frequencies = {}
    for i in items:
        
        if frequencies.has_key(i) == False:
            frequencies[i] = 1
        else:
            frequencies[i] += 1
    # Your code goes here
    return frequencies
