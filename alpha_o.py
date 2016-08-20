from file_io import *
from Puzzle import *
from puzzle_logic import *

def main():
    row_hints, column_hints = read_hints('examples/problem1.txt')
    grid = read_grid('examples/solution1.txt')

    puzzle = Puzzle(row_hints, column_hints, grid)

    for i in range(puzzle.get_num_rows()):
        if not satisfies_constraint(puzzle.get_row(i), row_hints[i]):
            print('row', i, "doesn't work.")

    for j in range(puzzle.get_num_columns()):
        if not satisfies_constraint(puzzle.get_column(j), column_hints[j]):
            print('column', j, "doesn't work.")

    file = open('tmp.txt', 'w')
    print(puzzle, file=file)
    file.close()

if __name__ == '__main__':
    main()
