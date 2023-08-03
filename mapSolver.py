from setups import *
import random
import dungeons

class SolveMap:
    def __init__(self, entranceRoomId, boardLimits):
        self.maxWidth = boardWidth
        self.maxHeight = boardHeight
        self.WorldDirections = WorldDirections
        self.boardLimits = boardLimits
        self.entranceRoomId = entranceRoomId
        self.movementValue = movementValue
        self.solvedRooms = [self.entranceRoomId]
        self.solvedRooms = self.solvePath(0)

        while len(self.solvedRooms) < (boardHeight * boardWidth) // 2.5:
            self.solveAlterPaths()

        self.roomsWithItems = self.spawnItems()

    def solvePath(self, id):
        counter = 0
        currentRoom = self.solvedRooms[id]
        while counter < (2 * (self.maxWidth + self.maxHeight)):
            possibleDirections = self.findPossibleDirections(currentRoom)
            if len(possibleDirections) == 0:
                break
            dir = (random.choice(possibleDirections))
            currentRoom += self.movementValue[dir]
            self.solvedRooms.append(currentRoom)
            counter += 1
        return self.solvedRooms

    def solveAlterPaths(self):
        possibleAlternatives = (random.sample(self.solvedRooms, len(self.solvedRooms) // 2))
        for id in possibleAlternatives:
            self.solvePath(self.solvedRooms.index(id))

    def findPossibleDirections(self, currentRoom):
        possibleDirections = list()
        for direction in self.WorldDirections:
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
        for direction in self.WorldDirections:
            if currentRoom + movementValue[direction] in solvedRooms:
                neighbourCount += 1
        return neighbourCount

    def spawnItems(self):
        roomsWithItems = list()
        while len(roomsWithItems) <= len(self.solvedRooms) // 6:
            pickedRoom = random.choice(self.solvedRooms)
            if self.countNeighbours(pickedRoom, movementValue, roomsWithItems) == 0:
                roomsWithItems.append(pickedRoom)
        # [DrawMap().drawChestsIcons(self, self.maxWidth, id, 'skyblue') for id in roomsWithItems]
        return roomsWithItems

    def verifyExits(self):
        pass
