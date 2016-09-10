from puzzle import *
from file_io import *

import sys

def test(problemfile, solutionfile):
    '''(str, str)
    Run a few sanity checks.
    '''
    r, c = read_hints(problemfile)
    g = read_grid(solutionfile)
    puzzle = Puzzle(r, c, g)

    for n in range(puzzle.get_num_rows()):
        for c in puzzle.get_row(n):
            print(c, end='')
        print()

    print()

    for n in range(puzzle.get_num_columns()):
        for c in puzzle.get_column(n):
            print(c, end='')
        print()

    print()

    for n in range(puzzle.get_num_rows()):
        if not satisfies_constraint(puzzle.get_row(n), puzzle.get_row_constraint(n)):
            print('Bad row:', n)

    for n in range(puzzle.get_num_columns()):
        if not satisfies_constraint(puzzle.get_column(n), puzzle.get_column_constraint(n)):
            print('Bad column:', n)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: expects filename')
        sys.exit(1)
        
    filename = sys.argv[1]
    test('../examples/problems/' + filename, '../examples/solutions/' + filename)
