import tkinter as tk
from tkinter import ttk
from minesweeper import Board


class Game(ttk.Frame):
    #lower fame that allow player to play the game

    def __init__(self, container, board):
        super().__init__(container)
        self.board = board
        self.container = container

        # add padding to the frame and show it
        self.grid(column=0, row=1, padx=5, pady=5, sticky="nsew")
        
        self.generate_btn(self.board.board_vis)

    def generate_btn(self, board_r):
        #generate buttons for player to play minesweeper
        for i in range(len(board_r)):
            for j in range(len(board_r[0])):
                button = ttk.Button(self, text = board_r[i][j], command = lambda c = i,r = j :self.refresh(c,r))
                button.grid(row = i, column = j, sticky = 'NWES')

    def refresh(self,c,r):
        #update the board with new state
        self.board.reveal(c,r)
        new_board = self.board.board_vis
        if self.board.board[c][r] == "bomb":
            State(self.container, "Game Over!")
        if len(self.board.visited) + self.board.bomb_num == self.board.row * self.board.column:
            State(self.container, "You Win!")
        self.generate_btn(new_board)  
        

class Setup_Board(ttk.Frame):
    #upper fame that allow player to setup the board

    def __init__(self, container):
        super().__init__(container)

        text_row = tk.StringVar()
        row = ttk.Entry(self)
        row.grid(row = 1, column = 2, sticky = 'NWES')
        label_row = ttk.Label(self, text = "Enter how mnay rows: ")
        label_row.grid(row = 1, column = 1, sticky = 'NWES')

        text_column = tk.StringVar()        
        column = ttk.Entry(self)
        column.grid(row = 2, column = 2, sticky = 'NWES')
        label_col = ttk.Label(self, text = "Enter how many columns: ")
        label_col.grid(row = 2, column = 1, sticky = 'NWES')

        text_bomb = tk.StringVar()
        bomb_num = ttk.Entry(self)
        bomb_num.grid(row = 3, column = 2, sticky = 'NWES')
        label_bomb = ttk.Label(self, text = "Enter how many bombs: ")
        label_bomb.grid(row = 3, column = 1, sticky = 'NWES')

        confirm = ttk.Button(self, text = "Start!", command = lambda:Game(container, Board(int(row.get()), int(column.get()), int(bomb_num.get()))))    
        confirm.grid(row = 5, column = 1, sticky = 'NWES',columnspan = 2)

        # add padding to the frame and show it
        self.grid(column=0, row=0, padx=5, pady=5, sticky="nsew")

class State(ttk.Frame):

    def __init__(self, container, state):
        super().__init__(container)
        self.state = state
         
        self.grid(column=0, row=1, padx=5, pady=5, sticky="nsew")
        
        label = ttk.Label(self, text = self.state)
        label.grid(sticky = 'NWES')


class App(tk.Tk):
    def __init__(self):
        super().__init__()        
        self.title("Mineseeper.py")        
               


if __name__ == '__main__':
    app = App()
    Setup_Board(app)
    #a = Board(5, 5, 5)
    #Game(app,a)
    app.mainloop()
