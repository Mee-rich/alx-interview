#!/usr/bin/python3
"""
Write a script that reads stdin line by line and computes metrics:

    Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size> (if the format is not this one, the line must be skipped)
    After every 10 lines and/or a keyboard interruption (CTRL + C), print these statistics from the beginning:
        Total file size: File size: <total size>
        where <total size> is the sum of all previous <file size> (see input format above)
        Number of lines by status code:
            possible status code: 200, 301, 400, 401, 403, 404, 405 and 500
            if a status code doesn’t appear or is not an integer, don’t print anything for this status code
            format: <status code>: <number>
            status codes should be printed in ascending order
"""

import sys
import signal
from functools import wraps

total_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

def print_stats_decorator(func):
    """Decorator to print stats every 10 lines and upon interrupt (Ctlr + C)."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        global line_count
        try:
            result = func(*args, **kwargs)
            line_count += 1
            if line_count % 10 == 0:
                print_stats()
            return result
        except KeyboardInterrupt:
                print_stats()
                sys.exit(0)
    return wrapper

def process_decorator(func):
    """Decorator to process the input line and update stattistics."""
    @wraps(func)
    def wrapper(line):
        global total_size, status_codes
        parts = line.split()
        if len(parts) < 9:
            return # Skips lines taht don't match the format

        try:
            #Extract necessary files
            status_code = int(parts[8])
            file_size = int(parts[9])

            #Update metrics
            total_size += file_size
            if status_code in status_codes:
                status_codes[status_code] += 1

        except (ValueError, IndexError)
        return #Skip malformes lines
    return wrapper

def print_stats():
    """Prints the metrics collected"""
    print(f"File size: {total_size}")
    for code in sorted(status_codes):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")

@print_stats_decorator
@process_decorator
def process_line(line):
    """Processes a single line of input."""
    pass  # Actual processing is handled by decorators

def signal_handler(sig, frame):
    """Handle keyboard interrupt signal (Ctrl + C)."""
    print_stats()
    sys.exit(0)

# Register the signal handler for Ctrl + C
signal.signal(signal.SIGINT, signal_handler)

if __name__ == "__main__":
    try:
        for line in sys.stdin:
            process_line(line.strip())

    except KeyboardInterrupt:
        print_stats()
        sys.exit(0)

    # Print remaining stats after processing all lines
    print_stats()


