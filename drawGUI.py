from tkinter import Canvas, Button, PhotoImage
from setups import boardWidth, boardHeight,  WorldDirections, GUISetups


class DrawMap:
    def __init__(self, root, entranceRoomId) -> None:
        print(5 * GUISetups.rectSize)
        self.mapWindow = Canvas(root,height=5 * GUISetups.rectSize, width=5 * GUISetups.rectSize)
        self.mapWindow.configure(scrollregion=(0, 0, GUISetups.rectSize * boardHeight , GUISetups.rectSize * boardWidth))
        self.mapWindow.configure(confine=False)
        #self.mapWindow.yview_moveto(GUISetups.rectSize//(boardHeight * GUISetups.rectSize) * (entranceRoomId // boardWidth))
        #self.mapWindow.xview_moveto(GUISetups.rectSize//(boardWidth * GUISetups.rectSize) * (entranceRoomId % boardWidth))
        #self.mapWindow.xview_moveto(0.5)
        #self.mapWindow.yview_moveto(0.5)
        self.mapWindow.xview_moveto(-2 * (1/boardWidth) + (entranceRoomId % boardWidth) * (1/boardWidth))
        self.mapWindow.yview_moveto(-2 * (1/boardHeight) + (entranceRoomId // boardWidth) * (1/boardHeight))
        self.mapWindow.grid()

        quitButton = Button(root, text="Quit", command=root.destroy)
        quitButton.grid()

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

        x0, y0, x1, y1 = (margin + (id % boardWidth) * rectSize + rectSize/2 + iconMargin,
                          margin + (id // boardWidth) * rectSize + rectSize/2 + iconMargin,
                          margin + (id % boardWidth) * rectSize + rectSize - iconMargin,
                          margin + (id // boardWidth) * rectSize + rectSize - iconMargin)

        self.photo = PhotoImage(file='Textures/dwarf_80px.png')
        self.playerTexture = self.mapWindow.create_image(x0, y0, image=self.photo)
        
        #self.player = self.mapWindow.create_rectangle(x0, y0, x1, y1,
        #                                           fill="yellow",
        #                                           tags='player'
        #                                           )

        print(self.playerTexture)
        
        return self.playerTexture
    
    def colorizeBorders(self, roomsList, color):
        for direction in WorldDirections:
            self.colorizeRooms(roomsList[direction], color)

    def colorizeRooms(self, roomsList, color):
        for roomId in roomsList:
            room = (self.mapWindow.find_withtag(f'room_{roomId}'))
            self.mapWindow.itemconfig(room, fill=color)
