#!/usr/bin/python3

from color import *

def read_hints(file_name):
    '''(str) -> ([[int]], [[int]])
    Read the hints in the file into two lists: one for rows and one for
    columns. Each entry in the lists is itself a list containing the 'hints'
    for a particular row or column. See the examples for what the file format
    looks like.

    Raises an exception if the file isn't in the expected format.

    The island sizes in the hints can't be negative; and any island sizes
    equal to 0 will be ignored. Thus, use a hint containing the single island
    size "0" to notate a completely blank
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

    return row_hints, col_hints

def read_grid(file_name):
    '''(str) -> [[Color]]
    Read a solution grid from a file.
    See the examples for what the file format looks like.

    Grids should look like something like this:
    -###------
    -#-#--##--
    ####---##-
    --##----##
    --########
    --###---##
    --###--##-
    ---#####--
    ------#---
    ----####--
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

    # Ignore trailing newlines.
    while len(grid) > 0 and grid[-1] == []:
        grid.pop()

    # Ensure non-jagged grid.
    if is_jagged(grid):
        raise Exception('Jagged grid.')

    return grid

def hints_to_str(row_hints, col_hints):
    '''([[int]], [[int]]) -> str
    Echo the hints to a string in the same format that is read by read_hints().

    >>> hints_to_str([[2], [1, 1], []], [[2], [1], [1]])
    '2\\n1 1\\n0\\n\\n2\\n1\\n1\\n'
    '''
    s = ''
    for hints in (row_hints, col_hints):
        for hint in hints:
            if len(hint) == 0:
                s += '0'
            else:
                s += ' '.join(str(island) for island in hint)
            s += '\n'
        s += '\n'
    s = s[:-1]

    return s

def write_hints(row_hints, col_hints, file_name):
    '''([[int]], [[int]], str)
    Write the hints to a file in the same format that is read by read_hints().
    '''
    file = open(file_name, 'w')
    file.write(hints_to_str(row_hints, col_hints))
    file.close()

def grid_to_str(grid):
    '''([[Color]]) -> str
    Echo the grid to a string in the same format that is read by read_grid().

    >>> w, b, n = Color.white, Color.black, Color.none
    >>> grid_to_str([[b, b, w], [n, n, b], [w, w, n]])
    '##-\\n??#\\n--?\\n'
    '''
    s = ''
    for row in grid:
        for tile in row:
            s += str(tile)
        s += '\n'
    return s

def write_grid(grid, file_name):
    '''([[Color]], str)
    Write the grid to a file in the same format that is read by read_grid().
    '''
    file = open(file_name, 'w')
    file.write(grid_to_str(grid))
    file.close()

if __name__ == '__main__':
    import doctest
    doctest.testmod()
