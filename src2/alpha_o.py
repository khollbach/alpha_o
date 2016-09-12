from file_io import *
from puzzle import *
from csp_solver import *

import sys
from datetime import datetime

def main(argv):
    row_hints, column_hints = read_hints(argv[1])

    puzzle = Puzzle(row_hints, column_hints)

    solver = CSPSolver(puzzle)

    print(datetime.now())
    
    try:
        solver.backtrack()
        print('No solution found.')
    except PuzzleSolvedException:
        print('Writing solution to tmp.txt ...', end='')
        file = open('tmp.txt', 'w')
        file.write(str(puzzle))
        file.close()
        print('done.')
    
    print(datetime.now())
    
if __name__ == '__main__':
    main(sys.argv)