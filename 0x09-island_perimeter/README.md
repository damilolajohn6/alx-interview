# # 0x09-island_perimeter

## Description

This project contains a Python script that defines a function `island_perimeter` to calculate the perimeter of an island described in a 2D grid.

## Files

- `0-island_perimeter.py`: Python script containing the `island_perimeter` function.
- `0-main.py`: Example usage of the `island_perimeter` function.

## Requirements

- Allowed editors: vi, vim, emacs
- All files interpreted/compiled on Ubuntu 20.04 LTS using Python 3.4.3
- Code should use the PEP 8 style (version 1.7)
- No module imports allowed
- All modules and functions must be documented
- All files must be executable

## Function Description

```python
def island_perimeter(grid):
    """
    Returns the perimeter of the island described in grid.

    Args:
        grid (list of list of int): 2D grid where 0 represents water and 1 represents land.

    Returns:
        int: The perimeter of the island.

    Requirements:
        - The grid is completely surrounded by water.
        - There is only one island (or nothing).
        - The island doesn’t have “lakes” (water inside that isn’t connected to the water surrounding the island).
    """
```

## Usage

```python
# Example in 0-main.py
grid = [
    [0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0]
]
print(island_perimeter(grid))
```

## Testing

To run the provided example:

```bash
./0-main.py
```

This should output the expected result based on the provided grid.

## Author
damilolajohn6 (damilolajohn622@gmail.com)
