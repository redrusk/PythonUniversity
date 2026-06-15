from random import randint as rand

def randbool(limit, max_random):
    t = rand(0, max_random)
    return t <= limit

def randcell(h, w):
    return rand(0, h), rand(0, w)

# 0 - up, 1 - right, 2 - bottom, 3 - left
def nextcell(x, y):
    moves = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    t = rand(0, 3)
    dx, dy = moves[t]
    return x + dx, y + dy
