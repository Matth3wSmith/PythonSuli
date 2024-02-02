#Egyszerű pong játék
#Start: 2024.01.31
#Kovács Máté

from tkinter import *

#ablak létrehozása
win=Tk()

jatekHatter="lightgray"

#ablak mérete
win.geometry("1000x1000")

#canvas létrehozás
canvas=Canvas(win, width=600, height=600, bg=jatekHatter)
canvas.configure()
#canvas akkora amekkora az ablak
canvas.pack(fill = BOTH, expand = 1)

win.title("Pong")

canvas.create_oval(0,0,100,100, fill="red")

win.mainloop()