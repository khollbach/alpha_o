from enum import Enum

class Color(Enum):
    '''
    Represents the colors a tile can be: white or black.
    An unknown color of tile can be represented with None instead of using a Color object.
    '''

    white = 0
    black = 1

    def __str__(self):
        '''(Color) -> str
        Print a single-character representation of the color.
        '''
        if self == Color.white:
            return '-'
        elif self == Color.black:
            return '#'

def parse_color(s):
    '''(str) -> Color
    Read a single-character string, returning either a color or None, depending on if the character
    is a known representation of a color.
    Specifically: '-' ==> white, '#' ==> black. Anything else ==> None.
    '''
    if s == '-':
        return Color.white
    elif s == '#':
        return Color.black
    else:
        return None