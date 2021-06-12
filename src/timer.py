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
    """Count second 10ths and echo it on even seconds until done."""
    global total
    reset()
    while True:
        sleep(0.1)
        if counting:
            total += 0.1
            if int(total * 10) % 10 == 0:
                echo(format(total))
        if done:
            break

def reset():
    """Reset total and echo '00:00'."""
    global total
    total = 0
    echo('00:00')

timer = threading.Thread(target=run)
# https://stackoverflow.com/a/59130384
timer.setDaemon(True)

if __name__ == "__main__":
    timer.start()
    while True:
        if total > 5:
            counting = False; print('wait 2s...'); sleep(2)
            done = True
            timer.join()
            print(f"timer thread killed @ {total:.2f}s")
            break
