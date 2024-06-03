#!/usr/bin/python3
"""Writing a function for Pascal's Triangle"""

def pascal_triangle(n):
    """
    Generates Pascal's triangle up to the nth row.
    Returns a list of lists of integers.
    """
    if n <= 0:
        return []  # Return an empty list for non-positive n

    triangle = []  # Initialize an empty list to store the triangle rows
    for i in range(n):
        row = [1]  # The first element of each row is always 1
        if i > 0:
            # Calculate the middle elements of the row
            prev_row = triangle[-1]
            for j in range(1, i):
                row.append(prev_row[j - 1] + prev_row[j])
            row.append(1)  # The last element of each row is also 1
        triangle.append(row)

    return triangle

