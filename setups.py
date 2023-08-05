from enum import Enum
import random


'''Defines board dimensions'''
boardWidth = random.randint(20, 20)
boardHeight = random.randint(20, 20)


class GUISetups():
    rectSize = 80
    iconSize = 40
    playerSize = 80
    margin = 0


class WorldDirections(Enum):
    North = 1
    South = 2
    East = 3
    West = 4


class RoomType(Enum):
    Empty = 1
    Blind = 2
    TwoExits = 3
    ThreeExits = 4
    Crossroad = 5


class RoomStatus(Enum):
    Empty = 1
    inProgress = 2
    Solved = 3


movementValue = {WorldDirections.North: -boardWidth,
                 WorldDirections.South: boardWidth,
                 WorldDirections.East: 1,
                 WorldDirections.West: -1
                 }
