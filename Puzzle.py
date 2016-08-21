from color import *

class Puzzle:
    '''
    Represents an O'Ekakki puzzle.
    Contains a state of the grid, where each tile is either Color.white, Color.black, or None.
    Keeps track of the constraints (a.k.a. 'hints') for each row and column in two lists.
    '''

    def __init__(self, row_constraints, column_constraints, grid=None):
        '''(Puzzle, [int, ...], [int, ...], [[Color, ...], ...]) -> None
        Create a new Puzzle.
        '''
        self._row_constraints = row_constraints
        self._column_constraints = column_constraints

        num_rows = len(row_constraints)
        num_columns = len(column_constraints)

        if grid is None:
            self._grid = [[None for j in range(num_columns)] for i in range(num_rows)]
        else:
            if len(grid) != num_rows:
                raise Exception('Grid dimensions disagree with number of row constraints.')

            for row in grid:
                if len(row) != num_columns:
                    raise Exception('Grid dimensions disagree with number of column constraints.')

            self._grid = grid

    def get_num_rows(self):
        '''(Puzzle) -> int
        Get the number of rows.
        '''
        return len(self._row_constraints)

    def get_num_columns(self):
        '''(Puzzle) -> int
        Get the number of columns.
        '''
        return len(self._column_constraints)

    def get_tile(self, i, j):
        '''(Puzzle, int, int) -> Color
        Get the color of a specified tile. A color of None represents an unknown/unset tile.
        '''
        return self._grid[i][j]

    def set_tile(self, i, j, color):
        '''(Puzzle, int, int, Color) -> None
        Sets a tile to a given color. color can be None for unknown tiles.
        '''
        self._grid[i][j] = color

    def get_row(self, i):
        '''(Puzzle, int) -> [Color, ...]
        Returns a copy of the specified row. Changing the copy won't affect this Puzzle.
        '''
        return list(self._grid[i])

    def get_column(self, j):
        '''(Puzzle, int) -> [Color, ...]
        Returns a copy of the specified column. Changing the copy won't affect this Puzzle.
        '''
        return list(row[j] for row in self._grid)

    def get_row_constraint(self, i):
        '''(Puzzle, int) -> [Color, ...]
        Returns a copy of the specified row constraint.
        '''
        return list(self._row_constraints[i])

    def get_column_constraint(self, j):
        '''(Puzzle, int) -> [Color, ...]
        Returns a copy of the specified column constraint.
        '''
        return list(self._column_constraints[j])

    def __str__(self):
        '''(Puzzle) -> str
        Return a string that visually represents the grid for this puzzle.
        '''
        s = ''
        for row in self._grid:
            for tile in row:
                if tile is None:
                    s += '?'
                else:
                    s += str(tile)
            s += '\n'
        return s

def satisfies_constraint(row_or_column, constraint):
    '''([Color, ...], [int, ...]) -> bool
    Return True iff the row or column has a complete coloring that agrees with the 'hint'.
    '''
    # 'Island' is my terminology for a sequence of black tiles bookended by white tiles and/or
    # edges of the grid.
    # The list 'islands' will accumulate the island sizes for the given row or column.
    # E.g., if: row == [white, BLACK, BLACK, BLACK, white, white, BLACK, white, BLACK, BLACK]
    #     then: islands == [3, 1, 2]
    islands = []

    current_island_size = 0
    for tile in row_or_column:
        if tile == Color.white:
            if current_island_size > 0:
                islands.append(current_island_size)
            current_island_size = 0
        elif tile == Color.black:
            current_island_size += 1
        else:
            # If a tile is neither white nor black, the coloring is incomplete.
            return False

    if current_island_size > 0:
        islands.append(current_island_size)

    return islands == constraint
