from Color import *

def read_hints(file_name):
    '''(str) -> ([[int, ...], ...], [[int, ...], ...])
    Read the hints in the file into two lists: one for rows and one for columns.
    Each entry in the lists is itself a list containing the hints for a particular row or column.
    See the examples for what the file format looks like.
    '''
    file = open(file_name)

    row_hints = []
    column_hints = []

    blank_lines_seen = 0
    for line in file:
        line = line.strip()

        if line == '':
            blank_lines_seen += 1
        else:
            if blank_lines_seen == 0:
                row_hints.append([int(x) for x in line.split()])
            elif blank_lines_seen == 1:
                column_hints.append([int(x) for x in line.split()])
            else:
                raise Exception('Bad file format.')

    file.close()

    return row_hints, column_hints

def read_grid(file_name):
    '''(str) -> [[Color, ...], ...]
    Read a solution grid from a file.
    See the examples for what the file format looks like.
    '''
    file = open(file_name)

    grid = []
    for line in file:
        line = line.strip('\n')

        row = []
        for char in line:
            row.append(parse_color(char))

        grid.append(row)

    file.close()

    return grid
