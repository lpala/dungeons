from tkinter import Canvas, Button
# from tkineter import ttk
# from tkinter import *
import random


class DrawMap:
    def __init__(self, root, maxWidth, maxHeight) -> None:
        rectSize = 40

        self.mapWindow = Canvas(root, height=maxHeight * rectSize + 20, width=maxWidth * rectSize + 20)
        self.mapWindow.grid()

        quitButton = Button(root, text="Quit", command=root.destroy)
        quitButton.grid()

        self.yCoords = ((i // maxWidth) + 1 for i in range(maxWidth * maxHeight))
        self.xCoords = ((i % maxWidth) + 1 for i in range(maxWidth * maxHeight))
        self.id = (i for i in range(maxWidth * maxHeight))
        self.rectMap = [self.createMapArray(next(self.xCoords), next(self.yCoords), next(self.id), rectSize) for _ in range(maxWidth * maxHeight)]

    def createMapArray(self, w, h, id, rectSize):
        counter = id
        self.mapWindow.create_rectangle(10 + (w - 1) * rectSize,
                                        10 + (h - 1) * rectSize,
                                        10 + rectSize + (w - 1) * rectSize,
                                        10 + rectSize + (h - 1) * rectSize,
                                        fill='silver',
                                        tags=f"square_{counter}"
                                        )

    def colorizeBorders(self, limits, WorldDirections):
        for direction in WorldDirections._member_names_:
            for i in limits[direction]:
                border = (self.mapWindow.find_withtag(f'square_{i}'))
                self.mapWindow.itemconfig(border, fill='dimgray')

    def colorizeSolved(self, solvedRooms):
        for roomId in solvedRooms:
            solvedRoom = (self.mapWindow.find_withtag(f'square_{roomId}'))
            self.mapWindow.itemconfig(solvedRoom, fill='green')

    def colorizeEntrance(self, entranceRoomId):
        entrance = (self.mapWindow.find_withtag(f'square_{entranceRoomId}'))
        self.mapWindow.itemconfig(entrance, fill='red')


class SolveMap:
    def __init__(self, entranceRoomId, boardLimits, WorldDirections, movementValue, maxHeight, maxWidth):
        self.maxWidth = maxWidth
        self.maxHeight = maxHeight
        self.WorldDirections = WorldDirections
        self.boardLimits = boardLimits
        self.entranceRoomId = entranceRoomId
        self.movementValue = movementValue
        self.solvedRooms = [self.entranceRoomId]
        self.solvedRooms = self.solvePath(0)
        self.solveAlterPaths()
        self.solveAlterPaths()
        self.solveAlterPaths()

    def solvePath(self, id):
        counter = 0
        currentRoom = self.solvedRooms[id]
        while counter < (2 * (self.maxWidth + self.maxHeight)):
            possibleDirections = self.findPossibleDirections(currentRoom)
            if len(possibleDirections) == 0:
                print('path has died :(')
                break
            print(currentRoom, possibleDirections)
            dir = (random.choice(possibleDirections))
            currentRoom += self.movementValue[dir]
            self.solvedRooms.append(currentRoom)
            counter += 1
        return self.solvedRooms

    def solveAlterPaths(self):
        possibleAlternatives = (random.sample(self.solvedRooms, 30))
        for id in possibleAlternatives:
            self.solvePath(self.solvedRooms.index(id))

    def findPossibleDirections(self, currentRoom):
        possibleDirections = list()
        for direction in self.WorldDirections._member_names_:
            numberOfNeighbours = self.countNeighbours((currentRoom + self.movementValue[direction]), self.movementValue, self.solvedRooms)
            if currentRoom in self.boardLimits[direction]:
                continue
            elif currentRoom + self.movementValue[direction] in self.solvedRooms:
                continue
            elif numberOfNeighbours > 2:
                continue
            elif numberOfNeighbours == 2 and currentRoom + 2 * self.movementValue[direction] in self.solvedRooms:
                possibleDirections.append(direction)
            elif numberOfNeighbours == 2:
                continue
            else:
                possibleDirections.append(direction)
        return possibleDirections

    def countNeighbours(self, currentRoom, movementValue, solvedRooms):
        neighbourCount = 0
        for direction in self.WorldDirections._member_names_:
            if currentRoom + movementValue[direction] in solvedRooms:
                neighbourCount += 1
        return neighbourCount
