#!/usr/bin/env python3
#
# files.py
#
import os
from os.path import abspath, dirname, join, splitext

"""
Collect all the filenames of card faces.
"""
1234567890123456789012345678901234567890123456789012345678901234567890

def card_pathnames(path, ext='.png'):
    """Return paths to files in path with ext."""
    # Create list for cards.
    cards = []

    # Iterate through files w/ "png" and append them to cards list.
    for root, dirs, files in os.walk(path, topdown=False):
        for name in files:
            head, tail = splitext(name)
            if ext == tail:
                cards.append(join(root, name))
    return cards

if __name__ == "__main__":
    cardpath = abspath(join(dirname(__file__), '../cards/faces'))
    cards = card_pathnames(cardpath)
    print(len(cards), cards)
