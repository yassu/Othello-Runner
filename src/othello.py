from random import shuffle as random_shuffle
from copy import deepcopy

DEFAULT_OTHELLO_SIZE = (8, 8)


class OthelloCell:

    def __init__(self, color):
        self._color = color

    @property
    def color(self):
        return self._color.lower()

    @property
    def other_color(self):
        if self.color == 'white':
            return BLACK
        elif self.color == 'black':
            return WHITE

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

    @property
    def different_color(self):
        return WhiteCell()


class WhiteCell(OthelloCell):

    def __init__(self):
        OthelloCell.__init__(self, 'White')

    @property
    def different_color(self):
        return BlackCell()


class UndefCell(OthelloCell):

    def __init__(self):
        OthelloCell.__init__(self, 'Undef')

    def __str__(self):
        return '.'

BLACK = BlackCell()
WHITE = WhiteCell()
UNDEF = UndefCell()


class Othello:

    def __init__(self, size=DEFAULT_OTHELLO_SIZE):
        self._size = size
        self._mat = [[UNDEF for i in range(size[1])] for j in range(size[0])]

        self._mat[size[1] // 2 - 1][size[0] // 2 - 1] = WHITE
        self._mat[size[1] // 2 - 1][size[0] // 2] = BLACK
        self._mat[size[1] // 2][size[0] // 2 - 1] = BLACK
        self._mat[size[1] // 2][size[0] // 2] = WHITE

    @property
    def mat(self):
        return self._mat

    @property
    def size(self):
        return self._size

    def filled(self):
        return not (UNDEF in [cell for row in self.mat for cell in row])

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

    def puttable_inds(self, color):
        inds = set()
        for i in range(self.size[0]):
            for j in range(self.size[1]):
                if self.puttable((i, j), color):
                    inds.add((i, j))
                    print(inds)
        return inds


    def puttable_somewhere(self, color):
        for i in range(self.size[0]):
            for j in range(self.size[1]):
                if self.puttable((i, j), color):
                    return True

        return False

    def put(self, ind, color):
        if not self.puttable(ind, color):
            raise ValueError("Can't at ({}, {}.)".format(ind[0], ind[1]))

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

    def win_color(self):
        if not self.finished():
            raise ValueError('This othello not finished')

        black_cnt = self.count(BLACK)
        white_cnt = self.count(WHITE)
        if black_cnt > white_cnt:
            return BLACK
        elif black_cnt == white_cnt:
            return None
        else:   # black_cnt < white_cnt
            return WHITE

    def pritty_str(self):
        s = "  "
        s += ''.join(list(map(str, range(self.size[1])))) + "\n"
        for i in range(self.size[0]):
            s += "{} ".format(i)
            s += ''.join(list(map(str, [self.mat[i][j] for j in
                                        range(self.size[1])])))
            s += "\n"
        return s

    def finished(self):
        return not self.puttable_somewhere(BLACK) and \
            not self.puttable_somewhere(WHITE)

    def __str__(self):
        s = ""
        for row in self.mat:
            for c in row:
                s += str(c)
            s += "\n"
        return s

    def __eq__(self, other):
        return self.mat == other.mat

    def __getitem__(self, ind):
        return self.mat[ind]


class OthelloIter:

    def __init__(self, othello_data):
        self._data = deepcopy(othello_data)
        self._othello = Othello()

    @property
    def data(self):
        return self._data

    def __iter__(self):
        return self

    def next(self):
        if len(self._data) == 0:
            raise StopIteration()

        ind, color = self._data[0]
        del(self._data[0])
        self._othello.put(ind, color)
        return self._othello


class Player:

    def __init__(self, name, othello, color):
        self._name = name
        self._othello = othello
        self._color = color

    @property
    def name(self):
        return self._name

    @property
    def color(self):
        return self._color

    @property
    def othello(self):
        return self._othello

    def get_next_move(self, in_=raw_input):
        print('{} input:'.format(self.name))
        ind = s_ind_to_ind(in_())
        return ind

    def puttable(self, ind):
        return self._othello.puttable(ind, self.color)

    def puttable_somewhere(self):
        return self.othello.puttable_somewhere(self.color)

    def put(self, ind):
        self._othello.put(ind, self.color)

    def win(self):
        othello = self.othello
        return othello.finished() and \
            othello.count(self.color) > round(
                othello.size[0] * othello.size[1] // 2)

    def draw(self):
        othello = self.othello
        return othello.finished() and \
            othello.count(self.color) == round(
            othello.size[0] * othello.size[1] // 2)

    def lost(self):
        othello = self.othello
        return othello.finished() and \
            othello.count(self.color) < round(
                othello.size[0] * othello.size[1] // 2)


def s_ind_to_ind(s_ind):
    s_ind = s_ind.replace(' ', '')
    first, second = s_ind.split(',')
    return int(first), int(second)


class CuiRunner:

    def main(self):
        ary = ['BLACK', 'WHITE']
        s_color_to_color = {'BLACK': BLACK, 'WHITE': WHITE}
        random_shuffle(ary)
        color1, color2 = ary
        print('Your color is {}.'.format(color1))

        color1 = s_color_to_color[color1]
        color2 = s_color_to_color[color2]
        othello = Othello()

        if color1 == BLACK:
            first_player = Player('player1', othello, color1)
            user = first_player
            second_player = Player('player2', othello, color2)
        else:
            first_player = Player('enemy', othello, color2)
            second_player = Player('user', othello, color1)
            user = second_player

        while not othello.filled():
            print(othello)
            ind = first_player.get_next_move()
            first_player.put(ind)

            print(othello)
            ind2 = second_player.get_next_move()
            second_player.put(ind2)

        if user.win():
            print('You Win.')
        elif user.draw():
            print('Draw.')
        else:
            print('You Lose.')

    def simulation(self, othello_iter):
        for othello in othello_iter:
            print(othello_iter)


if __name__ == '__main__':
    CuiRunner().main()
