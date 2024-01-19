from tkinter import *
import math
import random

#eltolás
def eltolas(pontok,x,y):
    for i in range(0,len(pontok),2):
        pontok[i]+=x
        pontok[i+1]+=y
    return pontok

#Nagyítás
def nagyit(pontok,x,y=-1):
    if y==-1:
        for i in range(len(pontok)):
            pontok[i]*=x
    else:
        for i in range(len(pontok)):
            if i%2==0:
                pontok[i]*=x
            else:
                pontok[i]*=y
    return pontok


def fasorsol(db):
    lista=[]
    temp=[]
    temp.append(random.randint(0,1))
    temp.append(random.randint(0,600))
    temp.append(random.randint(0,600))
    temp.append(random.randint(20,30)/100)


    return lista

#x'=cos αx - sin αy
#y'=sin αx + cos αy

#Elforgatás
def forgatPont(x,y,szog):
    x2= math.cos(math.radians(szog))*x - math.sin(math.radians(szog))*y
    y2=math.cos(math.radians(szog))*y + math.sin(math.radians(szog))*x
    return x2,y2

def forgat(lista,szog,oX="",oY=""):

    if oX=="" and oY=="":
        oX,oY=kozeppont(lista)
    elif oX=="" or oY=="":
        
        return lista
    
    else:
        lista=eltolas(lista,-oX,-oY)
        for i in range(0,len(lista),2):
            lista[i],lista[i+1]=forgatPont(lista[i],lista[i+1],szog)
        
        lista=eltolas(lista,oX,oY)
        return lista


#Középont kiszámolása; a koordináták átlag

def kozeppont(lista):
    xOssz=0
    yOssz=0
    for i in range(len(lista)):
        print(i)
        if i%2==0:
            xOssz+=lista[i]
        else:
            yOssz+=lista[i]
    x=xOssz/(len(lista)/2)
    y=yOssz/(len(lista)/2)
    return (x,y)
    

#ablak létrehozása
win=Tk()

#ablak mérete
win.geometry("1000x1000")

#canvas létrehozás
canvas=Canvas(win, width=600, height=300)
canvas.configure(bg="lightgray")
#canvas akkora amekkora az ablak
canvas.pack(fill = BOTH, expand = 1)

pontok=[40,40,400,40,400,400,40,400,40,40]

#canvas.create_line(pontok,width=5,fill="blue")
#canvas.create_line(eltolas(pontok,100,200),width=5,fill="blue")

fenyofa=[200,0,0,400,190,400,190,500,210,500,210,400,400,400,200,0]
pontok=eltolas(fenyofa,10,10)
#canvas.create_line(pontok,width=5,fill="green")

fenyo2=[200,0,
        0,100,
        150,100,
        0,200,
        150,200,
        0,300,
        150,300,
        150,400,
        250,400,
        250,300,
        400,300,
        250,200,
        400,200,
        250,100,
        400,100,
        200,0]

fenyo2=nagyit(fenyo2,0.3,0.5)
#fenyo2=forgat(fenyo2,90)
#canvas.create_line(fenyo2,width=5,fill="green")

kX,kY=kozeppont(fenyo2)
fenyo2=forgat(fenyo2,60,kX,kY)
fenyo2=eltolas(fenyo2,300,300)
canvas.create_line(fenyo2,width=4, fill="red")



win.mainloop()

