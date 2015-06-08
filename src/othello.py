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
                self.color == other.color

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

        self._mat[size[1]//2 - 1][size[0]//2 - 1] = WHITE
        self._mat[size[1]//2 - 1][size[0]//2] = BLACK
        self._mat[size[1]//2][size[0]//2 - 1] = BLACK
        self._mat[size[1]//2][size[0]//2] = WHITE

    @property
    def mat(self):
        return self._mat

    @property
    def size(self):
        return self._size

    def count(self, color):
        return [cell for row in self.mat for cell in row].count(color)

    def puttable(self, ind, color):
        mat = self.mat
        i, j = ind

        if self.mat[i][j] != UNDEF:
            return False

        j += 1
        while j < self.size[0]:
            if j == ind[1] + 1 and mat[i][j] == color:
                break
            elif mat[i][j] == UNDEF:
                break
            elif mat[i][j] == color:
                return True
            j += 1
        j = ind[1]

        j -= 1
        while j >= 0:
            if j == ind[1] - 1 and mat[i][j] == color:
                break
            elif mat[i][j] == UNDEF:
                break
            elif mat[i][j] == color:
                return True
            j -= 1
        j = ind[1]

        i += 1
        while i < self.size[1]:
            if i == ind[0] + 1 and mat[i][j] == color:
                break
            elif mat[i][j] == UNDEF:
                break
            elif mat[i][j] == color:
                return True
            i += 1
        i = ind[0]

        i -= 1
        while i >= 0:
            if i == ind[0] - 1 and mat[i][j] == color:
                break
            elif mat[i][j] == UNDEF:
                break
            elif mat[i][j] == color:
                return True
            i -= 1
        i = ind[0]

        i += 1
        j += 1
        while i < self.size[0] and j < self.size[1]:
            if i == ind[0] + 1 and mat[i][j] == color:
                break
            elif mat[i][j] == UNDEF:
                break
            elif mat[i][j] == color:
                return True
            i += 1
            j += 1
        i = ind[0]
        j = ind[1]

        i += 1
        j -= 1
        while i < self.size[0] and j >= 0:
            if i == ind[0] + 1 and mat[i][j] == color:
                break
            elif mat[i][j] == UNDEF:
                break
            elif mat[i][j] == color:
                return True
            i += 1
            j -= 1
        i = ind[0]
        j = ind[1]

        i -= 1
        j += 1
        while i >= 0 and j < self.size[1]:
            if i == ind[0] - 1 and mat[i][j] == color:
                break
            elif mat[i][j] == UNDEF:
                break
            elif mat[i][j] == color:
                return True
            i -= 1
            j += 1
        i = ind[0]
        j = ind[1]

        i -= 1
        j -= 1
        while i >= 0 and j >= 0:
            if i == ind[0] - 1 and mat[i][j] == color:
                break
            elif mat[i][j] == UNDEF:
                break
            elif mat[i][j] == color:
                return True
            i -= 1
            j -= 1
        i = ind[0]
        j = ind[1]

        return False

    def put(self, ind, color):
        if not self.puttable(ind, color):
            raise ValueError("Can't at ({}, [}.)".format(ind[0], ind[1]))

        mat = self.mat
        i, j = ind

        j += 1
        while j < self.size[0]:
            if j == ind[1] + 1 and mat[i][j] == color:
                break
            elif mat[i][j] == UNDEF:
                break
            elif mat[i][j] == color:
                for l in range(ind[1], j + 1):
                    mat[i][l] = color
            j += 1
        j = ind[1]

        j -= 1
        while j >= 0:
            if j == ind[1] - 1 and mat[i][j] == color:
                break
            elif mat[i][j] == UNDEF:
                break
            elif mat[i][j] == color:
                for l in range(j, ind[1] + 1):
                    mat[i][l] = color
            j -= 1
        j = ind[1]

        i += 1
        while i < self.size[1]:
            if i == ind[0] + 1 and mat[i][j] == color:
                break
            elif mat[i][j] == UNDEF:
                break
            elif mat[i][j] == color:
                for k in range(ind[0], i + 1):
                    mat[k][j] = color
            i += 1
        i = ind[0]

        i -= 1
        while i >= 0:
            if i == ind[0] - 1 and mat[i][j] == color:
                break
            elif mat[i][j] == UNDEF:
                break
            elif mat[i][j] == color:
                for k in range(i, ind[0] + 1):
                    mat[k][j] = color
            i -= 1
        i = ind[0]

        i += 1
        j += 1
        while i < self.size[0] and j < self.size[1]:
            if i == ind[0] + 1 and mat[i][j] == color:
                break
            elif mat[i][j] == UNDEF:
                break
            elif mat[i][j] == color:
                for k in range(i - ind[0] + 1):
                    mat[ind[0] + k][ind[1] + k] = color
            i += 1
            j += 1
        i = ind[0]
        j = ind[1]

        i += 1
        j -= 1
        while i < self.size[0] and j >= 0:
            if i == ind[0] + 1 and mat[i][j] == color:
                break
            elif mat[i][j] == UNDEF:
                break
            elif mat[i][j] == color:
                for k in range(i - ind[0] + 1):
                    mat[ind[0] + k][ind[1] - k] = color
            i += 1
            j -= 1
        i = ind[0]
        j = ind[1]

        i -= 1
        j += 1
        while i >= 0 and j < self.size[1]:
            if i == ind[0] - 1 and mat[i][j] == color:
                break
            elif mat[i][j] == UNDEF:
                break
            elif mat[i][j] == color:
                for k in range(j - ind[1] + 1):
                    mat[ind[0] - k][ind[1] + k] = color
            i -= 1
            j += 1
        i, j = ind

        i -= 1
        j -= 1
        cnt = 0
        while i >= 0 and j >= 0:
            cnt += 1
            if i == ind[0] - 1 and mat[i][j] == color:
                break
            elif mat[i][j] == UNDEF:
                break
            elif mat[i][j] == color:
                for k in range(cnt + 1):
                    mat[ind[0] - k][ind[1] - k] = color
            i -= 1
            j -= 1

    def __str__(self):
        s = ""
        for row in self.mat:
            for c in row:
                s += str(c)
            s += "\n"
        return s

    def __getitem__(self, ind):
        return self.mat[ind]

class Player:
    def __init__(self, othello, color):
        self._othello = othello
        self._color = color

    @property
    def color(self):
        return self._color

    @property
    def othello(self):
        return self._othello

    def puttable(self, ind):
        return self._othello.puttable(ind, self.color)

    def put(self, ind):
        self._othello.put(ind, self.color)
