from file_io import *

def main():
    row_hints, column_hints = read_hints('problem1.txt')

    print(row_hints)
    print(column_hints)

    board = read_solution('solution1.txt')

    print(board)

    write_solution(board, 'tmp.txt')

if __name__ == '__main__':
    main()
