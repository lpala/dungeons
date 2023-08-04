from tkinter import Canvas, Tk, PhotoImage

root = Tk()

myCanvas = Canvas(root, height=300, width=300, background="gray")


player = myCanvas.create_rectangle(0, 0, 150, 150,
                                                   fill="yellow",
                                                   tags='player'
                                                   )


photo = PhotoImage(file='Textures/dwarf.png')
playerTexture = myCanvas.create_image(150, 150, image=photo)

myCanvas.grid()

root.mainloop()