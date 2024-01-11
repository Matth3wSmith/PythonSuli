from tkinter import *
import math


win=Tk()

#ablak mérete
win.geometry("1000x1000")

#canvas létrehozás
canvas=Canvas(win, width=600, height=300)
canvas.configure(bg="lightgray")
#canvas akkora amekkora az ablak
canvas.pack(fill = BOTH, expand = 1)

teteje=[0,0,
       100,100,
       200,0,
       300,100,
       400,0,
       400,300,
       300,300,
       200,400,
       200,1000,
       200,800,
       300,800,
       500,600,
       500,500,
       200,800,
       200,700,
       400,500,
       500,500,
       200,800,
       200,700,
       100,700,
       0,600,
       0,500,
       200,700,
       200,600,
       100,500,
       0,500,
       200,700,
       200,400,
       100,300,
       300,300,
       0,300,
       0,0]

arc1=[0,200,
      100,300]


canvas.create_line(teteje,width=5,fill="green")

win.mainloop()