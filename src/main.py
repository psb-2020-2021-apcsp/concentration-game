#!/usr/bin/env python3
#
# main.py
#
import app, timer, sys

"""
Concentration card game. This module currently creates the windows.
"""
1234567890123456789012345678901234567890123456789012345678901234567890

def on_closing(root):
    """Stop timer, destroy app, and exit."""
    timer.done = True
    timer.timer.join()
    root.destroy()
    sys.exit()

if __name__ == "__main__":
    concentration = app.App()
    concentration.protocol("WM_DELETE_WINDOW", lambda: on_closing(concentration))
    concentration.mainloop()
