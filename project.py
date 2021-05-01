from tkinter import *
from turtle import TurtleScreen, RawTurtle


root=Tk()
root.minsize(920,720)

img = PhotoImage(file="tag.png")
Label(root, image=img).pack(side=TOP, pady=30)

imghanoi = PhotoImage(file="tower.png")
Button(root, image=imghanoi).place(x=130, y=250)

root.mainloop()
