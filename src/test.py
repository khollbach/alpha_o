from puzzle import *
from file_io import *

def test(problemfile, solutionfile):
    '''(str, str)
    Run a few sanity checks.
    '''
    r, c = read_constraints(problemfile)
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
    test('../examples/problems/problem4.txt', '../examples/solutions/problem4.txt')
