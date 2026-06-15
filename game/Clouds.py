from utils import randbool


class Clouds:
    def __init__(self, col, row):
        self.col = col
        self.row = row
        self.cells = [[0 for i in range(col)] for j in range(row)]

    def update_clouds(self, sc_limit=1, sc_max_rand=20, lc_limit=1, lc_max_rand=10):
        for row_i in range(self.row):
            for cell_i in range(self.col):
                if randbool(sc_limit, sc_max_rand):
                    self.cells[row_i][cell_i] = 1
                    if randbool(lc_limit, lc_max_rand):
                        self.cells[row_i][cell_i] = 2
                else:
                    self.cells[row_i][cell_i] = 0

    def export_data(self):
        return {"cells": self.cells}

    def import_data(self, data):
        self.cells = data["cells"] or [
            [0 for i in range(self.col)] for j in range(self.row)
        ]
