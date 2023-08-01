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

    def __init__(self, width: int, height: int):
        self.yCoords = ((i // width) + 1 for i in range(width * height))
        self.xCoords = ((i % width) + 1 for i in range(width * height))

        self.generatedDungeons = [Dungeon(next(self.xCoords), next(self.yCoords)) for _ in range(width * height)]


    def __getitem__(self, key):
        return self.generatedDungeons[key]


    def createDebugMap(self, width: int, height: int, value = 'id'):
        for h in range(1, height + 1):
            for _ in range(1, width + 1):
                index = [
                    (i.__dict__)[value]
                    for i in self.generatedDungeons
                    if i.yCoord == h
                ]
            print(index)


    def randomPrint(self):
        print (self.generatedDungeons[1].id)


"""     def directions(self):
        self.directions = {
            'North': -maxWidth,
            'South': maxWidth,
            'East': 1,
            'West': -1
        }

    def getBoardLimits(self):
        self.limits = {
            WorldDirections.North.name: [i for i in range(maxWidth * maxHeight) if i < maxWidth],
            WorldDirections.South.name: [i for i in range(maxWidth * maxHeight) if i >= maxWidth * maxHeight - maxWidth],
            WorldDirections.East.name: [(i * maxWidth) + maxWidth - 1 for i in range(maxHeight)],
            WorldDirections.West.name: [(i * maxWidth) for i in range(maxHeight)]
        } """
