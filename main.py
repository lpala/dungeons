# from pprint import pprint

import random
from tkinter import Tk
from threading import Thread

from dungeons import DungeonBoard
from drawGUI import DrawMap
from mapSolver import SolveMap
from player import Player
from setups import boardHeight, boardWidth, WorldDirections, GUISetups
import tileTex


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
    dungeonCanvas = DrawMap(root, entranceRoomId, boardLimits)

    groundTiles = dungeonCanvas.createCorridors(solvedRooms, 'room', tileTex.pathTex, 'nw')
    solvedEmpties = [i for i in range(boardWidth * boardHeight) if i not in solvedRooms]

    chestTiles = dungeonCanvas.createCorridors(solvedRoomsWithItems, 'chest', tileTex.woodenChestTex, 'nw', 15, 5)
    wallTilesS = dungeonCanvas.createCorridors(solvedRooms, 'blockSouth', tileTex.blockSouth, 'center', GUISetups.rectSize // 2, 3 * GUISetups.rectSize // 2, WorldDirections.South)
    wallTilesE = dungeonCanvas.createCorridors(solvedRooms, 'blockEast', tileTex.blockWest, 'center', 3 * GUISetups.rectSize // 2 + 5, GUISetups.rectSize // 2, WorldDirections.East)
    wallTilesW = dungeonCanvas.createCorridors(solvedRooms, 'blockWest', tileTex.blockEast, 'center', -GUISetups.rectSize // 2 - 5, GUISetups.rectSize // 2, WorldDirections.West)
    wallTilesN = dungeonCanvas.createCorridors(solvedRooms, 'blockNorth', tileTex.blockNorth, 'center', GUISetups.rectSize // 2, -GUISetups.rectSize // 2, WorldDirections.North)
    chestTiles = dungeonCanvas.createCorridors(solvedRoomsWithItems, 'chest', tileTex.woodenChestTex, 'nw', 15, 5)

    dungeonCanvas.switchWallsToDecors(wallTilesN, 'blockNorthDecor', tileTex.blockNorthDecor)
    dungeonCanvas.switchWallsToDecors(groundTiles, 'pathTexDecor', tileTex.pathTexDecor)
    
    return dungeonCanvas


def createPlayer():
    player = dungeonCanvas.createPlayer(entranceRoomId)
    fogOfWar = dungeonCanvas.createFogOfWar(entranceRoomId)
    Player(player, fogOfWar, root, dungeonCanvas,
           solvedRooms, boardLimits, entranceRoomId)


def saveToJSON():
    dungeonsBoard.saveMapToJSON(dungeonsBoard)


# ----------------------PROGRAM----------------------------#


root = createTkinterRoot()

# creates empty board and defines its limits
dungeonsBoard = DungeonBoard()
boardLimits = dungeonsBoard.defineBoardLimits()

# solves the board - provides corridors and items lists
dungeonsMap = SolveMap(entranceDirection, dungeonsBoard, boardLimits)
entranceRoomId = dungeonsMap.entranceRoomId
solvedRooms = dungeonsMap.solvedRooms
solvedRoomsWithItems = dungeonsMap.roomsWithItems

# draws the map using provided lists
dungeonCanvas = drawMapAndItems()

# creates the player object
createPlayer()

# starts a thread for a fogOfWar animation
ta = Thread(target=dungeonCanvas.animateFogOfWar)
ta.setDaemon(True)
ta.start()

saveToJSON()

root.mainloop()
