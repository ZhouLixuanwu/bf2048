import tkinter as tk
import tkinter.messagebox as messagebox
import sys

class GamePanel:
    '''The GUI view class of the 2048 game showing via tkinter.'''
    CELL_PADDING = 10
    BACKGROUND_COLOR = '#92877d'
    EMPTY_CELL_COLOR = '#9e948a'
    CELL_BACKGROUND_COLOR_DICT = {
        '2': '#eee4da',
        '4': '#ede0c8',
        '8': '#f2b179',
        '16': '#f59563',
        '32': '#f67c5f',
        '64': '#f65e3b',
        '128': '#edcf72',
        '256': '#edcc61',
        '512': '#edc850',
        '1024': '#edc53f',
        '2048': '#edc22e',
        'beyond': '#3c3a32'
    }
    CELL_COLOR_DICT = {
        '2': '#776e65',
        '4': '#776e65',
        '8': '#f9f6f2',
        '16': '#f9f6f2',
        '32': '#f9f6f2',
        '64': '#f9f6f2',
        '128': '#f9f6f2',
        '256': '#f9f6f2',
        '512': '#f9f6f2',
        '1024': '#f9f6f2',
        '2048': '#f9f6f2',
        'beyond': '#f9f6f2'
    }
    FONT = ('Verdana', 24, 'bold')
    UP_KEYS = ('w', 'W', 'Up')
    LEFT_KEYS = ('a', 'A', 'Left')
    DOWN_KEYS = ('s', 'S', 'Down')
    RIGHT_KEYS = ('d', 'D', 'Right')

    def __init__(self, grid):
        self.grid = grid
        self.root = tk.Tk()
        if sys.platform == 'win32':
            self.root.iconbitmap('2048.ico')
        self.root.title('2048')
        self.root.resizable(False, False)
        self.background = tk.Frame(self.root, bg=GamePanel.BACKGROUND_COLOR)
        self.cell_labels = []
        for i in range(self.grid.size):
            row_labels = []
            for j in range(self.grid.size):
                label = tk.Label(self.background, text='',
                                 bg=GamePanel.EMPTY_CELL_COLOR,
                                 justify=tk.CENTER, font=GamePanel.FONT,
                                 width=4, height=2)
                label.grid(row=i, column=j, padx=10, pady=10)
                row_labels.append(label)
            self.cell_labels.append(row_labels)
        self.background.pack(side=tk.TOP)

    def paint(self):
        for i in range(self.grid.size):
            for j in range(self.grid.size):
                if self.grid.cells[i][j] == 0:
                    self.cell_labels[i][j].configure(
                         text='',
                         bg=GamePanel.EMPTY_CELL_COLOR)
                else:
                    cell_text = str(self.grid.cells[i][j])
                    if self.grid.cells[i][j] > 2048:
                        bg_color = GamePanel.CELL_BACKGROUND_COLOR_DICT.get('beyond')
                        fg_color = GamePanel.CELL_COLOR_DICT.get('beyond')
                    else:
                        bg_color = GamePanel.CELL_BACKGROUND_COLOR_DICT.get(cell_text)
                        fg_color = GamePanel.CELL_COLOR_DICT.get(cell_text)
                    self.cell_labels[i][j].configure(
                        text=cell_text,
                        bg=bg_color, fg=fg_color)