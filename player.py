from drawGUI import DrawMap
from setups import WorldDirections, movementValue, GUISetups


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

        # self.movementDistance = int(GUISetups.rectSize / (GUISetups.rectSize / 2))
        self.movementDistance = 1

        root.bind("<Up>", self.North)
        root.bind("<Down>", self.South)
        root.bind("<Right>", self.East)
        root.bind("<Left>", self.West)

    def North(self, event):
        self.makeAMove(WorldDirections.North, 0, -GUISetups.rectSize)

    def South(self, event):
        self.makeAMove(WorldDirections.South, 0, GUISetups.rectSize)

    def East(self, event):
        self.tex = self.dungeonCanvas.displayNormalPlayerTexture()
        self.makeAMove(WorldDirections.East, GUISetups.rectSize, 0)

    def West(self, event):
        self.tex = self.dungeonCanvas.displayFlippedPlayerTexture()
        self.makeAMove(WorldDirections.West, -GUISetups.rectSize, 0)

    def makeAMove(self, WorldDirection, x, y):
        if self.validateMove(WorldDirection):
            self.dungeonCanvas.mapWindow.move(self.player, x, y)
            self.dungeonCanvas.mapWindow.move(self.fogOfWar, x, y)
            if WorldDirection == WorldDirections.North or WorldDirection == WorldDirections.South:
                self.dungeonCanvas.mapWindow.yview_scroll(int(y), 'units')
            elif WorldDirection == WorldDirections.East or WorldDirection == WorldDirections.West:
                self.dungeonCanvas.mapWindow.xview_scroll(int(x), 'units')


    def validateMove(self, direction):
        if self.currentRoom in self.boardLimits[direction]:
            return False
        if self.currentRoom + movementValue[direction] in self.solvedRooms:
            self.currentRoom += movementValue[direction]
            return True
        else:
            return False
