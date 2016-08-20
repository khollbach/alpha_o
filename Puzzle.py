from Color import Color

class Puzzle:
    def __init__(self, row_hints, column_hints, grid=None):
        '''(Puzzle, [int, ...], [int, ...], [[Color, ...], ...]) -> None
        '''
        if grid is None:
            self._grid = [[None for j in range(len(column_hints))] for i in range(len(row_hints))]
        else:
            num_columns = len(grid[0])
            for i in range(1, len(grid)):
                if len(grid[i]) != num_columns:
                    raise Exception('Jagged grid.')
            self._grid = grid
        self._row_hints = row_hints
        self._column_hints = column_hints

    def get_num_rows(self):
        '''(Puzzle) -> int
        '''
        return len(self._grid)

    def get_num_columns(self):
        '''(Puzzle) -> int
        '''
        return len(self._grid[0])

    def get_tile(self, i, j):
        '''(Puzzle, int, int) -> Color
        '''
        return self._grid[i][j]

    def set_tile(self, i, j, color):
        '''(Puzzle, int, int, Color) -> None
        '''
        self._grid[i][j] = color

    def get_row(self, i):
        '''(Puzzle, int) -> [Color, ...]
        '''
        return list(self._grid[i])

    def get_column(self, j):
        '''(Puzzle, int) -> [Color, ...]
        '''
        return list(row[j] for row in self._grid)

    def __str__(self):
        s = ''
        for row in self._grid:
            for tile in row:
                if tile is None:
                    s += '?'
                else:
                    s += str(tile)
            s += '\n'
        return s
