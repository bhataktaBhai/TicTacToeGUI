from tkinter import *


class TicTacToe(Tk):

    COLOUR = 'RED4'
    WIN_COLOUR = 'GREEN4'
    LINE = 20

    board = [[0]*3 for i in range(3)]
    squares = []
    moves = 0
    turn = 1
    symbol = 'X'

    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        self.configure(background = self.COLOUR)
        self.geometry(f'{self.LINE*29}x{self.LINE*29}')
        self.resizable(0, 0)
        for i in range(3):
            for j in range(3):
                frame = Frame(master = self,
                              height = self.LINE*9,
                              width  = self.LINE*9)
                frame.grid(row = i, column = j,
                           padx = (0, self.LINE),
                           pady = (0, self.LINE))
                frame.pack_propagate(0)
                square = Label(master = frame,
                               foreground = 'RED4',
                               font = ('Ariel', self.LINE*5))
                self.squares.append(square)
                square.row, square.column = i, j
                square.bind('<Button-1>', self.play)
                square.pack(fill = BOTH, expand = True)

    def play(self, event):
        square = event.widget
        row = square.row
        column = square.column
        self.board[row][column] = self.turn
        square.configure(text = self.symbol)
        square.bind('<Button-1>', lambda e: None)
        self.moves += 1
        winner = self.win()
        print(winner)
        if winner or self.moves == 9:
            for square in self.squares:
                square.bind('<Button-1>', lambda e: None)
                if (square.row, square.column) in winner:
                    square.configure(foreground = self.WIN_COLOUR)
        self.turn *= -1
        if self.symbol == 'X':
            self.symbol = 'O'
        else:
            self.symbol = 'X'

    def win(self):
        for row in range(3):
            player = self.board[row][0]
            if player != 0:
                for column in range(1, 3):
                    if self.board[row][column] != player:
                        break
                else:
                    return [(row, column) for column in range(3)]

        for column in range(3):
            player = self.board[0][column]
            if player != 0:
                for row in range(1, 3):
                    if self.board[row][column] != player:
                        break
                else:
                    return [(row, column) for row in range(3)]

        player = self.board[1][1]
        if player != 0:
            for row in range(0, 3, 2):
                if self.board[row][row] != player:
                    break
            else:
                return [(row, row) for row in range(3)]

            for row in range(0, 3, 2):
                if self.board[row][2-row] != player:
                    break
            else:
                return [(row, 2-row) for row in range(3)]

        return ()


tic = TicTacToe(className = 'Tic Tac Toe')
tic.mainloop()
