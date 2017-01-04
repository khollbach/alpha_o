#!/usr/bin/python3

import sys
sys.path.insert(0, '../main')

from csp_solver import *
from file_io import *

example = '../../examples/problems/problem1.txt'

def main():
    '''
    Visually test CSP var-selection heuristic initialization.
    '''
    print('Using: ' + example)
    row_hints, col_hints = read_hints(example)
    puzzle = Puzzle(row_hints, col_hints)

    print('Grid after init:')
    print(puzzle, end='')

    print('Fullness stats:')
    print('Rows:')
    for num in puzzle.row_fullness:
        print(num, end=' ')
    print()
    print('Cols:')
    for num in puzzle.col_fullness:
        print(num, end=' ')
    print()

if __name__ == '__main__':
    main()
