# from pprint import pprint

import random
from dungeons import DungeonBoard
from drawGUI import DrawMap
from mapSolver import SolveMap
from player import Player
from tkinter import Tk
from setups import boardHeight, boardWidth, WorldDirections
from threading import Thread

mapTiles = list()
entranceDirection = random.choice(list(WorldDirections))


# --------------------DEFINITIONS--------------------------#


def createTkinterRoot():
    root = Tk()
    root.configure(width=400, height=450)
    windowTitle = ('Dungeons Map ' + str(boardWidth) + ' x ' + str(boardHeight))
    root.title(windowTitle)
    return root


def drawMapAndItems():
    dungeonCanvas = DrawMap(root, entranceRoomId)
    [dungeonCanvas.createMapElement(id, 'room', 'grey') for id in range(boardWidth * boardHeight)]
    [dungeonCanvas.createMapElement(id, 'chest', 'blue', True) for id in solvedRoomsWithItems]
    return dungeonCanvas


def colorizeMapElements():
    dungeonCanvas.colorizeBorders(boardLimits, 'dimgray')
    dungeonCanvas.colorizeRooms(dungeonsMap.solvedRooms, 'chocolate')
    dungeonCanvas.colorizeRooms([entranceRoomId], 'red')


def createPlayer():
    player = dungeonCanvas.createPlayer(entranceRoomId)
    fogOfWar = dungeonCanvas.createFogOfWar(entranceRoomId)
    Player(player, fogOfWar, root, dungeonCanvas, solvedRooms, boardLimits, entranceRoomId)


def saveToJSON():
    dungeonsBoard.saveMapToJSON(dungeonsBoard)


# ----------------------PROGRAM----------------------------#


root = createTkinterRoot()

# creates empty board and defines its limits
dungeonsBoard = DungeonBoard()
boardLimits = dungeonsBoard.defineBoardLimits()

# solves the board - creates corridors and items
dungeonsMap = SolveMap(entranceDirection, dungeonsBoard, boardLimits)
entranceRoomId = dungeonsMap.entranceRoomId
solvedRooms = dungeonsMap.solvedRooms
solvedRoomsWithItems = dungeonsMap.roomsWithItems

# draws the map
dungeonCanvas = drawMapAndItems()
#colorizeMapElements()

# creates the player object
createPlayer()

ta = Thread(target=dungeonCanvas.animateFogOfWar)
ta.start()

saveToJSON()

root.mainloop()
