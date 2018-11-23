import random


class Board(object):
    _board = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    _player_sign = None
    _computer_sign = None
    _moved = []
    _move = None
    _winner = None

    def __init__(self):
        while self._player_sign not in ('X', 'O'):
            self._player_sign = (input("please select your sign: ")).upper()
            if self._player_sign == 'X':
                self._computer_sign = 'O'
            elif self._player_sign == 'O':
                self._computer_sign = 'X'
            else:
                print("incorrect input. your sign should be X or O.")

    def have_winner(self):
        if ((self._board[1] == self._board[2] == self._board[3] == self._player_sign) or
            (self._board[4] == self._board[5] == self._board[6] == self._player_sign) or
            (self._board[7] == self._board[8] == self._board[9] == self._player_sign) or
            (self._board[1] == self._board[5] == self._board[9] == self._player_sign) or
            (self._board[3] == self._board[5] == self._board[7] == self._player_sign)
        ):
            # print( self._board[1], self._board[2], self._board[3], self._player_sign)
            return self._player_sign
        elif ((self._board[1] == self._board[2] == self._board[3] == self._computer_sign) or
              (self._board[4] == self._board[5] == self._board[6] == self._computer_sign) or
              (self._board[7] == self._board[8] == self._board[9] == self._computer_sign) or
              (self._board[1] == self._board[5] == self._board[9] == self._computer_sign) or
              (self._board[3] == self._board[5] == self._board[7] == self._computer_sign)
        ):
            return self._computer_sign
        else:
            return None

    def draw(self):
        print("{}|{}|{}\n-|-|-\n{}|{}|{}\n-|-|-\n{}|{}|{}".format(*self._board[1:]))

    def player_turn(self):
        while True:
            self._move=int(input("choose your cell? "))
            if not (self._move in range(1, 10)):
                 print("input digits from 1 to 9, please.")
            elif (self._move in self._moved):
                 print("This cell is already chosen!")
            else:
                self._moved.append(self._move)
                self._board[self._move]=self._player_sign
                break

    def computer_turn(self):
        while self._move in self._moved:
            self._move=random.randint(1, 9)
        self._moved.append(self._move)
        self._board[self._move]=self._computer_sign


print("welcome to tic tac toe!")
board=Board()
board.draw()
while not board._winner:
    board.player_turn()
    board.computer_turn()
    board.draw()
    if board.have_winner():
        board._winner = board.have_winner()
        print("{} is winner".format(board._winner))
