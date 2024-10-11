#!/usr/bin/python3
"""
You have n number of locked boxes in front of you. Each box 
is numbered sequentially from 0 to n - 1 and each box 
may contain keys to the other boxes.
"""
from typing import List

def canUnlockAll(boxes: List[List[int]]) -> bool:
    """ A method that determines if all the boxes
    can be opened
    """
    unlocked_boxes = set([0])
    keys = set(boxes[0])

    while keys:
        new_key = keys.pop()
        if new_key not in unlocked_boxes and 0 <= new_key < len(boxes):
            unlocked_boxes.add(new_key)
            keys.update(boxes[new_key])

    return len(unlocked_boxes) == len(boxes)
