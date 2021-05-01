from tkinter import *
from turtle import TurtleScreen, RawTurtle

class HanoiEngine:
    def __init__(self, cv, nd, speed):
        self.ts = cv
        self.ts.tracer(False)
        self.designer = RawTurtle(cv, shape="square")
        self.designer.penup()
        self.designer.shapesize(0.5,21)
        self.designer.goto(0,-100)
        self.designer.stamp()
        self.designer.shapesize(7,0.5)
        self.designer.fillcolor("red")
        for x in -140, 0,140:
            self.designer.goto(x,-5);
            self.designer.stamp()
        self.ts.tracer(True)

class Hanoi:
    def __init__(self, nd, speed):
        root=Tk()
        root.title("Tower of Hanoi")
        cv=Canvas(root, width=440, height=210)
        cv.pack()
        cv=TurtleScreen(cv)
        HanoiEngine(cv,nd,speed)


        root.mainloop()
        



# def call():
#     Hanoi(5,3)

if __name__=="__main__":
    Hanoi(5,3)
    # root=Tk()
    # root.minsize(920,720)

    # img = PhotoImage(file="tag.png")
    # Label(root, image=img).pack(side=TOP, pady=30)

    # imghanoi = PhotoImage(file="tower.png")
    # Button(root, image=imghanoi, command=call).place(x=130, y=250)

    # root.mainloop()