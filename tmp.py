from puzzle import *
from file_io import *

r, c = read_constraints('examples/problem4.txt')
g = read_grid('examples/solution4.txt')

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
