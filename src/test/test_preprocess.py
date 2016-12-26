#!/usr/bin/python3

import sys
sys.path.insert(0, '../main')

from color import *
from file_io import *
from preprocess import *

def main():
    '''
    Visually test the preprocess() function
    '''
    row_hints, col_hints = read_hints('../../examples/problems/problem1.txt')

    rows = []
    for hint in row_hints:
        rows.append(line_solve(hint, len(col_hints)))
    for r in range(len(row_hints)):
        for c in range(len(col_hints)):
            print(rows[r][c], end='')
        print()

    print()

    cols = []
    for hint in col_hints:
        cols.append(line_solve(hint, len(row_hints)))
    for r in range(len(row_hints)):
        for c in range(len(col_hints)):
            print(cols[c][r], end='')
        print()

    print()

    grid = preprocess(row_hints, col_hints)

    print(grid_to_str(grid))

if __name__ == '__main__':
    main()
