import random

class Board():

    def __init__(self, row, column, bomb_num):
        self.row = row
        self.column = column
        self.bomb_num = bomb_num

        #generate a board that player see, fill with None when init
        self.board_vis = [ [None for j in range(self.column)] for i in range(self.row)]        

        #the board that records bomb positions, player cannot see
        self.board = self.plant_bombs()

        self.visited = set()
        

    def plant_bombs(self):
        ''' setup board and plant bombs'''
        board = []

        #plant bombs
        for i in range(self.bomb_num):
            board.append("bomb")
            
        #fill empty space
        for i in range(self.row * self.column - self.bomb_num):
            board.append(None)

        #shuffle the board
        random.shuffle(board)

        #arrange in board shape
        shape = []
        for i in range(self.row):
            shape.append(board[self.column * i :self.column * (i + 1)])

        return shape
                

    def give_value(self, row, col):
        '''given a row and a col and return how many bombs in the surrounded boxes, if it's bomb return "bomb"'''

        if self.board[row][col] == "bomb":
            # if it's bomb, return "bomb"
            return "bomb"
        
        else:
            #deal with box at edges and corners
            row_up = 0 if row < 1 else row - 1
            col_up = 0 if col < 1 else col - 1
            row_d = self.row - 1 if row == self.row - 1 else row + 1
            col_d = self.column - 1 if col == self.column - 1 else col + 1        

            #boxes sorrounded the box
            surround = {(row,col_up),(row,col_d),
                        (row_up,col_up),(row_up,col_d),
                        (row_d,col_up),(row_d,col_d),
                        (row_up,col),(row_d,col)
                        }
            #count bombs surrounded the box
            count = 0
            for r, c in surround:
                if self.board[r][c] == "bomb":
                    count += 1
            return count
              

    def reveal(self, row, col):

        #deal with box at edges and corners
        row_up = 0 if row < 1 else row - 1
        col_up = 0 if col < 1 else col - 1
        row_d = self.row - 1 if row == self.row - 1 else row + 1
        col_d = self.column - 1 if col == self.column - 1 else col + 1        

        #boxes sorrounded the box
        surround = {(row,col_up),(row,col_d),
                    (row_up,col_up),(row_up,col_d),
                    (row_d,col_up),(row_d,col_d),
                    (row_up,col),(row_d,col)
                    }

        if (row,col) not in self.visited:
            self.visited.add((row,col))
            
            #display value
            if self.give_value(row,col) != 0:
                self.board_vis[row][col] = self.give_value(row,col)

            #reveal all connected zeros if box is zero
            else:
                self.board_vis[row][col] = 0
                for r, c in surround:
                    self.reveal(r,c)
                    

    def __str__(self):
        init = '\n'.join(''.join(str(i).center(5) for i in row) for row in self.board_vis)
        return str(self.board) + "\n" +init


def play():
    print("Please enter board size and number of bombs:")
    row, column, bomb_num = input().split()
    a = Board(int(row), int(column), int(bomb_num))

    while True:
        print(a)
        print("enter box:")
        r,c = input().split()
        a.reveal(int(r), int(c))
        if a.board[int(r)][int(c)] == "bomb":
            break
    print(a)
    print("Game Over")
        
        
if __name__ == "__main__":
    play()
