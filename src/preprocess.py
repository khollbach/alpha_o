from puzzle import *
from color import *

def preprocess(hint, length):
    '''([int], int) -> [Color]
    Compute the most tile colors for a row or column given just the hint and the length.
    This is known as line-solving and relies on the D-value and the island sizes.

    >>> w, b, n = Color.white, Color.black, None
    >>> preprocess([4, 1, 5], 15) == [n, n, n, b, n, n, n, n, n, n, b, b, n, n, n]
    True
    >>> preprocess([], 5) == [w, w, w, w, w]
    True
    >>> preprocess([4, 1, 5], 12) == [b, b, b, b, w, b, w, b, b, b, b, b]
    True
    '''
    d = d_value(hint, length)

    # Simple cases (full solutions).
    if d == length:
        return [Color.white] * length
    elif d == 0:
        row_or_col = []
        for island in hint:
            row_or_col += [Color.black] * island + [Color.white]
        row_or_col.pop()
        return row_or_col

    # TODO
    return None

if __name__ == '__main__':
    import doctest
    doctest.testmod()
