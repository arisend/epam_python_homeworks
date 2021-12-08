"""
Given a Tic-Tac-Toe 3x3 board (can be unfinished).
Write a function that checks if the are some winners.
If there is "x" winner, function should return "x wins!"
If there is "o" winner, function should return "o wins!"
If there is a draw, function should return "draw!"
If board is unfinished, function should return "unfinished!"

Example:
    [[-, -, o],
     [-, x, o],
     [x, o, x]]
    Return value should be "unfinished"

    [[-, -, o],
     [-, o, o],
     [x, x, x]]

     Return value should be "x wins!"

"""
from itertools import product
from typing import List


class Tic_Tac_Toe_Board_Exception(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


class Tic_Tac_Toe_game():
    def __init__(self, board):
        if len(board) != 3 or len(board[0]) != 3:
            raise Tic_Tac_Toe_Board_Exception("Your board have not supported dimensions")
        self.board = board
        self.win_combinations = []
        elements = list(product('012', repeat=2))
        for i in range(0, 9, 3):
            self.win_combinations.append([elements[i], elements[i + 1], elements[i + 2]])
        for i in range(0, 3, 1):
            self.win_combinations.append([elements[i], elements[i + 3], elements[i + 6]])
        self.win_combinations.append([(0, 0), (1, 1), (2, 2)])
        self.win_combinations.append([(0, 2), (1, 1), (2, 0)])

    def check_game(self):
        win = None
        for comb in self.win_combinations:
            if self.check_comb(comb):
                win = {'side': self.get_cell(comb[0]), 'comb': comb}
        if "-" in [*self.board[0]] and not win:
            return "unfinished"
        elif win:
            return "{} wins!".format(win['side'])
        else:
            return "draw"

    def get_cell(self, coord: tuple):
        return self.board[int(coord[0])][int(coord[1])]

    def check_comb(self, comb):
        return self.get_cell(comb[0]) == self.get_cell(comb[1]) == self.get_cell(comb[2])


def tic_tac_toe_checker(board: List[List]) -> str:
    game3_3 = Tic_Tac_Toe_game(board)
    return game3_3.check_game()


tic_tac_toe_checker([['-', '-', 'o'], ['-', 'o', 'o'], ['x', 'x', 'x']])

tic_tac_toe_checker([['-', '-', 'o'], ['-', 'x', 'o'], ['x', 'o', 'x']])
