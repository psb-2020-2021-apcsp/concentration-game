#!/usr/bin/env python3
#
# main.py
#
import app, log

1234567890123456789012345678901234567890123456789012345678901234567890
"""
Concentration card game. This module currently creates the window and widgets.
"""
__author__ = "https://github.com/psb-2020-2021-apcsp/"
__copyright__ = "Copyright 2021, Public Schools of Brookline 2020-2021 APCS-P"
__license__ = "https://choosealicense.com/licenses/mit/"
__version__ = "0.0.1"
__maintainer__ = "David C. Petty"
__email__ = "david_petty@psbma.org"
__status__ = "Development"

logger = log.log(__name__)  # initialize logger

if __name__ == "__main__":
    concentration = app.App()
    concentration.mainloop()
