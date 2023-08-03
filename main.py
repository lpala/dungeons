# from pprint import pprint

import random
from dungeons import CreateBaseMap
from drawGUI import DrawMap
from mapSolver import SolveMap

from tkinter import Tk
from setups import boardHeight, boardWidth, WorldDirections, RoomType


# --------------------DEFINITIONS---------------------------#


def verifyExits(directions, limits):
    for oneRoom in mapTiles['Rooms']:
        oneRoom['exitsDirections'] = dict()
        for direction in WorldDirections:
            if oneRoom['id'] not in limits[direction] and oneRoom['type'] == RoomType.Blind:
                searchedRoomID = oneRoom['id'] + directions[direction]
                if mapTiles['Rooms'][searchedRoomID]['type'] == RoomType.Blind:
                    print(oneRoom['id'], "szukam kierunku", searchedRoomID)
                    oneRoom['exitsDirections'][searchedRoomID] = direction


# --------------------PROGRAM---------------------------#
mapTiles = list()
entranceDirection = random.choice(list(WorldDirections))

root = Tk()
root.title('Dungeons Map')

dungeonsMap = CreateBaseMap()
boardLimits = dungeonsMap.defineBoardLimits()
entranceRoomId = dungeonsMap.defineStartingPoint(entranceDirection)

solvedMap = SolveMap(entranceRoomId, boardLimits)
solvedRooms = solvedMap.solvedRooms
solvedRoomsWithItems = solvedMap.roomsWithItems

dungeonCanvas = DrawMap(root, boardWidth, boardHeight)
rectMap = [dungeonCanvas.createMapElement(id, 'room', 'grey') for id in range(boardWidth * boardHeight)]
itemIcons = [dungeonCanvas.createMapElement(id, 'chest', 'blue', True) for id in solvedRoomsWithItems]
print(rectMap)
print(itemIcons)
dungeonCanvas.colorizeBorders(boardLimits, 'dimgray')
dungeonCanvas.colorizeRooms(solvedMap.solvedRooms, 'chocolate')
dungeonCanvas.colorizeRooms([entranceRoomId], 'red')

dungeonsMap.saveMapToJSON(dungeonsMap)

root.mainloop()

# dungeonCanvas.colorizeRooms(solvedMap.roomsWithItems, 'yellow')
# dungeonCanvas.drawChestsIcons(maxWidth, 20, 'red')
# dungeonCanvas.colorizeEntrance(entranceRoomId)
# dungeonsMap.createDebugMap(dungeonsMap, 'id')
# dungeonsMap.createDebugMap(maxWidth, maxHeight, 'roomStatus')
# print(dungeonsMap[31].__dict__)
