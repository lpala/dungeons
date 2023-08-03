from tkinter import Canvas, Button
from setups import boardWidth, WorldDirections


class DrawMap:
    def __init__(self, root, boardWidth, boardHeight) -> None:
        self.rectSize = 40
        self.iconSize = 20
        self.margin = 10

        self.mapWindow = Canvas(root, height=boardHeight * self.rectSize + 20, width=boardWidth * self.rectSize + 20)
        self.mapWindow.grid()

        quitButton = Button(root, text="Quit", command=root.destroy)
        quitButton.grid()

    def createMapElement(self, id, name, color, isIcon=False) -> int:

        rectSize = self.rectSize
        iconSize = self.iconSize
        margin = self.margin

        iconMargin = 0
        if isIcon:
            iconMargin = (rectSize - iconSize / 2)

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
