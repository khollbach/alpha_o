from csp_solver import *
from file_io import *
from preprocess import *
from puzzle import *

import sys
from datetime import datetime

def main(argv):
    row_hints, column_hints = read_hints(argv[1])

    solver = CSPSolver(row_hints, column_hints)

    print(datetime.now())
    
    try:
        solver.backtrack()
        print('No solution found.')
    except PuzzleSolvedException:
        print(grid_to_str(solver.grid))
    
    print(datetime.now())
    
if __name__ == '__main__':
    main(sys.argv)