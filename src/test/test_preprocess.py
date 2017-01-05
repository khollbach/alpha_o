#!/usr/bin/python3

import sys
sys.path.insert(0, '../main')

from color import *
from file_io import *
from puzzle import *
from preprocess import *

example = '../../examples/problem1.txt'

def main():
    '''
    Visually test the preprocess() function.
    '''
    print('Using: ' + example)
    row_hints, col_hints = read_hints(example)
    num_rows, num_cols = len(row_hints), len(col_hints)

    print('Row line-solving:')
    rows = [line_solve(hint, num_cols) for hint in row_hints]
    for i in range(num_rows):
        for j in range(num_cols):
            print(rows[i][j], end='')
        print()

    print('Column line-solving:')
    cols = [line_solve(hint, num_rows) for hint in col_hints]
    for i in range(num_rows):
        for j in range(num_cols):
            print(cols[j][i], end='')
        print()

    print('All preprocessing: (both row and col)')
    puzzle = Puzzle(row_hints, col_hints)
    print(puzzle, end='')

if __name__ == '__main__':
    main()
