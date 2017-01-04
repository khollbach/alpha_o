#!/usr/bin/python3

from color import *

import puzzle

def c_value(hint):
    '''([int]) -> int
    The C-value for a row or column is the sum of the island sizes plus
    (num_islands - 1).  So, the total land mass plus the number of rivers in
    between islands.

    This is significant because it is the least space that these islands can
    take up; the length of the most compacted version of this row or column.

    >>> c_value([4, 1, 5])
    12
    >>> c_value([])  # Special case.
    0
    '''
    if len(hint) == 0:
        return 0
    else:
        return sum(hint) + len(hint) - 1

def d_value(hint, length):
    '''
    The length of the row or column minus the C-value.

    This is significant because it represents the degrees of freedom, or
    'slide factor', for that row or column. Rows/columns with a D-value of 0
    can be fully filled immediately, and ones with a D-value equals to the
    row's/column's length are entirely blank.

    A negative D-value indicates that the hint is impossible for a row/column
    of that length.

    Islands larger than the D-value for their row/column can have a number of
    black tiles filled equal to the difference between these two values:
    length minus D-value.

    >>> d_value([4, 1, 5], 15)
    3
    >>> d_value([], 15)
    15
    >>> # The following hint is impossible to satisfy in a row of length 10.
    >>> d_value([4, 1, 5], 10)
    -2
    '''
    return length - c_value(hint)

def line_solve(hint, length):
    '''([int], int) -> [Color]
    Solve a row or column for as many tiles as possible given just the hint
    and the length.

    This is a technique I call line-solving and relies on the D-value and
    the island sizes.

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

def preprocess(puzzle):
    '''(puzzle.Puzzle) -> None
    Compute the initial grid based on the preprocessing step.
    (I.e. perform line-solving on each row and column.)

    Raises an exception if a contradiction is found.
    '''
    # Line-solve each row.
    for i in range(puzzle.num_rows):
        row = line_solve(puzzle.row_hints[i], puzzle.num_cols)
        for j, color in enumerate(row):
            if color != Color.none:
                # Catch contradictions.
                prev_color = puzzle.get(i, j)
                if prev_color != Color.none and prev_color != color:
                    raise Exception('Contradiction. Impossible puzzle.')

                puzzle.set(i, j, color)

    # Line-solve each column.
    for j in range(puzzle.num_cols):
        col = line_solve(puzzle.col_hints[j], puzzle.num_rows)
        for i, color in enumerate(col):
            if color != Color.none:
                # Catch contradictions.
                prev_color = puzzle.get(i, j)
                if prev_color != Color.none and prev_color != color:
                    raise Exception('Contradiction. Impossible puzzle.')

                puzzle.set(i, j, color)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
