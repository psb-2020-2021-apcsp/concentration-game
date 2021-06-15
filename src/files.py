#!/usr/bin/env python3
#
# files.py
#
import os, random
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

def random_list(card_list, pairs):
    temp_list = card_list
    outlist = []
    for i in range(0, pairs):
        # https://docs.python.org/3/library/random.html#random.randint
        rand = random.randint(1, len(temp_list) - 1)
        outlist.append(temp_list[rand])
        temp_list.remove(temp_list[rand])
    # NOTE: We decided to randomize the image pairs in app.py ...plus
    #       copying the double list does not randomize the entire list.
    # outlist = outlist * 2
    return outlist

if __name__ == "__main__":
    cardpath = abspath(join(dirname(__file__), '../cards/faces'))
    cards = card_pathnames(cardpath)
    print(len(cards), cards)
    randomized = random_list(cards, len(cards) // 2)
    print(len(randomized), randomized)
