
# Log Parsing Script

This script performs log parsing from stdin, extracting information about status codes and file sizes from log entries and calculating relevant statistics based on the specified input format.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Usage](#usage)
- [Setup](#setup)
- [License](#license)

## Overview

The script reads log entries from the standard input (stdin), extracts status codes and file sizes based on a specific log entry format, and calculates statistics such as total file size and the count of each status code. It prints the statistics after every 10 lines of input or upon receiving a keyboard interruption (CTRL + C).

## Features

- Parses log entries from standard input.
- Calculates statistics including total file size and count of each status code.
- Handles keyboard interruption (CTRL + C) gracefully and prints statistics accordingly.
- Provides clean and organized code for easy understanding and maintenance.

## Usage

To use the script, pipe the log entries into the script using a generator script or any other means of providing input through stdin.

Example usage with a generator script:
```bash
./0-generator.py | ./0-stats.py
```

## Setup

1. **Clone the repository:**
    ```bash
    git clone <repository_url>
    cd log-parsing-script
    ```

2. **Run the script:**
   ```bash
   ./0-generator.py | ./0-stats.py
   ```

   Note: Replace `0-generator.py` with the appropriate input generator script.

## License

This project is licensed under the [MIT License](LICENSE).

---

Feel free to customize and enhance the documentation to better suit your specific use case and requirements.
