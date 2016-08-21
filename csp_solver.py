from puzzle import *

class CSPSolver:
    '''
    A class encapsulating the logic required to solve O'Ekakki puzzles using a simple
    backtracking algorithm.
    '''

    def __init__(self, puzzle):
        '''(CSPSolver, Puzzle) -> None
        Initialize a CSPSolver for a given puzzle.
        '''
        self._puzzle = puzzle

    def backtrack(self, level=0):
        '''(CSPSolver, int) -> None
        Runs a backtracking algorithm on the puzzle.
        Throws a PuzzleSolvedException if solved, returns normally if no solutions.
        '''
        v = self._get_unassigned_variable()
        if v is None:
            raise PuzzleSolvedException('Nice!')
        i, j = v

        for d in (Color.white, Color.black):
            self._puzzle.set_tile(i, j, d)

            pair1 = (self._puzzle.get_row(i), self._puzzle.get_row_constraint(i))
            pair2 = (self._puzzle.get_column(j), self._puzzle.get_column_constraint(j))
            for row_or_column, constraint in (pair1, pair2):
                if any(tile is None for tile in row_or_column):
                    continue
                if not satisfies_constraint(row_or_column, constraint):
                    break
            else:
                self.backtrack(level + 1)

        self._puzzle.set_tile(i, j, None)
        return

    def _get_unassigned_variable(self):
        '''(CSPSolver) -> (int, int)
        Return a pair of indeces indicating an unassigned variable/tile in the puzzle/grid.
        If no such pair exists, return None.
        '''
        for i in range(self._puzzle.get_num_rows()):
            for j in range(self._puzzle.get_num_columns()):
                if self._puzzle.get_tile(i, j) is None:
                    return i, j
        return None

class PuzzleSolvedException(Exception):
    pass
