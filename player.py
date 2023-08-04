from drawGUI import DrawMap
from tkinter import Tk
from setups import WorldDirections, movementValue, GUISetups, boardHeight, boardWidth


class Player:
    name = str
    strenght = int
    inventory = list
    WorldDirections = WorldDirections

    def __init__(self, player, root, dungeonCanvas, solvedRooms, boardLimits, room):
        self.root = root
        self.dungeonCanvas = dungeonCanvas
        self.player = player
        self.currentRoom = room
        self.solvedRooms = solvedRooms
        self.boardLimits = boardLimits

        self.movementDistance = GUISetups.rectSize // (GUISetups.rectSize // 2)

        root.bind("<Up>", self.North)
        root.bind("<Down>", self.South)
        root.bind("<Right>", self.East)
        root.bind("<Left>", self.West)

    def North(self, event):
        if self.validateMove(WorldDirections.North):
            self.dungeonCanvas.mapWindow.move(self.player, 0, -GUISetups.rectSize)
            self.dungeonCanvas.mapWindow.yview_scroll(-self.movementDistance, 'units')
    def South(self, event):
        if self.validateMove(WorldDirections.South):
            self.dungeonCanvas.mapWindow.move(self.player, 0, GUISetups.rectSize)
            self.dungeonCanvas.mapWindow.yview_scroll(self.movementDistance, 'units')

    def East(self, event):
        if self.validateMove(WorldDirections.East):
            self.dungeonCanvas.mapWindow.move(self.player, GUISetups.rectSize, 0)
            self.dungeonCanvas.mapWindow.xview_scroll(self.movementDistance, 'units')

    def West(self,event):
        if self.validateMove(WorldDirections.West):
            self.dungeonCanvas.mapWindow.move(self.player, -GUISetups.rectSize, 0)
            self.dungeonCanvas.mapWindow.xview_scroll(-self.movementDistance, 'units')

    def validateMove(self, direction):
        if self.currentRoom in self.boardLimits[direction]:
            return False
        if self.currentRoom + movementValue[direction] in self.solvedRooms:
            print(self.currentRoom + movementValue[direction])
            self.currentRoom += movementValue[direction]
            return True
        else:
            print(self.currentRoom + movementValue[direction])
            return False