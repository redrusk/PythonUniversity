import json
import os
import time

from pynput import keyboard

from Clouds import Clouds
from GameMap import GameMap
from Helicopter import Helicopter

TICK_SLEEP = 0.1
TREE_UPDATE = 50
FIRE_UPDATE = 50
CLOUDS_UPDATE = 100
MAP_COL, MAP_ROW = 10, 6
MOVES = {"w": (-1, 0), "d": (0, 1), "s": (1, 0), "a": (0, -1)}
tick = 1

gameMap = GameMap(MAP_COL, MAP_ROW)
helicopter = Helicopter(MAP_COL, MAP_ROW)
clouds = Clouds(MAP_COL, MAP_ROW)


def precess_key(key):
    global helicopter, clouds, gameMap, tick
    char = key.char.lower()
    if char in MOVES.keys():
        helicopter.move(MOVES[char][0], MOVES[char][1])
    elif char == "f":
        data = {
            "helicopter": helicopter.export_data(),
            "clouds": clouds.export_data(),
            "game_map": gameMap.export_data(),
            "tick": tick,
        }
        with open("level.json", "w") as lvl:
            json.dump(data, lvl)
    elif char == "g":
        with open("level.json", "r") as lvl:
            data = json.load(lvl)
            tick = data["tick"] or 1
            helicopter.import_data(data["helicopter"])
            clouds.import_data(data["clouds"])
            gameMap.import_data(data["game_map"])


listener = keyboard.Listener(on_release=precess_key)
listener.start()

while True:
    os.system("cls")
    gameMap.process_helicopter(helicopter, clouds)
    helicopter.print_stats()
    gameMap.print_map(helicopter, clouds)

    tick += 1
    time.sleep(TICK_SLEEP)

    if tick % TREE_UPDATE == 0:
        gameMap.generate_tree()

    if tick % FIRE_UPDATE == 0:
        gameMap.update_fires(helicopter)

    if tick % CLOUDS_UPDATE == 0:
        clouds.update_clouds()
