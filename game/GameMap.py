from utils import nextcell, randbool, randcell

# 0 - area
# 1 - forest tree
# 2 - river
# 3 - hospital
# 4 - shop
# 5 - fire

CELL_TYPES = ("🟩", "🌲", "🌊", "🏥", "🏪", "🔥")
TREE_BONUS = 100
UPGRADE_COST = 500
LIFE_COST = 1000


class GameMap:
    def __init__(self, col, row):
        self.col = col
        self.row = row
        self.cells = [[0 for i in range(col)] for j in range(row)]
        self.generate_forest(1, 6)
        self.generate_river(2)
        self.generate_river(3)

        self.add_fire()
        self.add_fire()
        self.add_fire()
        self.generate_upgrade_shop()
        self.generate_hospital()

    def generate_river(self, riverLen):
        """
        Генерирует реку случайной формы, начиная с случайной клетки.
        Args:
            riverLen: Длина реки
        """
        randRow, randCol = randcell(self.row - 1, self.col - 1)
        while self.check_cell_type(randRow, randCol, 2):
            randRow, randCol = randcell(self.row - 1, self.col - 1)

        self.cells[randRow][randCol] = 2

        length_left = riverLen - 1

        while length_left > 0:
            nextRow, nextCol = nextcell(randRow, randCol)

            if not self.check_bounds(nextRow, nextCol):
                continue

            if self.check_cell_type(nextRow, nextCol, 2):
                continue

            self.cells[nextRow][nextCol] = 2
            randRow, randCol = nextRow, nextCol
            length_left -= 1

    def generate_forest(self, limit, max_random):
        """
        Выставляет дерево в произвольную клетку поля
        Входные параметры влияют на результат таким образом
        Если передавать (5, 10) это будет означать что ~50% поля будет заполнено деревьями
        В этом случае чем меньше limit тем меньше деревьев будет на поле
        Args:
            limit (int): Пороговое значение для решения ставить дерево или нет
            max_random (int): Пороизвольное значение
        """
        for row_i in range(self.row):
            for cell_i in range(self.col):
                if randbool(limit, max_random):
                    self.cells[row_i][cell_i] = 1

    def generate_upgrade_shop(self):
        randRow, randCol = randcell(self.row - 1, self.col - 1)
        self.cells[randRow][randCol] = 4

    def generate_hospital(self):
        randRow, randCol = randcell(self.row - 1, self.col - 1)
        while self.check_cell_type(randRow, randCol, 4):
            randRow, randCol = randcell(self.row - 1, self.col - 1)

        self.cells[randRow][randCol] = 3

    def generate_tree(self):
        randRow, randCol = randcell(self.row - 1, self.col - 1)
        while not self.check_cell_type(randRow, randCol, 0):
            randRow, randCol = randcell(self.row - 1, self.col - 1)
        self.cells[randRow][randCol] = 1

    def add_fire(self):
        randRow, randCol = randcell(self.row - 1, self.col - 1)
        if self.check_cell_type(randRow, randCol, 1):
            self.cells[randRow][randCol] = 5

    def update_fires(self, helicopter):
        for row_i in range(self.row):
            for cell_i in range(self.col):
                if self.check_cell_type(row_i, cell_i, 5):
                    helicopter.score -= 10
                    self.cells[row_i][cell_i] = 0

        for _ in range(5):
            self.add_fire()

    def print_rows(self):
        for row in range(self.row):
            print(row)

    def print_map(self, helicopter, clouds):
        print("🔲" * (self.col + 2))
        for row in range(self.row):
            print("🔲", end="")
            for col in range(self.col):
                cell = self.cells[row][col]
                if clouds.cells[row][col] == 1:
                    print("🔵", end="")
                elif clouds.cells[row][col] == 2:
                    print("🌀", end="")
                elif helicopter.row == row and helicopter.col == col:
                    print("🚁", end="")
                elif 0 <= cell < len(CELL_TYPES):
                    print(CELL_TYPES[cell], end="")
            print("🔲")
        print("🔲" * (self.col + 2))

    def print_map_with_num(self, helicopter, clouds):
        print("+ ", end="")
        print(*range(self.col), end="")
        print("🔲")
        for row in range(self.row):
            print(row, end="")
            for col in range(self.col):
                cell = self.cells[row][col]
                if clouds.cells[row][col] == 1:
                    print("🔵", end="")
                elif clouds.cells[row][col] == 2:
                    print("🌀", end="")
                elif helicopter.row == row and helicopter.col == col:
                    print("🚁", end="")
                elif 0 <= cell < len(CELL_TYPES):
                    print(CELL_TYPES[cell], end="")
            print("🔲")
        print("+", end="")
        print("🔲" * (self.col + 1))

    def check_bounds(self, rowIdx, colIdx):
        """Проверяет входят ли координаты в пределы поля"""
        return 0 <= rowIdx < self.row and 0 <= colIdx < self.col

    def check_cell_type(self, rowIdx, colIdx, cellType):
        """Проверяет тип клетки"""
        return self.cells[rowIdx][colIdx] == cellType

    def process_helicopter(self, helicopter, clouds):
        heliRow, heliCol = helicopter.row, helicopter.col
        cloudCell = clouds.cells[helicopter.row][helicopter.col]

        if self.check_cell_type(heliRow, heliCol, 2):
            helicopter.tank = helicopter.mxTank
        if self.check_cell_type(heliRow, heliCol, 5) and helicopter.tank > 0:
            helicopter.tank -= 1
            helicopter.score += TREE_BONUS
            self.cells[heliRow][heliCol] = 1
        if (
            self.check_cell_type(heliRow, heliCol, 4)
            and helicopter.score >= UPGRADE_COST
        ):
            helicopter.mxTank += 1
            helicopter.score -= UPGRADE_COST
        if self.check_cell_type(heliRow, heliCol, 3) and helicopter.score >= LIFE_COST:
            helicopter.lives += 10
            helicopter.score -= LIFE_COST
        if cloudCell == 2:
            helicopter.lives -= 1
            if helicopter.lives == 0:
                helicopter.game_over()

    def export_data(self):
        return {"cells": self.cells}

    def import_data(self, data):
        self.cells = data["cells"] or [
            [0 for i in range(self.col)] for j in range(self.row)
        ]
