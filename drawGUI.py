
from tkinter import Canvas, Button, PhotoImage
from setups import boardWidth, boardHeight, GUISetups, movementValue
from PIL import Image, ImageTk
import dungeons
import time
import random


class DrawMap:
    def __init__(self, root, entranceRoomId, boardLimits) -> None:
        self.boardLimits = boardLimits

        self.root = root
        self.mapWindow = Canvas(root, background='black', height=5 * GUISetups.rectSize, width=5 * GUISetups.rectSize)
        self.mapWindow.configure(scrollregion=(0, 0, GUISetups.rectSize * boardHeight, GUISetups.rectSize * boardWidth))
        self.mapWindow.configure(confine=False)
        self.mapWindow.configure(xscrollincrement=1, yscrollincrement=1)
        self.mapWindow.xview_moveto(-2 * (1 / boardWidth) + (entranceRoomId % boardWidth) * (1 / boardWidth))
        self.mapWindow.yview_moveto(-2 * (1 / boardHeight) + (entranceRoomId // boardWidth) * (1 / boardHeight))
        self.mapWindow.place(x=0, y=0, width=400, height=400)

        quitButton = Button(root, text="Quit", command=root.destroy)
        quitButton.place(x=200, y=410)

    def createCorridors(self, roomsList, name: str, texturePath, anchor, xMargin=0, yMargin=0, wallSide=False):
        generatedImagesList = dict()
        textureFile = "self.tex_" + name
        globals()[textureFile] = PhotoImage(file=texturePath)
        roomsList.sort
        for i in roomsList:
            if wallSide:
                print (wallSide)
                if i + movementValue[wallSide] in roomsList and i not in self.boardLimits[wallSide]:
                    print ('jest sciezka:', i)
                    continue

            x0, y0, = ((i % boardWidth) * GUISetups.rectSize,
                    (i // boardWidth) * GUISetups.rectSize + 30)
            tag = f"{name}_{i}"
            tile = self.mapWindow.create_image(x0 + xMargin, y0 + yMargin, image=globals()[textureFile], anchor=anchor)
            generatedImagesList.update({tag: tile})

        return generatedImagesList


    def switchWallsToDecors(self, wallsList, name, texturePath):
         chanceForDecor = 10
         textureFile = "self.tex_" + name
         globals()[textureFile] = PhotoImage(file=texturePath)
         for i in random.sample(sorted(wallsList.values()), len(wallsList.values()) // chanceForDecor):
             self.mapWindow.itemconfigure(tagOrId=i, image=globals()[textureFile])


    def createPlayer(self, id):

        rectSize = GUISetups.rectSize

        x0, y0, = ((id % boardWidth) * rectSize + rectSize // 2,
                   (id // boardWidth) * rectSize + rectSize // 2)

        self.pil_playerImage = Image.open('Textures/dwarf_80px.png')
        self.pil_playerImageFlipped = self.pil_playerImage.transpose(Image.FLIP_LEFT_RIGHT)
        self.playerImage = ImageTk.PhotoImage(self.pil_playerImage)
        self.playerImageFlipped = ImageTk.PhotoImage(self.pil_playerImageFlipped)
        self.playerTexture = self.mapWindow.create_image(x0, y0, image=self.playerImage)

        print('player:', x0, y0)
        return self.playerTexture

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
        for i in range(1, 5):
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
