#!/usr/bin/python3

from color import *
from preprocess import *
from puzzle import *

class CSPSolver:
    '''
    A class encapsulating the logic required to solve O'Ekakki puzzles using a
    simple backtracking algorithm.
    '''
    def __init__(self, row_hints, col_hints):
        '''(CSPSolver, [int], [int]) -> None
        Initialize the CSPSolver.
        '''
        self.row_hints = row_hints
        self.col_hints = col_hints
        self.grid = preprocess(row_hints, col_hints)


        # Fullness stats to enable efficient variable selection.

        self.row_fullness = [0] * len(self.row_hints)
        self.col_fullness = [0] * len(self.col_hints)

        for i, row in enumerate(self.grid):
            for j, tile in enumerate(row):
                if tile != Color.none:
                    self.row_fullness[i] += 1
                    self.col_fullness[j] += 1

    def backtrack(self, level=0):
        '''(CSPSolver, int) -> None
        Runs a backtracking algorithm on the puzzle.
        Throws a PuzzleSolvedException if solved, returns normally if no
        solutions.
        '''
        v = self._get_unassigned_variable()
        if v is None:
            raise PuzzleSolvedException('Nice!')
        i, j = v

        for d in (Color.white, Color.black):
            self.grid[i][j] = d

            pair1 = (self.grid[i], self.row_hints[i])

            col = [self.grid[x][j] for x in range(len(self.row_hints))]
            pair2 = (col, self.col_hints[j])

            for row_or_col, hint in (pair1, pair2):
                if any(tile == Color.none for tile in row_or_col):
                    continue
                if not satisfies_hint(row_or_col, hint):
                    break
            else:
                self.backtrack(level + 1)

        self.grid[i][j] = Color.none
        return

    def _get_unassigned_variable(self):
        '''(CSPSolver) -> (int, int)
        Return a pair of indeces indicating an unassigned variable/tile in the
        puzzle/grid. If no such pair exists, return None.
        '''
        for i in range(len(self.row_hints)):
            for j in range(len(self.col_hints)):
                if self.grid[i][j] == Color.none:
                    return i, j
        return None

    def _get_unassigned_variable2(self):
        '''(CSPSolver) -> (int, int)
        Return a pair of indeces indicating an unassigned variable/tile in the
        puzzle/grid.  If no such pair exists, return None.

        Uses the heuristic of most tiles filled in a row/column.
        '''
        raise Exception('NYI')

        pass  # TODO

class PuzzleSolvedException(Exception):
    pass
