#!/usr/bin/env python3
#
# timer.py
#
import threading
from time import sleep
import gameplay, log

1234567890123456789012345678901234567890123456789012345678901234567890
"""
Define fractions-of-a-second timer.
"""

logger = log.log(__name__)    # initialize logger

# Initialize module data.
total, delay, increment, maximum, counting, done = 0, 0, 0.25, 60, True, False
# Callback for echo, fsm w/ default.
echo, fsm = logger.debug, lambda: logger.debug('fsm()')

def reset():
    """Reset total and echo '00:00'."""
    global total, maximum
    total, delay = 0, 0
    echo('00:00')

def start_wait(time=2):
    """Start gameplay delay."""
    global delay
    delay = total + time
    logger.info(f"wait until: {delay:.2f} = {total:.2f} + {time:.2f}")

def run():
    """Count second 25ths and echo it on even seconds until done."""
    global total, counting
    reset()
    while True:
        sleep(increment)
        if counting:
            total += increment
            if int(total) == total:
                echo(format(total))
            if total == delay:
                # TODO: random clicking can negate this call
                fsm()
            if total > maximum:
                counting = False
        if done:
            logger.info(f"Timer exiting...")
            break

# Define timer daemon thread. https://stackoverflow.com/a/59130384
def run_timer(): 
  timer = threading.Thread(target=run, daemon=True)
  timer.start()
  return timer

def format(total):
    """Return formatted seconds as mins:secs."""
    mins, secs = int(total) // 60, int(total) % 60
    return f"{mins:02d}:{secs:02d}"

if __name__ == "__main__":
    # Log everything, including logging.DEBUG.
    logger.setLevel('DEBUG')
    for handler in logger.handlers:
        handler.setLevel('DEBUG')
    timer = run_timer()
    # Count up to 5, then pause counting for 2s, then done.
    while True:
        if total > 5:
            counting = False; logger.info('wait 2s...'); sleep(2)
            done = True
            timer.join()
            logger.info(f"timer thread killed @ {total:.2f}s")
            break
