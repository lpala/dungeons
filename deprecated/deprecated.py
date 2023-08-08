# pyright: reportUndefinedVariable=false

def createMapElement(self, id: int, name: str, color: str, isIcon: bool = False) -> dict:

    rectSize = GUISetups.rectSize
    iconSize = GUISetups.iconSize
    margin = GUISetups.margin

    iconMargin = 0

    x0, y0, x1, y1 = (margin + (id % boardWidth) * rectSize + iconMargin,
                        margin + (id // boardWidth) * rectSize + iconMargin,
                        margin + (id % boardWidth) * rectSize + rectSize - iconMargin,
                        margin + (id // boardWidth) * rectSize + rectSize - iconMargin)

    tag = f"{name}_{id}"
    canvasID = self.mapWindow.create_rectangle(x0, y0, x1, y1,
                                                fill=color,
                                                tags=tag
                                                )
    return {tag: canvasID}


def colorizeBorders(self, roomsList, color):
    for direction in WorldDirections:
        self.colorizeRooms(roomsList[direction], color)


def colorizeRooms(self, roomsList, color):
    for roomId in roomsList:
        room = (self.mapWindow.find_withtag(f'room_{roomId}'))
        self.mapWindow.itemconfig(room, fill=color)


def colorizeMapElements():
    dungeonCanvas.colorizeBorders(boardLimits, 'dimgray')
    dungeonCanvas.colorizeRooms(dungeonsMap.solvedRooms, 'chocolate')
    dungeonCanvas.colorizeRooms([entranceRoomId], 'red')


# [dungeonCanvas.createMapElement(id, 'room', 'grey') for id in range(solvedRooms)]
# [dungeonCanvas.createMapElement(id, 'chest', 'blue', True) for id in solvedRoomsWithItems]