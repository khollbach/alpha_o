from color import *

def island_sizes(row_or_col):
    '''([Color]) -> [int]
    Return the sizes of the islands in a completely colored (no None's) row or column.

    >>> w, b = Color.white, Color.black
    >>> island_sizes([w, b, b, b, b, w, w, w, b, w, b, b, b, b, b])
    [4, 1, 5]
    '''
    islands = []

    current_island_size = 0
    for tile in row_or_col:
        if tile == Color.white:
            if current_island_size > 0:
                islands.append(current_island_size)
            current_island_size = 0
        elif tile == Color.black:
            current_island_size += 1
        else:
            raise Exception("This row or column hasn't been completely colored.")

    if current_island_size > 0:
        islands.append(current_island_size)

    return islands

def satisfies_hint(row_or_col, hint):
    '''([Color], [int]) -> bool
    Return True iff the row or column has a complete coloring that agrees with the 'hint'.

    >>> w, b = Color.white, Color.black
    >>> satisfies_hint([w, b, b, b, b, w, w, w, b, w, b, b, b, b, b], [4, 1, 5])
    True
    >>> satisfies_hint([w, b, b, b, b, w, w, b, b, w, b, b, b, w, w], [4, 3, 2])
    False
    '''
    return island_sizes(row_or_col) == hint

def c_value(hint):
    '''([int] -> int
    The C-value for a row or column is the sum of the island sizes plus (num_islands - 1).
    So, the total land mass plus the number of rivers in between islands.
    This is significant because it is the least space that these islands can take up;
    the length of the most compacted version of this row or column.

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
    This is significant because it represents the degrees of freedom, or 'slide factor', for that
    row or column. Rows/columns with a D-value of 0 can be fully filled immediately, and ones with
    a D-value equals to the row's/column's length are entirely blank.

    A negative D-value indicates that the hint is impossible for a row/column of that length.

    Islands larger than the D-value for their row/column can have a number of black tiles filled
    equal to the difference between these two values: length minus D-value.

    >>> d_value([4, 1, 5], 15)
    3
    >>> d_value([], 15)
    15
    >>> d_value([4, 1, 5], 10)  # !!! this hint is impossible to satisfy in a row of length 10.
    -2
    '''
    return length - c_value(hint)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
