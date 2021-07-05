#!/usr/bin/env python3
#
# files.py
#
import os, random
from os.path import join, splitext
import log

1234567890123456789012345678901234567890123456789012345678901234567890
"""
Collect all the filenames of card faces.
"""
__all__ = ["card_pathnames", ]
__author__ = "https://github.com/psb-2020-2021-apcsp/"
__copyright__ = "Copyright 2021, Public Schools of Brookline 2020-2021 APCS-P"
__license__ = "https://choosealicense.com/licenses/mit/"
__version__ = "0.0.1"
__maintainer__ = "David C. Petty"
__email__ = "david_petty@psbma.org"
__status__ = "Development"

logger = log.log(__name__)  # initialize logger


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
    logger.info(f"{len(cards)} {path} {[os.path.basename(c) for c in cards]}")
    return cards


# TODO: update from game.py or remove from here
def random_list(card_list, pairs):
    """Return random list of pairs of paths from card_list up to pairs pairs."""
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
    logger.info(f"{len(outlist)} {outlist}")
    return outlist


if __name__ == "__main__":
    from os.path import abspath, dirname, join
    card_path = abspath(join(dirname(__file__), '../cards/faces'))
    card_paths = card_pathnames(card_path)
    randomized = random_list(card_paths, len(card_paths) // 2)
