from player import HumanPlayer, RandomCompPlayer, GeniusComputerPlayer
import time


class TicTacToe:
    def __init__(self):
        self.board = [' ' for i in range(9)]
        self.current_winner = None

    def print_board(self):
        for row in [self.board[i*3: (i+1)*3] for i in range(3)]:
            print('| ' + '| '.join(row) + ' |')

    @staticmethod
    def print_board_nums():
        # 0 | 1 | 2 etc {tells us what number corresponds to what box}
        number_board = [
            [str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + '| '.join(row) + ' |')

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    def empty_squares(self):
        return ' ' in self.board

    def num_empty_squares(self):
        return self.board.count(' ')

    def make_move(self, square, letter):
        # if valid, make the move
        if self.board[square] == ' ':
            self.board[square] = letter
        #    print(type(square),type(letter))

            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        # check row
        row_ind = square // 3
        row = self.board[row_ind*3: (row_ind + 1) * 3]
        if all([spot == letter for spot in row]):
            return True

        # check column
        col_ind = square % 3
        column = [self.board[col_ind + i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True

        # check diagonal
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all([spot == letter for spot in diagonal1]):
                return True

            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([spot == letter for spot in diagonal2]):
                return True
        return False


def play(game, x_player, o_player, print_game=True):
    if print_game:
        game.print_board_nums()

    letter = 'X'  # starting letter
    # iterate while the game still has empty squares
    # ( we don't have to worry about winner because we'll just that which
    #   breaks the loop)
    while game.empty_squares():
        # get the move from an appropriate player
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        # let's define a function to make a move!
        if game.make_move(square, letter):
            if print_game:
                print(letter + f' makes a move to the square {square}')
                game.print_board()
                print()

            if game.current_winner:
                if print_game:
                    print(letter + ' wins!')
                return letter
            # after we make a move we need to alternate letters
            letter = 'O' if letter == 'X' else 'X'

        # pause
        time.sleep(0.5)

    if print_game:
        print('It\'s a tie! ')


if __name__ == '__main__':
    x = int(input(
        '''Which type of opponent do you want?
1- novice AI \n2- advanced AI \n3- PvP \n'''
        ))
    if x == 1:
        b = True
        while b is True:
            a = input('Choose if you want to go 1st(1) or 2nd(2): ')
            if a == '1':
                x_player = HumanPlayer('X')
                o_player = RandomCompPlayer('O')
                b = False
            elif a == '2':
                o_player = HumanPlayer('O')
                x_player = RandomCompPlayer('X')
                b = False
            else:
                print('Invalid input. Please only enter 1 or 2. Try again.')
    elif x == 2:
        b = True
        while b is True:
            a = input('Choose if you want to go 1st(1) or 2nd(2): ')
            if a == '1':
                x_player = HumanPlayer('X')
                o_player = GeniusComputerPlayer('O')
                b = False
            elif a == '2':
                o_player = HumanPlayer('O')
                x_player = GeniusComputerPlayer('X')
                b = False
            else:
                print('Invalid input. Please only enter 1 or 2. Try again.')
    elif x == 3:
        b = True
        while b is True:
            a = input('Choose if you want to go 1st(1) or 2nd(2): ')
            if a == '1':
                x_player = HumanPlayer('X')
                o_player = HumanPlayer('O')
                b = False
            elif a == '2':
                o_player = HumanPlayer('O')
                x_player = HumanPlayer('X')
                b = False
            else:
                print('Invalid input. Please only enter 1 or 2. Try again.')
    t = TicTacToe()
    play(t, x_player, o_player, print_game=True)
