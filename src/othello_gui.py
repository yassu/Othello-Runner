from Tkinter import *
from copy import deepcopy

from othello import DEFAULT_OTHELLO_SIZE

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
                self._button_mat[i][j] = Button(self, background="lime green")
                self._button_mat[i][j].grid(row=i, column=j)

    def button_mat(self):
        return deepcopy(self._button_mat)

    @property
    def size(self):
        return self._size

class SideButtonBarFrame(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)

        self._start_button = Button(self, text='start')
        self._start_button.grid(row=0, column=0)

        self._clear_button = Button(self, text='clear')
        self._clear_button.grid(row=1, column=0)

        self._load_data_button = Button(self, text='Load Data')
        self._load_data_button.grid(row=2, column=0)

        self._auto_put_button = Button(self, text='Auto put')
        self._auto_put_button.grid(row=3, column=0)

        self._all_put_button = Button(self, text='All put')
        self._all_put_button.grid(row=4, column=0)


if __name__ == '__main__':
    root = Tk()
    root.title('Othello')
    bord = OthelloBord(root)
    side_frame = SideButtonBarFrame(root)
    bord.pack(side='left')
    side_frame.pack(side='left')
    root.mainloop()
