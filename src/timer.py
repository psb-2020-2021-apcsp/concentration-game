#!/usr/bin/env python3
#
# timer.py
#
import threading
from time import sleep

"""
Define tenths-of-a-second timer.
"""
1234567890123456789012345678901234567890123456789012345678901234567890

total, counting, done, echo = 0, True, False, print

def format(seconds):
    """Return formatted seconds as mins:secs."""
    mins, secs = int(total) // 60, int(total) % 60
    return f"{mins:02d}:{secs:02d}"

# run function
def run():
    """Count second 25ths and echo it on even seconds until done."""
    global total
    reset()
    while True:
        sleep(0.25)
        if counting:
            total += 0.25
            # Why not int(total) == total?
            if round(abs(total- int(total)), 3) == 0: echo(format(total))
        if done:  break

def reset():
    """Reset total and echo '00:00'."""
    global total
    total = 0
    echo('00:00')

# Define timer daemon thread. https://stackoverflow.com/a/59130384
timer = threading.Thread(target=run, daemon=True)

if __name__ == "__main__":
    timer.start()
    # Count up to 5, then pause counting for 2s, then done.
    while True:
        if total > 10:
            counting = False; print('wait 2s...'); sleep(2)
            done = True
            timer.join()
            print(f"timer thread killed @ {total:.2f}s")
            break
