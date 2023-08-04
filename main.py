# from pprint import pprint

import random
from dungeons import DungeonBoard
from drawGUI import DrawMap
from mapSolver import SolveMap
from player import Player


from tkinter import Tk
from setups import boardHeight, boardWidth, WorldDirections


# --------------------DEFINITIONS--------------------------#


# ----------------------PROGRAM----------------------------#
mapTiles = list()
entranceDirection = random.choice(list(WorldDirections))

root = Tk()

dungeonsBoard = DungeonBoard()
boardLimits = dungeonsBoard.defineBoardLimits()

dungeonsMap = SolveMap(entranceDirection, dungeonsBoard, boardLimits)

entranceRoomId = dungeonsMap.entranceRoomId
print('entrance:', entranceRoomId, "width:", boardWidth)
solvedRooms = dungeonsMap.solvedRooms
solvedRoomsWithItems = dungeonsMap.roomsWithItems

dungeonCanvas = DrawMap(root, entranceRoomId)
createMapRects = [dungeonCanvas.createMapElement(id, 'room', 'grey') for id in range(boardWidth * boardHeight)]
createItemIcons = [dungeonCanvas.createMapElement(id, 'chest', 'blue', True) for id in solvedRoomsWithItems]

dungeonCanvas.colorizeBorders(boardLimits, 'dimgray')
dungeonCanvas.colorizeRooms(dungeonsMap.solvedRooms, 'chocolate')
dungeonCanvas.colorizeRooms([entranceRoomId], 'red')

player = dungeonCanvas.createPlayer(entranceRoomId)
Player(player, root, dungeonCanvas, solvedRooms, boardLimits, entranceRoomId)

dungeonsBoard.saveMapToJSON(dungeonsBoard)

windowTitle = ('Dungeons Map ' + str(boardWidth) + ' x ' + str(boardHeight))

root.title(windowTitle)
root.mainloop()

# dungeonCanvas.colorizeRooms(solvedMap.roomsWithItems, 'yellow')
# dungeonCanvas.drawChestsIcons(maxWidth, 20, 'red')
# dungeonCanvas.colorizeEntrance(entranceRoomId)
# dungeonsMap.createDebugMap(dungeonsMap, 'id')
# dungeonsMap.createDebugMap(maxWidth, maxHeight, 'roomStatus')
# print(dungeonsMap[31].__dict__)
