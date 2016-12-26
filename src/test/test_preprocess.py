#!/usr/bin/python3

import sys
sys.path.insert(0, '../main')

from color import *
from file_io import *
from preprocess import *

example = '../../examples/problems/problem1.txt'

def main():
    '''
    Visually test the preprocess() function.
    '''
    print('Using: ' + example)
    row_hints, col_hints = read_hints(example)

    print('Column line-solving:')
    rows = []
    for hint in row_hints:
        rows.append(line_solve(hint, len(col_hints)))
    for r in range(len(row_hints)):
        for c in range(len(col_hints)):
            print(rows[r][c], end='')
        print()

    print('Row line-solving:')
    cols = []
    for hint in col_hints:
        cols.append(line_solve(hint, len(row_hints)))
    for r in range(len(row_hints)):
        for c in range(len(col_hints)):
            print(cols[c][r], end='')
        print()

    print('All preprocessing: (both row and col)')
    grid = preprocess(row_hints, col_hints)
    print(grid_to_str(grid))

if __name__ == '__main__':
    main()
