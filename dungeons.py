class Dungeon:
    idCounter = 0

    def __init__(self, xCoord, yCoord):
        self.id = Dungeon.idCounter
        self.roomType = 'Empty'
        self.roomStatus = 'Empty'
        self.isEntrance = False
        self.xCoord = xCoord
        self.yCoord = yCoord
        self.nExits = 0
        self.exitsDirections = dict()
        Dungeon.idCounter += 1


class MapCreator:

    def __init__(self, width: int, height: int, WorldDirections):
        self.yCoords = ((i // width) + 1 for i in range(width * height))
        self.xCoords = ((i % width) + 1 for i in range(width * height))

        self.generatedDungeons = [Dungeon(next(self.xCoords), next(self.yCoords)) for _ in range(width * height)]


    def __getitem__(self, key):
        return self.generatedDungeons[key]

    def defineBoardLimits(self, width: int, height: int, WorldDirections):
        self.limits = {
            WorldDirections.North.name: [i for i in range(width * height) if i < width],
            WorldDirections.South.name: [i for i in range(width * height) if i >= width * height - width],
            WorldDirections.East.name: [(i * width) + width - 1 for i in range(height)],
            WorldDirections.West.name: [(i * width) for i in range(height)]
        }

    def defineStartingPoint(self, entranceDirection):
        counter = (len(self.limits[entranceDirection]))// 2
        entranceRoomId = self.limits[entranceDirection][counter]
        self.generatedDungeons[entranceRoomId].isEntrance = True
        print('side with entrance', entranceRoomId)


    def createDebugMap(self, width: int, height: int, value = 'id'):
        """Calculate and draws the debug map with values
        """

        for h in range(1, height + 1):
            for _ in range(1, width + 1):
                index = [
                    (i.__dict__)[value]
                    for i in self.generatedDungeons
                    if i.yCoord == h
                ]
            print(index)