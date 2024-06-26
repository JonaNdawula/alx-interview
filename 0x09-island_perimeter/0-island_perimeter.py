#!/usr/bin/python3
"""
This modle contains the island_perimeter
function which returns the perimeter of the island
described in a grid
"""


def island_perimeter(grid):
    """
    Args:
    grid: List of integers where 0 is water and 1 is land
    Returns: Perimeter of island described in grid
    """
    perimeter = 0
    rows = len(grid)
    columns = len(grid[0]) if rows else 0

    for row in range(rows):
        for col in range(columns):
            if grid[row][col] == 1:
                edges = 4

                if row > 0 and grid[row - 1][col] == 1:
                    edges -= 1

                if row < rows - 1 and grid[row + 1][col] == 1:
                    edges -= 1

                if col > 0 and grid[row][col - 1] == 1:
                    edges -= 1

                if col < columns - 1 and grid[row][col + 1] == 1:
                    edges -= 1

                perimeter += edges

    return perimeter
