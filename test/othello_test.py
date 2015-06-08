# from nose.tools import raises
from sys import path
path.append('src')
from othello import (
        OthelloCell, BlackCell, WhiteCell, UndefCell,
        WHITE, BLACK, UNDEF,
        Othello,
        Player)

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

class PlayerTestCase(TestCase):
    def setUp(self):
        self.othello = Othello()
        self.player = Player(self.othello, BLACK)

    def color_test(self):
        assert(self.player.color == BLACK)

    def othello_test(self):
        self.player.othello == self.othello

    def puttable_test(self):
        assert(self.player.puttable((2, 3)) is True)

    @raises(ValueError)
    def put_test(self):
        self.player.put((0, 0))

    def put_test2(self):
        self.player.put((3, 2))
        assert(self.othello[3][3] == BLACK)
        assert(self.othello[3][2] == BLACK)
