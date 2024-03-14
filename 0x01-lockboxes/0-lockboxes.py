#!/usr/bin/python3
"""method that determines if all the boxes can be opened"""


def canUnlockAll(boxes):
    """Create a method"""

    for key in range(1, len(boxes)):
        result = False
        for box in range(len(boxes)):
            if key in boxes[box] and box != key:
                result = True
                break
        if not result:
            return False

    return True
