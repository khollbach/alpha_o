WHITE = 0
BLACK = 1

def satisfies_constraint(row_or_column, expected_blocks):
    '''([WHITE|BLACK, ...], [int, ...]) -> bool
    Return True iff the row or column has a coloring that agrees with the 'hint'.
    '''
    blocks = []

    current_block_size = 0
    for square in row_or_column:
        if square == WHITE:
            if current_block_size > 0:
                blocks.append(current_block_size)
            current_block_size = 0
        elif square == BLACK:
            current_block_size += 1
    if current_block_size > 0:
        blocks.append(current_block_size)

    return blocks == expected_blocks

def satisfies_row_constraint(board, row_index, expected_blocks):
    '''([[WHITE|BLACK, ...], ...], int, [int, ...]) -> bool
    Return True iff the row has a coloring that agrees with the 'hint'.
    '''
    row = board[row_index]
    return satisfies_constraint(board[row_index], expected_blocks)

def satisfies_column_constraint(board, column_index, expected_blocks):
    '''([[WHITE|BLACK, ...], ...], int, [int, ...]) -> bool
    Return True iff the column has a coloring that agrees with the 'hint'.
    '''
    column = [board[i][column_index] for i in range(len(board))]
    return satisfies_constraint(column, expected_blocks)
