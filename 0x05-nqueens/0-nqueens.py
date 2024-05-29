#!/usr/bin/python3
"""
Module containing functions to solve the n queens Puzzle
"""
import sys


def queens_problem(size):
    """
    function to solve the N queens puzzle
    """

    def position_valid(position, has_piece):
        """
        function to check if the position is valid
        """
        for i in range(len(has_piece)):
            if (
                has_piece[i] == position or
                has_piece[i] - i == position - len(has_piece) or
                has_piece[i] + i == position + len(has_piece)
            ):
                return False
        return True

    def queens_position(size, index, has_piece, solutions):
        """
        function to track queens position
        """
        if index == size:
            solutions.append(has_piece[:])
            return

        for i in range(size):
            if position_valid(i, has_piece):
                has_piece.append(i)
                queens_position(size, index + 1, has_piece, solutions)
                has_piece.pop()

    solutions = []
    queens_position(size, 0, [], solutions)
    return solutions


def execute():
    """
    function to execute the solution
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        size = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if size < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = queens_problem(size)
    for sol in solutions:
        print([[i, sol[i]] for i in range(len(sol))])


if __name__ == "__main__":
    execute()
