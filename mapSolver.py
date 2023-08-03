from setups import boardHeight, boardWidth, WorldDirections, movementValue
import random


class SolveMap:
    def __init__(self, entranceRoomId, boardLimits):

        self.boardLimits = boardLimits
        self.entranceRoomId = entranceRoomId
        self.solvedRooms = [self.entranceRoomId]
        self.solvedRooms = self.solvePath(0)

        while len(self.solvedRooms) < (boardHeight * boardWidth) // 2.5:
            self.solveAlterPaths()

        self.roomsWithItems = self.spawnItems()

    def solvePath(self, id):
        counter = 0
        currentRoom = self.solvedRooms[id]
        while counter < (2 * (boardWidth + boardHeight)):
            possibleDirections = self.findPossibleDirections(currentRoom)
            if len(possibleDirections) == 0:
                break
            dir = (random.choice(possibleDirections))
            currentRoom += movementValue[dir]
            self.solvedRooms.append(currentRoom)
            counter += 1
        return self.solvedRooms

    def solveAlterPaths(self):
        possibleAlternatives = (random.sample(self.solvedRooms, len(self.solvedRooms) // 2))
        for id in possibleAlternatives:
            self.solvePath(self.solvedRooms.index(id))

    def findPossibleDirections(self, currentRoom):
        possibleDirections = list()
        for direction in WorldDirections:
            numberOfNeighbours = self.countNeighbours((currentRoom + movementValue[direction]), self.solvedRooms)
            if currentRoom in self.boardLimits[direction]:
                continue
            elif currentRoom + movementValue[direction] in self.solvedRooms:
                continue
            elif numberOfNeighbours > 2:
                continue
            elif numberOfNeighbours == 2 and currentRoom + 2 * movementValue[direction] in self.solvedRooms:
                possibleDirections.append(direction)
            elif numberOfNeighbours == 2:
                continue
            else:
                possibleDirections.append(direction)
        return possibleDirections

    def countNeighbours(self, currentRoom, solvedRooms):
        neighbourCount = 0
        for direction in WorldDirections:
            if currentRoom + movementValue[direction] in solvedRooms:
                neighbourCount += 1
        return neighbourCount

    def spawnItems(self):
        roomsWithItems = list()
        while len(roomsWithItems) <= len(self.solvedRooms) // 6:
            pickedRoom = random.choice(self.solvedRooms)
            if self.countNeighbours(pickedRoom, roomsWithItems) == 0:
                roomsWithItems.append(pickedRoom)
        return roomsWithItems

    def calculateDistance(self):
        pass

    def verifyExits(self):
        pass
