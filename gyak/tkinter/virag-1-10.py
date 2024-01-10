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

virag=[0,0,
       0,300,
       100,300]


canvas.create_line(virag,width=5,fill="green")

win.mainloop()