from file_io import *
from puzzle_logic import *

def main():
    row_hints, column_hints = read_hints('examples/problem1.txt')

    print(row_hints)
    print(column_hints)

    board = read_solution('examples/solution1.txt')

    print(board)

    for i in range(len(board)):
        if not satisfies_row_constraint(board, i, row_hints[i]):
            print('row', i, "doesn't match.")

    for j in range(len(board[0])):
        if not satisfies_column_constraint(board, j, column_hints[j]):
            print('column', j, "doesn't match.")

    write_solution(board, 'tmp.txt')

if __name__ == '__main__':
    main()
