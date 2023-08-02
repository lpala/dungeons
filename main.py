from pprint import pprint
import random
import enum
from dungeons import MapCreator

from dungeonsGUI import DrawMap
from tkinter import *

# import requests

maxWidth = 15
maxHeight = 11
mapTiles = list()

WorldDirections = enum.IntEnum('WorldDirections', 'North, South, East, West')
RoomType = enum.IntEnum('RoomType', 'Empty, Blind, TwoExits, ThreeExits, Crossroad')
RoomStatus = enum.IntEnum('RoomStatus', 'Empty, inProgress, Solved')

movementValue = {WorldDirections.North.name: -maxWidth,
                 WorldDirections.South.name: maxWidth,
                 WorldDirections.East.name: 1,
                 WorldDirections.West.name: -1
                 }

unsolvedRoomsIDs = set()
entranceDirection = WorldDirections.South.name

# --------------------DEFINITIONS---------------------------#

# unsolvedRoomsIDs.add(roomID['id'])
def corridorSolver(entranceRoomId, boardLimits):
    counter = 0
    currentRoom = entranceRoomId
    solvedRooms = [entranceRoomId]
    while counter < 20:
        
        possibleDirections = list()
        for direction in WorldDirections._member_names_:
            
            if currentRoom in boardLimits[direction]:
                continue
            elif currentRoom + movementValue[direction] in solvedRooms:
                continue
            elif checkIfNeighbour((currentRoom + movementValue[direction]), movementValue[direction], movementValue, solvedRooms): #tu jest blad
                print('nejbor!')
                continue
            else:
                possibleDirections.append(direction)
        print(currentRoom, possibleDirections) 
        dir = (random.choice(possibleDirections))
        currentRoom +=  movementValue[dir]
        solvedRooms.append(currentRoom)
        counter += 1
    return solvedRooms

def checkIfNeighbour(currentRoom, movement, movementValue, solvedRooms):

    hasNeighbour = False
    for direction in WorldDirections._member_names_:
        if currentRoom - movement in solvedRooms: #zawsze prawdziwy
            print (currentRoom - movement)
            continue
        if currentRoom + movementValue[direction] in solvedRooms:
            hasNeighbour = True
            print('tu tez')
    print (hasNeighbour)
    return hasNeighbour

""" def solveCaves(entryDir):

    # howManyExits = random.choices([1, 2, 3], [30, 60, 10])

    pprint(limits)
    for i in range(12):
        if len(unsolvedRoomsIDs) > 0:
            print('UnsolvedRoomsIDs:', unsolvedRoomsIDs)
            findPossibleDirections(directions, limits)
    verifyExits(directions, limits) """


def solveMainPath(directions, limits):
    for iterationStep in range(1.5 * ((maxHeight + maxWidth) // 2)):
        pass


def findPossibleDirections(directions, limits):
    tempUnsolvedRoomID = set()
    for singleRoomID in unsolvedRoomsIDs:
        possibleDirections = dict()
        for direction in WorldDirections._member_names_:
            if singleRoomID not in limits[direction]:
                searchedRoomID = singleRoomID + directions[direction]
            else:
                continue

            if mapTiles['Rooms'][searchedRoomID]['roomStatus'] == RoomStatus.Solved:
                continue
            else:
                if random.random() > 0.45:
                    possibleDirections[searchedRoomID] = direction
                    mapTiles['Rooms'][singleRoomID]['exitsDirections'] = possibleDirections
                    mapTiles['Rooms'][singleRoomID]['type'] = RoomType.Blind
                    tempUnsolvedRoomID.add(searchedRoomID)
                    mapTiles['Rooms'][searchedRoomID]['roomStatus'] = RoomStatus.inProgress
                else:
                    mapTiles['Rooms'][searchedRoomID]['roomStatus'] == RoomStatus.Solved
        print('Possible directions:', possibleDirections)
        mapTiles['Rooms'][singleRoomID]['roomStatus'] = RoomStatus.Solved
    unsolvedRoomsIDs.clear()
    for i in tempUnsolvedRoomID:
        unsolvedRoomsIDs.add(i)
    tempUnsolvedRoomID.clear()


def verifyExits(directions, limits):
    for oneRoom in mapTiles['Rooms']:
        oneRoom['exitsDirections'] = dict()
        for direction in WorldDirections._member_names_:
            if oneRoom['id'] not in limits[direction] and oneRoom['type'] == RoomType.Blind:
                searchedRoomID = oneRoom['id'] + directions[direction]
                if mapTiles['Rooms'][searchedRoomID]['type'] == RoomType.Blind:
                    print(oneRoom['id'], "szukam kierunku", searchedRoomID)
                    oneRoom['exitsDirections'][searchedRoomID] = direction


# --------------------PROGRAM---------------------------#
root = Tk()
root.title('Dungeons Map')

dungeonsMap = MapCreator(maxWidth, maxHeight, WorldDirections)
boardLimits = dungeonsMap.defineBoardLimits(maxWidth, maxHeight, WorldDirections)
entranceRoomId = dungeonsMap.defineStartingPoint(entranceDirection, RoomStatus)
print('Entrance room:', entranceRoomId)

dungeonsMap.saveMapToJSON()

solvedRooms = corridorSolver(entranceRoomId, boardLimits)


newgui = DrawMap(root, maxWidth, maxHeight)

newgui.colorizeBorders(dungeonsMap.limits, WorldDirections)
newgui.colorizeSolved(solvedRooms)
newgui.colorizeEntrance(entranceRoomId)


root.mainloop()

# dungeonsMap.createDebugMap(maxWidth, maxHeight, 'id')
# dungeonsMap.createDebugMap(maxWidth, maxHeight, 'roomStatus')
# print(dungeonsMap[31].__dict__)
