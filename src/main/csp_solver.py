#!/usr/bin/python3

from color import *
from puzzle import *

def backtrack(puzzle, level=0):
    '''(Puzzle, int) -> None
    Runs a backtracking algorithm on the puzzle.
    Throws a PuzzleSolvedException if solved, returns normally if no
    solutions.
    '''
    v = get_unassigned_variable2(puzzle)
    if v is None:
        raise PuzzleSolvedException('Nice!')
    i, j = v

    for d in (Color.white, Color.black):
        puzzle.set(i, j, d)

        row = [puzzle.get(i, x) for x in range(puzzle.num_cols)]
        row_hint = puzzle.row_hints[i]

        col = [puzzle.get(x, j) for x in range(puzzle.num_rows)]
        col_hint = puzzle.col_hints[j]

        for row_or_col, hint in ((row, row_hint), (col, col_hint)):
            if any(tile == Color.none for tile in row_or_col):
                continue
            if not satisfies_hint(row_or_col, hint):
                break
        else:
            backtrack(puzzle, level + 1)

    puzzle.set(i, j, Color.none)
    return

def get_unassigned_variable(puzzle):
    '''(Puzzle) -> (int, int)
    Return a pair of indeces indicating an unassigned variable/tile in the
    puzzle/grid. If no such pair exists, return None.
    '''
    for i in range(puzzle.num_rows):
        for j in range(puzzle.num_cols):
            if puzzle.get(i, j) == Color.none:
                return i, j
    return None

def get_unassigned_variable2(puzzle):
    '''(Puzzle) -> (int, int)
    Return a pair of indeces indicating an unassigned variable/tile in the
    puzzle/grid. If no such pair exists, return None.

    Uses the heuristic of most tiles filled in a row/column.
    '''
    best_row_idx = None
    max_row_fullness = -1
    for i, fullness in enumerate(puzzle.row_fullness):
        if fullness < puzzle.num_cols and fullness > max_row_fullness:
            best_row_idx = i
            max_row_fullness = fullness

    best_col_idx = None
    max_col_fullness = -1
    for j, fullness in enumerate(puzzle.col_fullness):
        if fullness < puzzle.num_rows and fullness > max_col_fullness:
            best_col_idx = j
            max_col_fullness = fullness

    if max_row_fullness == -1 and max_col_fullness == -1:
        return None

    if max_row_fullness > max_col_fullness:
        for j in range(puzzle.num_cols):
            if puzzle.get(best_row_idx, j) == Color.none:
                return best_row_idx, j
        assert False
    else:
        for i in range(puzzle.num_rows):
            if puzzle.get(i, best_col_idx) == Color.none:
                return i, best_col_idx
        assert False

class PuzzleSolvedException(Exception):
    pass
