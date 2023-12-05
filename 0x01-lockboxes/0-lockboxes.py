#!/usr/bin/python3

"""Method to determine if all boxes can be unlock"""


def canUnlockAll(boxes):
    """Determines if all boxes can be opened
       Arg:
          boxes: list of lists
       Return:
          True or False
    """
    n = len(boxes)
    opened = set()
    opened.add(0)   # The first boxe is already opened

    keys = [0]   # stack used to store keys or index of boxes not yet traversed

    while keys:
        current_box = keys.pop()
        for key in boxes[current_box]:
            if key < n and key not in opened:
                opened.add(key)
                keys.append(key)
    return len(opened) == n
