#!/usr/bin/python3

"""
Log Parsing Script
"""

import re
import sys

def print_statistics(file_size, status_counts):
    """
    Prints the accumulated statistics including the total file size and the count of status codes.

    Args:
        file_size (int): The total file size.
        status_counts (dict): A dictionary containing status codes as keys and their counts as values.

    Returns:
        None
    """
    print("File size: {}".format(file_size))
    for status_code, count in sorted(status_counts.items()):
        if count > 0:
            print("{}: {}".format(status_code, count))

def parse_log_line(line, status_counts):
    """
    Parses a log line, extracts the status code and file size, and updates the status code counts.

    Args:
        line (str): A log line to be parsed.
        status_counts (dict): A dictionary to keep track of status code counts.

    Returns:
        int: The file size extracted from the log line.
    """
    # Use regex to extract status code and file size
    match = re.match(r'.* "GET /projects/260 HTTP/1.1" (\d+) (\d+)', line)
    if match:
        status_code, file_size = map(int, match.groups())
        if status_code in status_counts:
            status_counts[status_code] += 1
        return file_size
    return 0

if __name__ == "__main__":
    total_file_size = 0
    status_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}

    try:
        for line_number, line in enumerate(sys.stdin, start=1):
            file_size = parse_log_line(line, status_counts)
            total_file_size += file_size

            if line_number % 10 == 0:
                print_statistics(total_file_size, status_counts)
        
        # Print final statistics
        print_statistics(total_file_size, status_counts)

    except KeyboardInterrupt:
        # Print final statistics on keyboard interruption
        print_statistics(total_file_size, status_counts)
        raise
