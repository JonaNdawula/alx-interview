#!/usr/bin/python3
"""
LockBoxes
"""


def canUnlockAll(boxes):
    """
    Determines if all boxes can be opened

    Args:
        boxes: list of lists where each inner list represents the keys in a box

        Returns:
            True if all boxes can be opened and false if not
    """

    n = len(boxes)
    keys = {0}
    visited = {0}

    while keys:
        nxt_key = keys.pop()
        for key in boxes[nxt_key]:
            if key not in visited and 0 < key < n:
                keys.add(key)
                visited.add(key)

    return (len(visited) == n)
