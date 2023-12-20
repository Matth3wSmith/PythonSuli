from tkinter import *
import math

#eltolás
def eltolas(pontok,x,y):
    for i in range(0,len(pontok),2):
        pontok[i]+=x
        pontok[i+1]+=y
    return pontok


#ablak létrehozása
win=Tk()

#ablak mérete
win.geometry("600x600")

#canvas létrehozás
canvas=Canvas(win, width=600, height=300)
canvas.configure(bg="lightgray")
#canvas akkora amekkora az ablak
canvas.pack(fill = BOTH, expand = 1)

pontok=[40,40,400,40,400,400,40,400,40,40]

canvas.create_line(pontok,width=5,fill="blue")
canvas.create_line(eltolas(pontok,100,200),width=5,fill="blue")


win.mainloop()

