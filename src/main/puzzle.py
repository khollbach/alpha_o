#!/usr/bin/python3

from color import *
from file_io import *

import preprocess

class Puzzle:
    '''
    A class representing a grid of tiles.
    Tiles can be colored white/black/unknown. See Color class.
    '''

    def __init__(self, row_hints, col_hints):
        '''(Puzzle, [int], [int]) -> None
        '''
        # These should remain constant once initialized.
        self.row_hints = row_hints
        self.col_hints = col_hints
        self.num_rows = len(self.row_hints)
        self.num_cols = len(self.col_hints)

        self.grid = [[Color.none for j in range(self.num_cols)]
                for i in range(self.num_rows)]

        self.row_fullness = [0 for i in range(self.num_rows)]
        self.col_fullness = [0 for j in range(self.num_cols)]

        preprocess.preprocess(self)

    def __str__(self):
        '''(Puzzle) -> str
        '''
        return grid_to_str(self.grid)

    def get(self, i, j):
        '''(Puzzle, int, int) -> Color
        '''
        return self.grid[i][j]

    def set(self, i, j, color):
        '''(Puzzle, int, int, Color) -> None
        '''
        if not isinstance(color, Color):
            raise ValueError('Not a color: ' + str(color))
        if color == Color.none and self.grid[i][j] != Color.none:
            self.row_fullness[i] -= 1
            self.col_fullness[j] -= 1
        if color != Color.none and self.grid[i][j] == Color.none:
            self.row_fullness[i] += 1
            self.col_fullness[j] += 1
        self.grid[i][j] = color

def island_sizes(row_or_col):
    '''([Color]) -> [int]
    Return the sizes of the islands in a completely colored row or column.

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
            raise Exception("This row or column" +
                    "hasn't been completely colored.")

    if current_island_size > 0:
        islands.append(current_island_size)

    return islands

def satisfies_hint(row_or_col, hint):
    '''([Color], [int]) -> bool
    Return True iff the row or column has a complete coloring that agrees with
    the 'hint'.

    >>> w, b = Color.white, Color.black
    >>> satisfies_hint([w, b, b, b, b, w, w, w, b, w, b, b, b, b, b], [4, 1, 5])
    True
    >>> satisfies_hint([w, b, b, b, b, w, w, b, b, w, b, b, b, w, w], [4, 3, 2])
    False
    '''
    return island_sizes(row_or_col) == hint

def check_consistency(row_hints, col_hints):
    '''([[int]], [[int]]) -> bool
    Return False if the hints are obviously impossible, or meaningless.
    I.e.: non-positive island sizes, or over-crowded rows or columns.
    '''
    # Enusure no non-positive numbers.
    for hints in (row_hints, col_hints):
        for hint in hints:
            for island in hint:
                if island <= 0:
                    return False

    # Check consistancy of the hints with the row/column lengths.
    for hint in row_hints:
        if d_value(hint, len(col_hints)) < 0:
            return False
    for hint in col_hints:
        if d_value(hint, len(row_hints)) < 0:
            return False

    return True

def is_jagged(grid):
    '''([[Color]]) -> bool
    Return True if the grid is jagged.
    '''
    length = None
    for row in grid:
        if length is None:
            length = len(row)
        else:
            if len(row) != length:
                return True
    return False

if __name__ == '__main__':
    import doctest
    doctest.testmod()
