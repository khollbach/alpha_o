from Color import *

def satisfies_constraint(row_or_column, expected_blocks):
    '''([Color, ...], [int, ...]) -> bool
    Return True iff the row or column has a coloring that agrees with the 'hint'.
    '''
    blocks = []

    current_block_size = 0
    for tile in row_or_column:
        if tile == Color.white:
            if current_block_size > 0:
                blocks.append(current_block_size)
            current_block_size = 0
        elif tile == Color.black:
            current_block_size += 1
        else:
            return False
    if current_block_size > 0:
        blocks.append(current_block_size)

    return blocks == expected_blocks
