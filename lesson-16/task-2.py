class Turtle:
    def __init__(self, x=0, y=0, s=1):
        self.x = x
        self.y = y
        self.s = s

    def go_up(self):
        self.y += self.s

    def go_down(self):
        self.y -= self.s

    def go_left(self):
        self.x -= self.s

    def go_right(self):
        # В условии была опечатка: увеличиваем x, а не y
        self.x += self.s

    def evolve(self):
        self.s += 1

    def degrade(self):
        if self.s <= 1:
            raise ValueError("Cannot degrade: step size would become ≤ 0")
        self.s -= 1

    def count_moves(self, x2, y2):
        dx = abs(x2 - self.x)
        dy = abs(y2 - self.y)

        if dx % self.s != 0 or dy % self.s != 0:
            return -1

        moves_x = dx // self.s
        moves_y = dy // self.s

        return moves_x + moves_y
