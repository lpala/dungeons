# import random
from pprint import pprint
import enum
import json
# import requests


EntryDirection = enum.IntEnum('EntryDirection', 'North, South, East, West')
RoomType = enum.IntEnum('RoomType', 'Empty, Blind, TwoExits, ThreeExits, Crossroad')
RoomStatus = enum.IntEnum('RoomStatus', 'Empty, inProgress, Solved')

unsolvedRoomsIDs = set()

maxWidth = 7
maxHeight = 9
mapTiles = list()
entrance = EntryDirection.South

# --------------------DEFINITIONS---------------------------#


def createMap():
    mapSingleRoom = {
        'id': 0,
        'type': RoomType.Empty,
        'roomStatus': RoomStatus.Empty,
        'isEntrance': False,
        'X_coords': int(),
        'Y_coords': int(),
        'nExits': 0,
        'exitsDirections': ()
    }

    counter = 0
    for height in range(maxHeight):
        for width in range(maxWidth):
            tempSingleRoom = mapSingleRoom.copy()
            tempSingleRoom['id'] = counter
            tempSingleRoom['X_coords'] = width + 1
            tempSingleRoom['Y_coords'] = height + 1
            counter += 1
            mapTiles.append(tempSingleRoom)
    mapFile = {'Rooms': mapTiles}
    return (mapFile)


def defineStartingPoint(mapTiles, entrance):
    for room in mapTiles['Rooms']:
        match entrance:
            case EntryDirection.South:
                calculated_room = mapTiles['Rooms'][maxHeight * maxWidth - maxWidth // 2 - 1]
                modifyStartingPointRoomParameters(calculated_room)
                return calculated_room['id']
            case EntryDirection.North:
                calculated_room = mapTiles['Rooms'][(maxWidth) // 2 - 1]
                modifyStartingPointRoomParameters(calculated_room)
                return calculated_room['id']
            case EntryDirection.East:
                calculated_room = mapTiles['Rooms'][maxWidth * (maxHeight // 2 + 1) - 1]
                modifyStartingPointRoomParameters(calculated_room)
                return calculated_room['id']
            case EntryDirection.West:
                calculated_room = mapTiles['Rooms'][maxWidth * (maxHeight // 2)]
                modifyStartingPointRoomParameters(calculated_room)
                return calculated_room['id']


def modifyStartingPointRoomParameters(roomID):
    roomID['type'] = RoomType.Blind
    roomID['isEntrance'] = True
    roomID['roomStatus'] = RoomStatus.inProgress
    unsolvedRoomsIDs.add(roomID['id'])


def saveJSONtoFile(mapTiles):
    mapJSON = json.dumps(mapTiles, indent=4)
    with open("mapGenerated.json", "w") as outfile:
        outfile.write(mapJSON)


def visualizeMap(mapTiles):
    for height in range(1, maxHeight + 1):
        vis = [
            room["type"].value
            for room in mapTiles['Rooms']
            if room["Y_coords"] == height
        ]
        print(vis)


def drawIndexedMap(mapTiles):
    for height in range(1, maxHeight + 1):
        for width in range(1, maxWidth + 1):
            ind = [
                (f"{(room['id']):02d}")
                for room in mapTiles['Rooms']
                if room["Y_coords"] == height
            ]
        print(ind)


def solveCaves(entryDir):

    # howManyExits = random.choices([1, 2, 3], [30, 60, 10])

    directions = {
        'north': [0, -maxHeight],
        'south': [0, maxHeight],
        'east': [1, 0],
        'west': [-1, 0]
    }
    limits = {
        'north': [i for i in range(maxWidth * maxHeight) if i < maxWidth],
        'south': [i for i in range(maxWidth * maxHeight) if i >= maxWidth * maxHeight - maxWidth],
        'east': [(i * maxWidth) + maxWidth - 1 for i in range(maxHeight)],
        'west': [(i * maxWidth) for i in range(maxHeight)]
    }

    pprint(directions)
    pprint(limits)


def findPossibleDirections():
    for singleRoomID in unsolvedRoomsIDs:
        print('bede zmieniac pokoj:', mapTiles['Rooms'][singleRoomID])


# --------------------PROGRAM---------------------------#
mapTiles = createMap()
startingRoomID = defineStartingPoint(mapTiles, entrance)
print("Entrance Room ID:", startingRoomID)

visualizeMap(mapTiles)
drawIndexedMap(mapTiles)

solveCaves(entrance)

saveJSONtoFile(mapTiles)
