#!/usr/bin/env python3
"""A script to determine pascal's triangle for any number"""

from typing import List

def pascal_triangle(n: int) -> List[List[int]]:
    """
    returns a list of lists of integers representing the pascal's triangle of n
    """

    triangle = []

    if n == 0:
        return triangle
    for i in range(n):
        temp_list = []

        for j in range(i+1):
            temp_list.append(1)
        else:
            temp_list.append(triangle[i-1][j-1] + triangle[i+1][j])
         triangle.append(temp_list)
    # print(triangle)
    return triangle
