#!/usr/bin/python3

from puzzle import *
from color import *

def line_solve(hint, length):
    '''([int], int) -> [Color]
    Compute the most tile colors for a row or column given just the hint and the length.
    This is known as line-solving and relies on the D-value and the island sizes.

    >>> w, b, n = Color.white, Color.black, Color.none
    >>> line_solve([4, 1, 5], 15) == [n, n, n, b, n, n, n, n, n, n, b, b, n, n, n]
    True
    >>> line_solve([], 5) == [w, w, w, w, w]
    True
    >>> line_solve([4, 1, 5], 12) == [b, b, b, b, w, b, w, b, b, b, b, b]
    True
    '''
    d = d_value(hint, length)

    # Simple cases: zero islands.
    if d == length:
        return [Color.white] * length

    # Simple case: full solution.
    if d == 0:
        row_or_col = []
        for island in hint:
            row_or_col += [Color.black] * island + [Color.white]
        row_or_col.pop()
        return row_or_col

    row_or_col = []

    for island in hint:
        if island - d > 0:
            row_or_col += [Color.none] * d
            row_or_col += [Color.black] * (island - d)
            row_or_col += [Color.none]
        else:
            row_or_col += [Color.none] * island
            row_or_col += [Color.none]

    row_or_col += [Color.none] * (length - len(row_or_col))

    return row_or_col

def preprocess(row_hints, col_hints):
    '''([[int]], [[int]]) -> [[Color]]
    Compute the initial grid based on the preprocessing step (a.k.a. line-solving).

    Raises an exception if a contradiction is found.
    '''
    num_rows = len(row_hints)
    num_cols = len(col_hints)

    grid = []

    # Line-solve each row.
    for r in range(num_rows):
        grid.append(line_solve(row_hints[r], num_cols))

    # Line-solve each column.
    for c in range(num_cols):
        col = line_solve(col_hints[c], num_rows)
        for r in range(num_rows):
            if col[r] != Color.none:
                if grid[r][c] != Color.none and grid[r][c] != col[r]:
                    raise Exception('Contradiction. Impossible puzzle.')
                else:
                    grid[r][c] = col[r]

    return grid

if __name__ == '__main__':
    import doctest
    doctest.testmod()
