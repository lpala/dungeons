from tkinter import Canvas, Button, PhotoImage
from setups import boardWidth, boardHeight, WorldDirections, GUISetups
from PIL import Image, ImageTk
import time
import random


class DrawMap:
    def __init__(self, root, entranceRoomId) -> None:
        self.root = root
        self.mapWindow = Canvas(root, background='dimgray', height=5 * GUISetups.rectSize, width=5 * GUISetups.rectSize)
        self.mapWindow.configure(scrollregion=(0, 0, GUISetups.rectSize * boardHeight, GUISetups.rectSize * boardWidth))
        self.mapWindow.configure(confine=False)
        self.mapWindow.configure(xscrollincrement=1, yscrollincrement=1)
        self.mapWindow.xview_moveto(-2 * (1 / boardWidth) + (entranceRoomId % boardWidth) * (1 / boardWidth))
        self.mapWindow.yview_moveto(-2 * (1 / boardHeight) + (entranceRoomId // boardWidth) * (1 / boardHeight))
        self.mapWindow.place(x=0, y=0, width=400, height=400)

        quitButton = Button(root, text="Quit", command=root.destroy)
        quitButton.place(x=200, y=410)

    def createMapElement(self, id: int, name: str, color: str, isIcon: bool = False) -> dict:

        rectSize = GUISetups.rectSize
        iconSize = GUISetups.iconSize
        margin = GUISetups.margin

        iconMargin = 0
        if isIcon:
            iconMargin = (rectSize - iconSize) / 2

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

    def createPlayer(self, id):

        rectSize = GUISetups.rectSize
        playerSize = GUISetups.playerSize
        margin = GUISetups.margin
        iconMargin = (rectSize - playerSize) / 2

        x0, y0, = (margin + (id % boardWidth) * rectSize + rectSize / 2 + iconMargin,
                   margin + (id // boardWidth) * rectSize + rectSize / 2 + iconMargin)

        self.pil_playerImage = Image.open('Textures/dwarf_80px.png')
        self.pil_playerImageFlipped = self.pil_playerImage.transpose(Image.FLIP_LEFT_RIGHT)
        self.playerImage = ImageTk.PhotoImage(self.pil_playerImage)
        self.playerImageFlipped = ImageTk.PhotoImage(self.pil_playerImageFlipped)
        self.playerTexture = self.mapWindow.create_image(x0, y0, image=self.playerImage)

        return self.playerTexture
        self.mapWindow.s
    def displayFlippedPlayerTexture(self):
        self.mapWindow.itemconfigure(self.playerTexture, image=self.playerImageFlipped)
        return self.playerTexture

    def displayNormalPlayerTexture(self):
        self.mapWindow.itemconfigure(self.playerTexture, image=self.playerImage)
        return self.playerTexture

    def createFogOfWar(self, id):

        rectSize = GUISetups.rectSize
        playerSize = GUISetups.playerSize
        margin = GUISetups.margin
        iconMargin = (rectSize - playerSize) / 2

        x0, y0, = (margin + (id % boardWidth) * rectSize + rectSize / 2 + iconMargin,
                   margin + (id // boardWidth) * rectSize + rectSize / 2 + iconMargin)

        self.fog = PhotoImage(file='Textures/fog_01.png')
        self.fogOfWarTexture = self.mapWindow.create_image(x0, y0, image=self.fog)

        return self.fogOfWarTexture
    
    def animateFogOfWar(self):    
        for i in range(1,5):
            self.fog_01 = PhotoImage(file='Textures/fog_01.png')
            self.fog_02 = PhotoImage(file='Textures/fog_02.png')
            self.fog_03 = PhotoImage(file='Textures/fog_03.png')
            self.fog_04 = PhotoImage(file='Textures/fog_04.png')
        self.fogOfWarImages = [self.fog_01, self.fog_02, self.fog_03, self.fog_04]
        while True:
            randomFog = random.choice(self.fogOfWarImages)   
            self.mapWindow.itemconfigure(self.fogOfWarTexture, image=randomFog)
            self.root.update()
            time.sleep(0.2)

    def colorizeBorders(self, roomsList, color):
        for direction in WorldDirections:
            self.colorizeRooms(roomsList[direction], color)

    def colorizeRooms(self, roomsList, color):
        for roomId in roomsList:
            room = (self.mapWindow.find_withtag(f'room_{roomId}'))
            self.mapWindow.itemconfig(room, fill=color)
