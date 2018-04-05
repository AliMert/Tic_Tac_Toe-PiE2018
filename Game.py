import os

os.system("clear")


def print_header():
    print("Welcome to Tic-Tac-Toe\n")


class Game:
    def __init__(self):
        self.cells = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
        self.playerX = "playerX"
        self.playerO = "playerO"

    def start(self):
        print_header()
        print("  - Please Enter the Name of the Players -")
        self.playerX = str(input("Player1(X) : "))
        self.playerO = str(input("Player2(O) : "))

        while self.playerO == self.playerX:
            os.system("clear")
            print_header()
            print("  - Please Enter the Name of the Players -")
            print("Player1(X) : " + str(self.playerX))
            print("\n\"%s\" is taken, Please choose another name: " % self.playerX)
            self.playerO = str(input("Player2(O) : "))

    def display(self):
        print(" %s | %s | %s " % (self.cells[0], self.cells[1], self.cells[2]))
        print("-----------")
        print(" %s | %s | %s " % (self.cells[3], self.cells[4], self.cells[5]))
        print("-----------")
        print(" %s | %s | %s " % (self.cells[6], self.cells[7], self.cells[8]))

    def update(self, cell_no, player):  # test: cell_no ?= int, player X or O
        player = "X" if player is self.playerX else "O"
        if self.cells[cell_no] == " ":
            self.cells[cell_no] = player

    def refresh(self):
        # Clears the screen
        os.system("clear")

        # prints the header
        print_header()

        # Shows the board
        self.display()

    def is_winner(self, player):

        player = "X" if player is self.playerX else "O"
        for x, y, z in [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]:
            if self.cells[x] == self.cells[y] == self.cells[z]:
                if self.cells[x] == player:  # is "X" or "O": # maybe test
                    return True

        return False

    def is_tie(self):
        for cell in self.cells:
            if cell == " ":
                return False

        return True

    def whose_turn(self):
        x = self.cells.count("X")
        o = self.cells.count("O")

        if x == o:
            return self.playerX
        else:
            return self.playerO

    def reset(self):
        self.cells = [" ", " ", " ", " ", " ", " ", " ", " ", " "]


