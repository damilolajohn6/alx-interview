import sys
import re
from collections import defaultdict

# Initialize variables to store metrics
total_file_size = 0
status_counts = defaultdict(int)

try:
    for line_number, line in enumerate(sys.stdin, start=1):
        line = line.strip()
        # Use regex to extract necessary information from the line
        match = re.match(r'^\d+\.\d+\.\d+\.\d+ - \[.*\] "GET /projects/260 HTTP/1.1" (\d+) (\d+)$', line)
        if match:
            status_code, file_size = map(int, match.groups())
            total_file_size += file_size
            status_counts[status_code] += 1

        # Print statistics every 10 lines
        if line_number % 10 == 0:
            print("Total file size: File size: {}".format(total_file_size))
            for status_code in sorted(status_counts.keys()):
                print("{}: {}".format(status_code, status_counts[status_code]))

except KeyboardInterrupt:
    # Print statistics on keyboard interruption
    print("Total file size: File size: {}".format(total_file_size))
    for status_code in sorted(status_counts.keys()):
        print("{}: {}".format(status_code, status_counts[status_code]))
