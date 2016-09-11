from enum import Enum

class Color(Enum):
    '''
    Represents the colors a tile can be: none (unknown), white, or black.
    '''
    none = 0
    white = 1
    black = 2

    def __str__(self):
        '''(Color) -> str
        Print a single-character representation of the color.

        >>> str(Color.none)
        '?'
        >>> str(Color.white)
        '-'
        >>> str(Color.black)
        '#'
        '''
        if self == Color.none:
            return '?'
        elif self == Color.white:
            return '-'
        elif self == Color.black:
            return '#'

def parse_color(s):
    '''(str) -> Color
    Read a single-character string, returning either a Color.
    Specifically: '?' ==> none, '-' ==> white, '#' ==> black.
    Raises an Exception on any other input.

    >>> parse_color('?') == Color.none
    True
    >>> parse_color('-') == Color.white
    True
    >>> parse_color('#') == Color.black
    True
    '''
    if s == '?':
        return Color.none
    elif s == '-':
        return Color.white
    elif s == '#':
        return Color.black
    else:
        raise Exception('Not a color.')

if __name__ == '__main__':
    import doctest
    doctest.testmod()
