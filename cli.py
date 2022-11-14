# This file contains the Command Line Interface (CLI) for
# the Tic-Tac-Toe game. This is where input and output happens.
# For core game logic, see logic.py.


from logic import Logic
from tests import Test


class Cli:

    def __init__(self):
        self.board = []
        self.logic = Logic()

    def create_board(self):
        for i in range(3):
            row = []
            for j in range(3):
                row.append('-')
            self.board.append(row)
    
    def fix_spot(self, row, col, player):
        self.board[row][col] = player

    
    def show_board(self):
        for row in self.board:
            for item in row:
                print(item, end=" ")
            print()

    
    def start(self):
        self.create_board()

        player = 'X' if self.logic.get_random_first_player() == 1 else 'O'
        while True:
            print(f"Player {player} turn")

            self.show_board()

            # asking users for input
            row, col = list(
                map(int, input("Enter row and column numbers to fix a spot: ").split()))
            print()

            # fixing the spot
            self.fix_spot(row - 1, col - 1, player)

            # checking if the current player has won or not
            if self.logic.is_player_win(player, self.board):
                print(f"Player {player} wins the game!")
                break

            # checking whether the game is draw or not
            if self.logic.is_board_filled(self.board):
                print("Match Draw!")
                break

            # swapping the turn
            player = self.logic.swap_player_turn(player)

        # showing the final view of board
        print()
        self.show_board()


if __name__ == '__main__':
    cli = Cli()
    cli.start()