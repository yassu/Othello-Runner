from sys import path
path.append('src')
from othello import (
    OthelloCell, BlackCell, WhiteCell, UndefCell,
    WHITE, BLACK, UNDEF,
    Othello, OthelloIter,
    Player,
    s_ind_to_ind)

from unittest import TestCase
from nose.tools import raises


class OthelloCellTestCase(TestCase):

    def setUp(self):
        self.cell = OthelloCell('Red')

    def color_test(self):
        assert(self.cell.color == 'red')

    def str_test(self):
        assert(str(self.cell) == 'R')

    def repr_test(self):
        assert(repr(self.cell) == 'Cell<red>')

    def other_color_test(self):
        cell = OthelloCell('Black')
        assert(cell.other_color == WHITE)

    def other_color_test2(self):
        cell = OthelloCell('White')
        assert(cell.other_color == BLACK)

    def eq_test(self):
        assert(self.cell == OthelloCell('RED'))

    def eq_test2(self):
        assert(self.cell != OthelloCell('ReBlack'))


class BlackCellTestCase(TestCase):

    def setUp(self):
        self.black_cell = BlackCell()

    def str_test(self):
        assert(str(self.black_cell) == 'B')

    def repr_test(self):
        assert(repr(self.black_cell) == 'Cell<black>')

    def eq_test(self):
        assert(self.black_cell == BlackCell())
        assert(self.black_cell != WhiteCell())
        assert(self.black_cell != UndefCell())


class WhiteCellTestCase(TestCase):

    def setUp(self):
        self.white_cell = WhiteCell()

    def str_test(self):
        assert(str(self.white_cell) == 'W')

    def repr_test(self):
        assert(repr(self.white_cell) == 'Cell<white>')

    def eq_test(self):
        assert(self.white_cell != BlackCell())
        assert(self.white_cell == WhiteCell())
        assert(self.white_cell != UndefCell())


class UndefCellTestCase(TestCase):

    def setUp(self):
        self.undef_cell = UndefCell()

    def str_test(self):
        assert(str(self.undef_cell) == '.')

    def repr_test(self):
        assert(repr(self.undef_cell) == 'Cell<undef>')

    def eq_test(self):
        assert(self.undef_cell != BlackCell())
        assert(self.undef_cell != WhiteCell())
        assert(self.undef_cell == UndefCell())


class OthelloTestCase(TestCase):

    def setUp(self):
        self.othello = Othello()

    def init_test(self):
        assert(self.othello[3][3] == WHITE)
        assert(self.othello[3][4] == BLACK)
        assert(self.othello[4][3] == BLACK)
        assert(self.othello[4][4] == WHITE)
        assert(self.othello[2][3] == UNDEF)
        assert(self.othello[5][3] == UNDEF)
        assert(self.othello[3][2] == UNDEF)
        assert(self.othello[3][5] == UNDEF)

    def filled_test(self):
        assert(self.othello.filled() is False)

    def filled_test2(self):
        for i in range(8):
            for j in range(8):
                self.othello._mat[i][j] = BLACK
        assert(self.othello.filled() is True)

    def count_test(self):
        assert(self.othello.count(WHITE) == 2)
        assert(self.othello.count(BLACK) == 2)

    def count_test2(self):
        self.othello.put((3, 2), BLACK)
        assert(self.othello.count(BLACK) == 4)

    def puttable_test(self):
        assert(self.othello.puttable((3, 3), WHITE) is False)

    def puttable_test2(self):
        assert(self.othello.puttable((3, 2), BLACK) is True)
        assert(self.othello.puttable((3, 2), WHITE) is False)

    def puttable_test3(self):
        assert(self.othello.puttable((3, 5), WHITE) is True)
        assert(self.othello.puttable((3, 5), BLACK) is False)

    def puttable_test4(self):
        assert(self.othello.puttable((2, 3), BLACK) is True)
        assert(self.othello.puttable((2, 3), WHITE) is False)

    def puttable_test5(self):
        assert(self.othello.puttable((5, 3), WHITE) is True)
        assert(self.othello.puttable((5, 3), BLACK) is False)

    def puttable_test6(self):
        self.othello._mat[3][3] = BLACK
        assert(self.othello.puttable((2, 2), WHITE) is True)

    def puttable_test7(self):
        self.othello._mat[3][4] = WHITE
        assert(self.othello.puttable((2, 5), BLACK) is True)
        self.othello._mat[3][4] = BLACK

    def puttable_test8(self):
        self.othello._mat[4][3] = WHITE
        assert(self.othello.puttable((5, 2), BLACK) is True)
        self.othello._mat[4][3] = BLACK

    def puttable_test9(self):
        self.othello._mat[4][4] = BLACK
        assert(self.othello.puttable((5, 5), WHITE) is True)
        self.othello._mat[4][4] = WHITE

    def puttable_somewhere_test(self):
        assert(self.othello.puttable_somewhere(WHITE) is True)

    def puttable_somewhere_test2(self):
        for i in range(8):
            for j in range(8):
                self.othello._mat[i][j] = BLACK
        assert(self.othello.puttable_somewhere(BLACK) is False)
        assert(self.othello.puttable_somewhere(WHITE) is False)

    def puttable_somewhere_test3(self):
        for i in range(8):
            for j in range(8):
                self.othello._mat[i][j] = BLACK
        self.othello._mat[0][0] = UNDEF
        self.othello._mat[0][3] = WHITE
        assert(self.othello.puttable_somewhere(BLACK) is False)
        assert(self.othello.puttable_somewhere(WHITE) is True)

    @raises(ValueError)
    def put_test(self):
        self.othello.put((0, 0), BLACK)

    def put_test2(self):
        self.othello.put((3, 2), BLACK)
        assert(self.othello[3][3] == BLACK)
        assert(self.othello[3][2] == BLACK)

    def put_test3(self):
        self.othello.put((3, 5), WHITE)
        assert(self.othello[3][4] == WHITE)
        assert(self.othello[3][5] == WHITE)

    def put_test4(self):
        self.othello.put((2, 3), BLACK)
        assert(self.othello[2][3] == BLACK)
        assert(self.othello[3][3] == BLACK)

    def put_test5(self):
        self.othello.put((5, 3), WHITE)
        assert(self.othello[5][3] == WHITE)
        assert(self.othello[4][3] == WHITE)

    def put_test6(self):
        self.othello.put((2, 3), BLACK)
        self.othello.put((2, 2), WHITE)
        assert(self.othello[3][3] == WHITE)

    def put_test7(self):
        self.othello.put((2, 4), WHITE)
        self.othello.put((2, 5), BLACK)
        assert(self.othello[2][5] == BLACK)
        assert(self.othello[3][4] == BLACK)

    def put_test8(self):
        self.othello.put((5, 3), WHITE)
        self.othello.put((5, 2), BLACK)
        assert(self.othello[5][2] == BLACK)
        assert(self.othello[4][3] == BLACK)

    def put_test9(self):
        self.othello.put((5, 4), BLACK)
        self.othello.put((5, 5), WHITE)
        assert(self.othello[5][5] == WHITE)
        assert(self.othello[4][4] == WHITE)

    def pritty_str_test(self):
        assert(self.othello.pritty_str() == (
            "  01234567\n"
            "0 ........\n"
            "1 ........\n"
            "2 ........\n"
            "3 ...WB...\n"
            "4 ...BW...\n"
            "5 ........\n"
            "6 ........\n"
            "7 ........\n"
        ))

    def pritty_str_test2(self):
        self.othello.put((5, 4), BLACK)
        assert(self.othello.pritty_str() == (
            "  01234567\n"
            "0 ........\n"
            "1 ........\n"
            "2 ........\n"
            "3 ...WB...\n"
            "4 ...BB...\n"
            "5 ....B...\n"
            "6 ........\n"
            "7 ........\n"
        ))

    def finished_test(self):
        othello = Othello()
        for i in range(8):
            for j in range(6):
                othello._mat[i][j] = BLACK
        assert(othello.finished() is True)

    def str_test(self):
        assert(str(self.othello) == (
            "........\n"
            "........\n"
            "........\n"
            "...WB...\n"
            "...BW...\n"
            "........\n"
            "........\n"
            "........\n"
        ))


class OthelloIterTestCase(TestCase):

    @raises(StopIteration)
    def iter_test(self):
        data = OthelloIter([
            ((3, 2), BLACK),
            ((2, 2), WHITE)
        ])
        othello = Othello()

        othello.put((3, 2), BLACK)
        assert(next(data) == othello)

        othello.put((2, 2), WHITE)
        assert(next(data) == othello)

        next(data)


class PlayerTestCase(TestCase):

    def setUp(self):
        self.othello = Othello()
        self.player = Player('user', self.othello, BLACK)

    def color_test(self):
        assert(self.player.color == BLACK)

    def othello_test(self):
        self.player.othello == self.othello

    def get_next_move_test(self):
        assert(self.player.get_next_move(in_=lambda: '1, 2') == (1, 2))

    @raises(ValueError)
    def get_next_move_test2(self):
        self.player.get_next_move(in_=lambda: 'ab, def')

    @raises(ValueError)
    def get_next_move_test3(self):
        self.player.get_next_move(in_=lambda: 'abcdef')

    def puttable_test(self):
        assert(self.player.puttable((2, 3)) is True)

    @raises(ValueError)
    def put_test(self):
        self.player.put((0, 0))

    def put_test2(self):
        self.player.put((3, 2))
        assert(self.othello[3][3] == BLACK)
        assert(self.othello[3][2] == BLACK)

    def win_test(self):
        assert(self.player.win() is False)

    def win_test2(self):
        for i in range(4):
            for j in range(8):
                self.othello._mat[i][j] = BLACK

        for i in range(4, 8):
            for j in range(8):
                self.othello._mat[i][j] = WHITE
        assert(self.player.win() is False)

    def win_test3(self):
        for i in range(4):
            for j in range(8):
                self.othello._mat[i][j] = BLACK

        for i in range(4, 8):
            for j in range(8):
                self.othello._mat[i][j] = WHITE
        self.othello._mat[7][7] = BLACK

        assert(self.player.win() is True)

    def win_test4(self):
        for i in range(4):
            for j in range(8):
                self.othello._mat[i][j] = BLACK

        for i in range(4, 8):
            for j in range(8):
                self.othello._mat[i][j] = WHITE
        self.othello._mat[3][3] = WHITE
        assert(self.player.win() is False)

    def win_test5(self):
        for i in range(4):
            for j in range(8):
                self.othello._mat[i][j] = BLACK

        for i in range(4, 8):
            for j in range(7):
                self.othello._mat[i][j] = BLACK

        assert(self.player.win() is True)

    def draw_test(self):
        assert(self.player.draw() is False)

    def draw_test2(self):
        for i in range(4):
            for j in range(8):
                self.othello._mat[i][j] = BLACK

        for i in range(4, 8):
            for j in range(8):
                self.othello._mat[i][j] = WHITE
        assert(self.player.draw() is True)

    def draw_test3(self):
        for i in range(4):
            for j in range(8):
                self.othello._mat[i][j] = BLACK

        for i in range(4, 8):
            for j in range(8):
                self.othello._mat[i][j] = WHITE
        self.othello._mat[7][7] = BLACK

        assert(self.player.draw() is False)

    def draw_test4(self):
        for i in range(4):
            for j in range(8):
                self.othello._mat[i][j] = BLACK

        for i in range(4, 8):
            for j in range(8):
                self.othello._mat[i][j] = WHITE
        self.othello._mat[3][3] = WHITE
        assert(self.player.draw() is False)

    def lost_test(self):
        assert(self.player.lost() is False)

    def lost_test2(self):
        for i in range(4):
            for j in range(8):
                self.othello._mat[i][j] = BLACK

        for i in range(4, 8):
            for j in range(8):
                self.othello._mat[i][j] = WHITE

    def lost_test3(self):
        for i in range(4):
            for j in range(8):
                self.othello._mat[i][j] = BLACK

        for i in range(4, 8):
            for j in range(8):
                self.othello._mat[i][j] = WHITE
        self.othello._mat[7][7] = BLACK

        assert(self.player.lost() is False)

    def lost_test4(self):
        for i in range(4):
            for j in range(8):
                self.othello._mat[i][j] = BLACK

        for i in range(4, 8):
            for j in range(8):
                self.othello._mat[i][j] = WHITE
        self.othello._mat[3][3] = WHITE
        assert(self.player.lost() is True)

    def lost_test5(self):
        for i in range(8):
            for j in range(7):
                self.othello._mat[i][j] = WHITE
        assert(self.player.lost() is True)


def s_ind_to_ind_test():
    assert(s_ind_to_ind('  1 ,  3 ') == (1, 3))


@raises(ValueError)
def s_ind_to_ind_test2():
    s_ind_to_ind('ab, def')


@raises(ValueError)
def s_ind_to_ind_test3():
    s_ind_to_ind('abcdef')
