from GUI import GUI
import tower
from tkinter import *


def call():
    tower.Hanoi(5,3)

def call1():
    gui = GUI()
    gui.run()

if __name__  == "__main__":
    root=Tk()
    root.minsize(920,790)

    img = PhotoImage(file="tag.png")
    Label(root, image=img).pack(side=TOP, pady=30)

    imghanoi = PhotoImage(file="tower.png")
    imgpuzzle = PhotoImage(file="puzzle1.png")
    Button(root, image=imghanoi, command=call).place(x=130, y=200)
    Button(root, image=imgpuzzle, command=call1).place(x=490, y=200)

    img1 = PhotoImage(file="creators.png")
    Label(root, image=img1).place(x=135, y=630)

    root.mainloop()