from enum import Enum

class Color(Enum):
    white = 0
    black = 1

    def __str__(self):
        '''(Color) -> str
        '''
        if self == Color.white:
            return '-'
        elif self == Color.black:
            return '#'

def parse_color(s):
    '''(str) -> Color
    '''
    if s == '-':
        return Color.white
    elif s == '#':
        return Color.black
    else:
        return None
