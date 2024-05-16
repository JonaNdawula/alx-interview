#!/usr/bin/python3
"""
This module contains a script
that reads stdin line by
line and computes metrices
"""
import sys
import signal


status_codes = {
    '200': 0,
    '301': 0,
    '400': 0,
    '401': 0,
    '403': 0,
    '404': 0,
    '405': 0,
    '500': 0
}
total_size = 0
line_count = 0


def print_stats():
    """
    prints the status code
    """
    print(f"File size: {total_size}")
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")


def signal_handler(sig, frame):
    """
    handles the signal
    """
    print_stats()
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        try:
            parts = line.split()
            size = int(parts[-1])
            if size < 0:
                continue

            status_code = parts[-2]
            if not status_code.isdigit() or len(status_code) != 3:
                continue

            if status_code not in status_codes:
                status_codes[status_code] = 0

            if status_code in status_codes:
                status_codes[status_code] += 1
            
            total_size += size
            line_count += 1

            if line_count % 10 == 0:
                print_stats()

        except (IndexError, ValueError):
            continue

except SystemExit:
    pass

finally:
    print_stats()
