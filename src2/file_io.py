from color import *

def read_hints(file_name):
    '''(str) -> ([[int, ...], ...], [[int, ...], ...])
    Read the hints in the file into two lists: one for rows and one for columns.
    Each entry in the lists is itself a list containing the 'hints' for a particular row or column.
    See the examples for what the file format looks like.

    Raises an exception if the file isn't in the expected format.

    The island sizes in the hints can't be negative; and any island sizes equal to 0 will be
    ignored. Thus, use a hint containing the single island size "0" to notate a completely blank
    row or column.
    '''
    file = open(file_name)

    row_hints = []
    col_hints = []

    blank_lines_seen = 0
    for line in file:
        line = line.strip()

        if line == '':
            blank_lines_seen += 1
        else:
            if blank_lines_seen == 0:
                row_hints.append([int(x) for x in line.split() if int(x) != 0])
            elif blank_lines_seen == 1:
                col_hints.append([int(x) for x in line.split() if int(x) != 0])
            else:
                raise Exception('Bad file format. Too many blank lines.')

    file.close()

    # Enusure no negative numbers.
    for hints in (row_hints, col_hints):
        for hint in hints:
            for island in hint:
                if island < 0:
                    raise Exception("Island sizes can't be negative.")

    # Check consistancy of the hints. That is, the c-value can't exceed the length of the crow.
    for hint in row_hints:
        if c_value(hint) > len(col_hints):
            raise Exception('Row too tightly packed compared to the number of columns.').
    for hint in col_hints:
        if c_value(hint) > len(row_hints):
            raise Exception('Column too tightly packed compared to the number of rows.').

    return row_hints, col_hints

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
