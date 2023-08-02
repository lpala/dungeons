from pprint import pprint

import enum
import random
from dungeons import MapCreator

from dungeonsGUI import DrawMap, SolveMap
from tkinter import *

# import requests

maxWidth = 14
maxHeight = 7
mapTiles = list()

WorldDirections = enum.IntEnum('WorldDirections', 'North, South, East, West')
RoomType = enum.IntEnum('RoomType', 'Empty, Blind, TwoExits, ThreeExits, Crossroad')
RoomStatus = enum.IntEnum('RoomStatus', 'Empty, inProgress, Solved')

movementValue = {WorldDirections.North.name: -maxWidth,
                 WorldDirections.South.name: maxWidth,
                 WorldDirections.East.name: 1,
                 WorldDirections.West.name: -1
                 }

# entranceDirection = WorldDirections.South.name
entranceDirection = random.choice(WorldDirections._member_names_)

# --------------------DEFINITIONS---------------------------#


def verifyExits(directions, limits):
    for oneRoom in mapTiles['Rooms']:
        oneRoom['exitsDirections'] = dict()
        for direction in WorldDirections._member_names_:
            if oneRoom['id'] not in limits[direction] and oneRoom['type'] == RoomType.Blind:
                searchedRoomID = oneRoom['id'] + directions[direction]
                if mapTiles['Rooms'][searchedRoomID]['type'] == RoomType.Blind:
                    print(oneRoom['id'], "szukam kierunku", searchedRoomID)
                    oneRoom['exitsDirections'][searchedRoomID] = direction


# --------------------PROGRAM---------------------------#
root = Tk()
root.title('Dungeons Map')

dungeonsMap = MapCreator(maxWidth, maxHeight)
boardLimits = dungeonsMap.defineBoardLimits(maxWidth, maxHeight, WorldDirections)
entranceRoomId = dungeonsMap.defineStartingPoint(entranceDirection, RoomStatus)

dungeonsMap.saveMapToJSON()

solvedMap = SolveMap(entranceRoomId, boardLimits, WorldDirections, movementValue, maxHeight, maxWidth)
solvedRooms = solvedMap.solvedRooms

dungeonCanvas = DrawMap(root, maxWidth, maxHeight)

dungeonCanvas.colorizeBorders(dungeonsMap.limits, WorldDirections)
dungeonCanvas.colorizeSolved(solvedRooms)
dungeonCanvas.colorizeEntrance(entranceRoomId)

root.mainloop()

# dungeonsMap.createDebugMap(maxWidth, maxHeight, 'id')
# dungeonsMap.createDebugMap(maxWidth, maxHeight, 'roomStatus')
# print(dungeonsMap[31].__dict__)
