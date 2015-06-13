from Tkinter import *
from copy import deepcopy

from othello import DEFAULT_OTHELLO_SIZE

class OthelloCellButton(Button):
    def __init__(self, master=None, **kw):
        if 'background' not in kw.keys():
            kw['background'] = 'lime green'
        Button.__init__(self, master, kw)

class StartButton(Button):
    def __init__(self, master=None, **kw):
        if 'text' not in kw.keys():
            kw['text'] = 'Start'
        Button.__init__(self, master, kw)

    def get_name(self):
        return 'Start'

class ClearButton(Button):
    def __init__(self, master=None, **kw):
        if 'text' not in kw.keys():
            kw['text'] = 'Clear'
        Button.__init__(self, master, kw)

class LoadDataButton(Button):
    def __init__(self, master=None, **kw):
        if 'text' not in kw.keys():
            kw['text'] = 'Load Data'
        Button.__init__(self, master, kw)

class AutoPutButton(Button):
    def __init__(self, master=None, **kw):
        if 'text' not in kw.keys():
            kw['text'] = 'Auto put'
        Button.__init__(self, master, kw)

class AllPutButton(Button):
    def __init__(self, master=None, **kw):
        if 'text' not in kw.keys():
            kw['text'] = 'All put'
        Button.__init__(self, master, kw)

class OthelloBord(Frame):

    def __init__(self, master=None, size=DEFAULT_OTHELLO_SIZE):
        Frame.__init__(self, master)

        self._size = size
        self._button_mat = None

        self.init(master)

    def init(self, master=None):
        self._button_mat = [[0 for i in range(self.size[0])] for j in
                            range(self.size[1])]
        for i in range(self.size[0]):
            for j in range(self.size[1]):
                self._button_mat[i][j] = OthelloCellButton(self)
                self._button_mat[i][j].grid(row=i, column=j)

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


if __name__ == '__main__':
    root = Tk()
    root.title('Othello')
    bord = OthelloBord(root)
    side_frame = SideButtonBarFrame(root)
    bord.pack(side='left')
    side_frame.pack(side='left')
    root.mainloop()
