class OthelloCell:
    def __init__(self, color):
        self._color = color

    @property
    def color(self):
        return self._color.lower()

    def __str__(self):
        return self._color[0].upper()

    def __repr__(self):
        return 'Cell<{}>'.format(self._color.lower())

    def __eq__(self, other):
        return self.__class__ == other.__class__ and \
                self._color == other._color

class BlackCell(OthelloCell):
    def __init__(self):
        OthelloCell.__init__(self, 'Black')

class WhiteCell(OthelloCell):
    def __init__(self):
        OthelloCell.__init__(self, 'White')

class UndefCell(OthelloCell):
    def __init__(self):
        OthelloCell.__init__(self, 'Undef')

    def __str__(self):
        return '.'

BLACK = BlackCell()
WHITE = WhiteCell()
UNDEF = UndefCell()

class Othello:
    def __init__(self, size=(8, 8)):
        self._size = size
        self._mat = [[UNDEF for i in range(size[1])] for j in range(size[0])]

        self._mat[size[0]//2 - 1][size[1]//2 - 1] = WHITE
        self._mat[size[0]//2 - 1][size[1]//2] = BLACK
        self._mat[size[0]//2][size[1]//2 - 1] = BLACK
        self._mat[size[0]//2][size[1]//2] = WHITE

    @property
    def mat(self):
        return self._mat
