import enum
import random


'''Defines board dimensions'''
boardWidth = random.randint(10,20)
boardHeight = random.randint(10,20)

WorldDirections = enum.IntEnum('WorldDirections', 'North, South, East, West')
RoomType = enum.IntEnum('RoomType', 'Empty, Blind, TwoExits, ThreeExits, Crossroad')
RoomStatus = enum.IntEnum('RoomStatus', 'Empty, inProgress, Solved')

movementValue = {WorldDirections.North: -boardWidth,
                 WorldDirections.South: boardWidth,
                 WorldDirections.East: 1,
                 WorldDirections.West: -1
                 }
