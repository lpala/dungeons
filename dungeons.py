import json
from setups import boardHeight, boardWidth, WorldDirections


class Dungeon:
    idCounter = 0

    def __init__(self, xCoord: int, yCoord: int):
        self.id = Dungeon.idCounter
        self.roomType = 1
        self.roomStatus = 1
        self.isEntrance = False
        self.coords = [xCoord, yCoord]
        self.exitsDirections = dict()
        Dungeon.idCounter += 1
        # self.tags = ["entrance"]


'''    def isEntrance() -> bool:
        return "entrance" in self.tags'''


class DungeonBoard:

    def __init__(self):
        self.yCoords = ((i // boardWidth) + 1 for i in range(boardWidth * boardHeight))
        self.xCoords = ((i % boardWidth) + 1 for i in range(boardWidth * boardHeight))

        self.generatedDungeons = [Dungeon(next(self.xCoords), next(self.yCoords)) for _ in range(boardWidth * boardHeight)]


    def __getitem__(self, key: int):
        return self.generatedDungeons[key]

    def defineBoardLimits(self):
        self.limits = {
            WorldDirections.North: [i for i in range(boardWidth * boardHeight) if i < boardWidth],
            WorldDirections.South: [i for i in range(boardWidth * boardHeight) if i >= boardWidth * boardHeight - boardWidth],
            WorldDirections.East: [(i * boardWidth) + boardWidth - 1 for i in range(boardHeight)],
            WorldDirections.West: [(i * boardWidth) for i in range(boardHeight)]
        }
        return self.limits

    @staticmethod
    def createDebugMap(dungeonsMap: list, value: str = 'id'):
        for h in range(1, boardHeight + 1):
            for _ in range(1, boardWidth + 1):
                index = [
                    (i.__dict__)[value]
                    for i in dungeonsMap
                    if i.yCoord == h
                ]
            print(index)

    @staticmethod
    def saveMapToJSON(dungeonsMap):
        roomsList = [i.__dict__ for i in dungeonsMap]
        mapJSON = json.dumps(roomsList, indent=4)
        with open("mapGenerated.json", "w") as outfile:
            outfile.write(str(mapJSON))
