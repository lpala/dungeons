import random
from pprint import pprint
import enum
import json
from dungeons import MapCreator
# import requests


WorldDirections = enum.IntEnum('WorldDirections', 'North, South, East, West')
RoomType = enum.IntEnum('RoomType', 'Empty, Blind, TwoExits, ThreeExits, Crossroad')
RoomStatus = enum.IntEnum('RoomStatus', 'Empty, inProgress, Solved')

unsolvedRoomsIDs = set()

maxWidth = 7
maxHeight = 5
mapTiles = list()
entranceDirection = WorldDirections.South.name

# --------------------DEFINITIONS---------------------------#


""" def defineStartingPoint(mapTiles, entranceDirection):
    for room in mapTiles['Rooms']:
        match entranceDirection:
            case WorldDirections.South:
                calculated_room = mapTiles['Rooms'][maxHeight * maxWidth - maxWidth // 2 - 1]
                modifyStartingPointRoomParameters(calculated_room)
                return calculated_room['id']
            case WorldDirections.North:
                calculated_room = mapTiles['Rooms'][(maxWidth) // 2 - 1]
                modifyStartingPointRoomParameters(calculated_room)
                return calculated_room['id']
            case WorldDirections.East:
                calculated_room = mapTiles['Rooms'][maxWidth * (maxHeight // 2 + 1) - 1]
                modifyStartingPointRoomParameters(calculated_room)
                return calculated_room['id']
            case WorldDirections.West:
                calculated_room = mapTiles['Rooms'][maxWidth * (maxHeight // 2)]
                modifyStartingPointRoomParameters(calculated_room)
                return calculated_room['id'] """


def modifyStartingPointRoomParameters(roomID):
    roomID['type'] = RoomType.Blind
    roomID['isEntrance'] = True
    roomID['roomStatus'] = RoomStatus.inProgress
    unsolvedRoomsIDs.add(roomID['id'])


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


def findPossibleDirections2(directions, limits):
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

#  for i in possibleDirections.keys():
#     unsolvedRoomsIDs.add(i)


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

dungeonsMap = MapCreator(maxWidth, maxHeight, WorldDirections)
dungeonsMap.defineBoardLimits(maxWidth, maxHeight, WorldDirections)
dungeonsMap.defineStartingPoint(entranceDirection, RoomType, RoomStatus)

dungeonsMap.createDebugMap(maxWidth, maxHeight, 'id')


print(dungeonsMap.limits)

print(dungeonsMap[31].__dict__)
print(dungeonsMap[7].__dict__)
dungeonsMap.saveMapToJSON()




""" mapTiles = createMapStructure()

startingRoomID = defineStartingPoint(mapTiles, entranceDirection)
print("Entrance Room ID:", startingRoomID)

visualizeMap(mapTiles)
drawIndexedMap(mapTiles)

solveCaves(entranceDirection)
visualizeMap(mapTiles)

saveJSONtoFile(mapTiles) """
# print (dungeons.CreateMap.createX(maxWidth, maxHeight))
