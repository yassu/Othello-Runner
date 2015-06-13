from Tkinter import *
from copy import deepcopy

from othello import DEFAULT_OTHELLO_SIZE, Othello, BLACK, WHITE, UNDEF

class Field:
    def set_othello_bord(self, bord):
        self._othello_bord = bord

    @property
    def othello_bord(self):
        return self._othello_bord()

    def set_start_button(self, b):
        self._start_button = b

    @property
    def start_button(self):
        return self._start_button

    def set_clear_button(self, b):
        self._clear_button = b

    @property
    def clear_button(self):
        return self._clear_button

    def set_load_data_button(self, b):
        self._load_data_button = b

    @property
    def load_data_button(self):
        return self._load_data_button

    def set_auto_put_button(self, b):
        self._auto_put_button = b

    @property
    def auto_put_button(self):
        return self._auto_put_button

    def set_all_put_button(self, b):
        self._all_put_button = b

    @property
    def all_put_button(self):
        return self._all_put_button

class OthelloCellButton(Button):
    def __init__(self, master=None, **kw):
        if 'background' not in kw.keys():
            kw['background'] = 'lime green'
        Button.__init__(self, master, kw)

    def set_field(self, field):
        self._field = field

    def change_color(self, color):
        if color == UNDEF:
            self.configure(text='')
        else:
            self.configure(text=str(color))

class StartButton(Button):
    def __init__(self, master=None, **kw):
        if 'text' not in kw.keys():
            kw['text'] = 'Start'
        Button.__init__(self, master, kw)

    def set_field(self):
        self._field = field

    def get_name(self):
        return 'Start'

class ClearButton(Button):
    def __init__(self, master=None, **kw):
        if 'text' not in kw.keys():
            kw['text'] = 'Clear'
        Button.__init__(self, master, kw)

    def set_field(self):
        self._field = field

class LoadDataButton(Button):
    def __init__(self, master=None, **kw):
        if 'text' not in kw.keys():
            kw['text'] = 'Load Data'
        Button.__init__(self, master, kw)

    def set_field(self):
        self._field = field

class AutoPutButton(Button):
    def __init__(self, master=None, **kw):
        if 'text' not in kw.keys():
            kw['text'] = 'Auto put'
        Button.__init__(self, master, kw)

    def set_field(self):
        self._field = field

class AllPutButton(Button):
    def __init__(self, master=None, **kw):
        if 'text' not in kw.keys():
            kw['text'] = 'All put'
        Button.__init__(self, master, kw)

    def set_field(self):
        self._field = field

class OthelloBord(Frame):

    def __init__(self, master=None, size=DEFAULT_OTHELLO_SIZE):
        Frame.__init__(self, master)

        self._size = size
        self._button_mat = None
        self._othello = Othello()

        self.init(master)

    def init(self, master=None):
        self._button_mat = [[0 for i in range(self.size[0])] for j in
                            range(self.size[1])]
        for i in range(self.size[0]):
            for j in range(self.size[1]):
                self._button_mat[i][j] = OthelloCellButton(self, width=1,
                        height=1)
                self._button_mat[i][j].grid(row=i, column=j)
        self.synchronized_with_othello()

    def synchronized_with_othello(self):
        for i in range(self.size[0]):
            for j in range(self.size[1]):
                self._button_mat[i][j].change_color(self._othello[i][j])

    def set_field(self, field):
        self._field = field

    def button_mat(self):
        return deepcopy(self._button_mat)

    @property
    def size(self):
        return self._size


class SideButtonBarFrame(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)

        self._start_button = StartButton(self)
        self._start_button.grid(row=0, column=0)

        self._clear_button = ClearButton(self)
        self._clear_button.grid(row=1, column=0)

        self._load_data_button = LoadDataButton(self)
        self._load_data_button.grid(row=2, column=0)

        self._auto_put_button = AutoPutButton(self)
        self._auto_put_button.grid(row=3, column=0)

        self._all_put_button = AllPutButton(self)
        self._all_put_button.grid(row=4, column=0)

    def set_field(self, field):
        self._start_button.set_field(field)
        self._clear_button.set_field(field)
        self._load_data_button.set_field(field)
        self._auto_put_button.set_field(field)
        self._all_put_button.set_field(field)


if __name__ == '__main__':
    root = Tk()
    root.title('Othello')
    bord = OthelloBord(root)
    side_frame = SideButtonBarFrame(root)
    bord.pack(side='left')
    side_frame.pack(side='left')
    root.mainloop()
