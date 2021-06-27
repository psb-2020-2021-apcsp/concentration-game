#!/usr/bin/env python3
#
# log.py
#
import logging, tempfile

1234567890123456789012345678901234567890123456789012345678901234567890
"""
Logging module that logs to the console and a temporary log file.
"""
# Initialize global log_path for temporary log file.
log_path = None

# TODO: Set default level to logging.WARNING, once working.
def log(name, level=logging.INFO):
    """Return logger with name and level."""
    global log_path
    new_file = log_path is None

    FORMAT = '{asctime:s} {name:^10s} [{threadName:^10s}] {levelname:<8s} {message:s}'
    FORMAT = '{asctime:s} {name:^10s} {levelname:<8s} {message:s}'
    logging.basicConfig(filename='/dev/null', level=logging.NOTSET)
    logger = logging.getLogger(name)

    # Create file handler which logs messages at level.
    if new_file: fd, log_path = tempfile.mkstemp('.log', 'concentration-')
    fh = logging.FileHandler(log_path, 'w')
    fh.setLevel(level)

    # Create console handler which logs messages at level.
    ch = logging.StreamHandler()
    ch.setLevel(level)

    # Create formatter and add it to handlers.
    formatter = logging.Formatter(
        FORMAT, style='{', datefmt='%Y/%m/%d-%H:%M:%S')
    ch.setFormatter(formatter)
    fh.setFormatter(formatter)

    # Add the handlers to logger.
    logger.addHandler(ch)
    logger.addHandler(fh)

    if new_file: logger.info(f"LOG PATH: {log_path}")

    return logger

if __name__ == '__main__':
    logger = log(__name__)
    logger.debug('D: SPAM')
    logging.debug('D: SPAM')
    logger.info('I: SPAM, SPAM')
    logger.warning('W: SPAM, SPAM, SPAM')
    logger.error('E: SPAM, SPAM, SPAM, SPAM')
    logger.critical('C: SPAM, SPAM, SPAM, SPAM, SPAM')
