import os

from utils import randcell


class Helicopter:
    def __init__(self, col, row):
        randRow, randCol = randcell(row - 1, col - 1)
        self.mapCol = col
        self.mapRow = row
        self.row = randRow
        self.col = randCol
        self.tank = 0
        self.mxTank = 1
        self.score = 0
        self.lives = 20

    def move(self, toRow, toCol):
        nRow = toRow + self.row
        nCol = toCol + self.col
        if 0 <= nRow < self.mapRow and 0 <= nCol < self.mapCol:
            self.row = nRow
            self.col = nCol

    def print_stats(self):
        print("🪣 ", self.tank, "/", self.mxTank, sep="", end=" | ")
        print("🏆", self.score, end=" | ")
        print("💛", self.lives)

    def game_over(self):
        os.system("cls")
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        print("X                                X")
        print("X  GAME OVER, YOUR SCORE: ", self.score, "  X")
        print("X                                X")
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        exit(0)

    def export_data(self):
        return {
            "row": self.row,
            "col": self.col,
            "score": self.score,
            "lives": self.lives,
            "tank": self.tank,
            "mx_tank": self.mxTank,
        }

    def import_data(self, data):
        self.row = data["row"] or 0
        self.col = data["col"] or 0
        self.score = data["score"] or 0
        self.lives = data["lives"] or 3
        self.tank = data["tank"] or 0
        self.mxTank = data["mx_tank"] or 1
