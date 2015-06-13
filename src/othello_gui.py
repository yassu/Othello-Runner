from Tkinter import *
from copy import deepcopy

from othello import DEFAULT_OTHELLO_SIZE, Othello, BLACK, WHITE, UNDEF

class Field:
    def set_othello_bord(self, bord):
        self._othello_bord = bord

    @property
    def othello_bord(self):
        return self._othello_bord

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

    def set_simulation_button(self, b):
        self._simulation_button = b

    @property
    def simulation_button(self):
        return self._simulation_button

class OthelloCellButton(Button):
    def __init__(self, ind, master=None, **kw):
        if 'background' not in kw.keys():
            kw['background'] = 'lime green'
        Button.__init__(self, master, kw, command=self.clicked_event)
        self._ind = ind

    @property
    def ind(self):
        return self._ind

    def clicked_event(self):
        othello_bord = self._field.othello_bord
        color = othello_bord.next_color
        othello_bord.put(self.ind)

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

    def set_field(self, field):
        self._field = field

    def get_name(self):
        return 'Start'

class ClearButton(Button):
    def __init__(self, master=None, **kw):
        if 'text' not in kw.keys():
            kw['text'] = 'Clear'
        Button.__init__(self, master, kw)

    def set_field(self, field):
        self._field = field

class LoadDataButton(Button):
    def __init__(self, master=None, **kw):
        if 'text' not in kw.keys():
            kw['text'] = 'Load Data'
        Button.__init__(self, master, kw)

    def set_field(self, field):
        self._field = field

class SimulationButton(Button):
    def __init__(self, master=None, **kw):
        if 'text' not in kw.keys():
            kw['text'] = 'Simulation'
        Button.__init__(self, master, kw)

    def set_field(self, field):
        self._field = field


class OthelloBord(Frame):

    def __init__(self, master=None, size=DEFAULT_OTHELLO_SIZE):
        Frame.__init__(self, master)

        self._size = size
        self._button_mat = None
        self._next_color = BLACK
        self._othello = Othello()

        self.init(master)

    def init(self, master=None):
        self._button_mat = [[0 for i in range(self.size[0])] for j in
                            range(self.size[1])]
        for i in range(self.size[0]):
            for j in range(self.size[1]):
                self._button_mat[i][j] = OthelloCellButton(
                        (i, j),
                        self,
                        width=1, height=1)
                self._button_mat[i][j].grid(row=i, column=j)
        self.synchronized_with_othello()

    @property
    def next_color(self):
        return self._next_color

    @property
    def othello(self):
        return self._othello

    def synchronized_with_othello(self):
        for i in range(self.size[0]):
            for j in range(self.size[1]):
                self._button_mat[i][j].change_color(self._othello[i][j])

    def set_field(self, field):
        self._field = field
        for i in range(self.size[0]):
            for j in range(self.size[1]):
                self._button_mat[i][j].set_field(field)

    def button_mat(self):
        return deepcopy(self._button_mat)

    @property
    def size(self):
        return self._size

    def put(self, ind):
        self.othello.put(ind, self._next_color)
        self.synchronized_with_othello()
        self._next_color = self._next_color.different_color


class SideButtonBarFrame(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)

        self._start_button = StartButton(self)
        self._start_button.grid(row=0, column=0)

        self._clear_button = ClearButton(self)
        self._clear_button.grid(row=1, column=0)

        self._load_data_button = LoadDataButton(self)
        self._load_data_button.grid(row=2, column=0)

        self._simulation_button = SimulationButton(self)
        self._simulation_button.grid(row=3, column=0)

    @property
    def start_button(self):
        return self._start_button

    @property
    def clear_button(self):
        return self._clear_button

    @property
    def load_data_button(self):
        return self._load_data_button

    @property
    def simulation_button(self):
        return self._simulation_button

    def set_field(self, field):
        self._start_button.set_field(field)
        self._clear_button.set_field(field)
        self._load_data_button.set_field(field)
        self._simulation_button.set_field(field)


if __name__ == '__main__':
    root = Tk()
    root.title('Othello')
    field = Field()

    bord = OthelloBord(root)
    bord.set_field(field)
    field.set_othello_bord(bord)

    side_frame = SideButtonBarFrame(root)
    side_frame.set_field(field)
    field.set_start_button(side_frame.start_button)
    field.set_clear_button(side_frame.clear_button)
    field.set_load_data_button(side_frame.load_data_button)
    field.set_simulation_button(side_frame.simulation_button)
    bord.pack(side='left')
    side_frame.pack(side='left')
    root.mainloop()
