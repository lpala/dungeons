from setups import WorldDirections, movementValue, GUISetups
import time


class Player:
    name = str
    strenght = int
    inventory = list
    WorldDirections = WorldDirections

    def __init__(self, player, fogOfWar, root, dungeonCanvas, solvedRooms, boardLimits, room):
        self.root = root
        self.dungeonCanvas = dungeonCanvas
        self.player = player
        self.fogOfWar = fogOfWar
        self.currentRoom = room
        self.solvedRooms = solvedRooms
        self.boardLimits = boardLimits
        self.isInMotion = False

        self.timeDivider = 10

        root.bind("<Up>", self.North)
        root.bind("<Down>", self.South)
        root.bind("<Right>", self.East)
        root.bind("<Left>", self.West)

    def North(self, event):
        if not self.isInMotion:
            self.makeAMove(WorldDirections.North, 0, -GUISetups.rectSize // self.timeDivider)

    def South(self, event):
        if not self.isInMotion:
            self.makeAMove(WorldDirections.South, 0, GUISetups.rectSize // self.timeDivider)

    def East(self, event):
        if not self.isInMotion:
            self.tex = self.dungeonCanvas.displayNormalPlayerTexture()
            self.makeAMove(WorldDirections.East, GUISetups.rectSize // self.timeDivider, 0)

    def West(self, event):
        if not self.isInMotion:
            self.tex = self.dungeonCanvas.displayFlippedPlayerTexture()
            self.makeAMove(WorldDirections.West, -GUISetups.rectSize // self.timeDivider, 0)

    def makeAMove(self, WorldDirection, x, y):
        counter = 0

        if self.validateMove(WorldDirection):
            self.isInMotion = True
            while counter < 10:
                self.dungeonCanvas.mapWindow.move(self.player, x, y)
                self.dungeonCanvas.mapWindow.move(self.fogOfWar, x, y)
                if WorldDirection == WorldDirections.North or WorldDirection == WorldDirections.South:
                    self.dungeonCanvas.mapWindow.yview_scroll(int(y), 'units')
                elif WorldDirection == WorldDirections.East or WorldDirection == WorldDirections.West:
                    self.dungeonCanvas.mapWindow.xview_scroll(int(x), 'units')
                self.root.update()
                time.sleep(0.03)
                counter += 1
            self.isInMotion = False

    def validateMove(self, direction):
        if self.currentRoom in self.boardLimits[direction]:
            return False
        if self.currentRoom + movementValue[direction] in self.solvedRooms:
            self.currentRoom += movementValue[direction]
            return True
        else:
            return False
