import tkinter as tk
from tkinter import Canvas, Tk, PhotoImage

root = Tk()
root.configure(width=400, height=400)

myCanvas = Canvas(root, height=300, width=300, background="gray")


photo = PhotoImage(file='Textures/ground.png')
print(photo)
groundTexture = myCanvas.create_image(0, 0, image=photo, anchor=tk.NW)
groundTexture2 = myCanvas.create_image(0, 80, image=photo, anchor=tk.NW)
groundTexture3 = myCanvas.create_image(80, 80, image=photo, anchor=tk.NW)

rockPhoto = PhotoImage(file='Textures/rock.png')
print(rockPhoto)
rockTexture = myCanvas.create_image(80, 0, image=rockPhoto, anchor=tk.NW)
rockTexture = myCanvas.create_image(80, 0, image=rockPhoto, anchor=tk.NW)

rectangle = myCanvas.create_rectangle(160, 0, 240, 80, fill='red')

myCanvas.place(x=0, y=0, width=400, height=400)

root.mainloop()
