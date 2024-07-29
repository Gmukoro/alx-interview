#!/usr/bin/python3
import sys
import signal


def print_stats(total_file_size, status_code_counts):
    print("File size: {}".format(total_file_size))
    for code in sorted(status_code_counts.keys()):
        if status_code_counts[code] > 0:
            print("{}: {}".format(code, status_code_counts[code]))


total_file_size = 0
line_count = 0
status = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}


def signal_handler(sig, frame):
    print_stats(total_file_size, status)
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

for line in sys.stdin:
    parts = line.split()
    if len(parts) < 7:
        continue

    try:
        file_size = int(parts[-1])
        status_code = int(parts[-2])
    except ValueError:
        continue

    total_file_size += file_size
    if status_code in status:
        status[status_code] += 1

    line_count += 1

    if line_count % 10 == 0:
        print_stats(total_file_size, status)

print_stats(total_file_size, status)
