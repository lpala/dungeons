from tkinter import *
from tkinter import ttk




class DrawMap:
    def __init__(self, root, maxWidth, maxHeight) -> None:
        rectSize = 40

        self.mapWindow = Canvas(root, height=maxHeight * rectSize + 20, width=maxWidth * rectSize + 20)
        self.mapWindow.grid()

        quitButton = Button(root, text="Quit", command=root.destroy)
        quitButton.grid()

        self.yCoords = ((i // maxWidth) + 1 for i in range(maxWidth * maxHeight))
        self.xCoords = ((i % maxWidth) + 1 for i in range(maxWidth * maxHeight))
        self.id = (i for i in range(maxWidth * maxHeight))
        self.rectMap = [self.createMapArray(next(self.xCoords), next(self.yCoords), next(self.id), rectSize) for _ in range(maxWidth * maxHeight)]

    def createMapArray(self, w, h, id, rectSize):
        counter = id
        self.mapWindow.create_rectangle(10 + (w - 1) * rectSize,
                                        10 + (h - 1) * rectSize,
                                        10 + rectSize + (w - 1) * rectSize,
                                        10 + rectSize + (h - 1) * rectSize,
                                        fill='silver',
                                        tags=f"square_{counter}"
                                        )

    def colorizeBorders(self, limits, WorldDirections):
        for direction in WorldDirections._member_names_:
            for i in limits[direction]:
                border = (self.mapWindow.find_withtag(f'square_{i}'))
                self.mapWindow.itemconfig(border, fill='dimgray')

    def colorizeSolved(self, solvedRooms):
        for roomId in solvedRooms:
            solvedRoom = (self.mapWindow.find_withtag(f'square_{roomId}'))
            self.mapWindow.itemconfig(solvedRoom, fill='green')

    def colorizeEntrance(self, entranceRoomId):
        entrance = (self.mapWindow.find_withtag(f'square_{entranceRoomId}'))
        self.mapWindow.itemconfig(entrance, fill='red')
