"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    for i in items:
        count = frequencies[i]
        if count == None:
            frequencies[i] = 1
        else:
            frequencies[i] = count + 1
    # Your code goes here
    return frequencies
