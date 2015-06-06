# from nose.tools import raises
from sys import path
path.append('src')
from othello import BlackCell, WhiteCell, UndefCell, Othello, WHITE, BLACK, UNDEF

from unittest import TestCase

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
        assert(self.othello.mat[3][3] == WHITE)
        assert(self.othello.mat[3][4] == BLACK)
        assert(self.othello.mat[4][3] == BLACK)
        assert(self.othello.mat[4][4] == WHITE)
        assert(self.othello.mat[2][3] == UNDEF)
        assert(self.othello.mat[5][3] == UNDEF)
        assert(self.othello.mat[3][2] == UNDEF)
        assert(self.othello.mat[3][5] == UNDEF)

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
        self.othello._mat[3][3] = WHITE

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
