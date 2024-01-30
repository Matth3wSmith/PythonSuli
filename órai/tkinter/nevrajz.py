import transzformaciok
from tkinter import *

#ablak létrehozása
win=Tk()

#ablak mérete
win.geometry("2000x2000")

#canvas létrehozás
canvas=Canvas(win, width=600, height=300)
canvas.configure(bg="lightgray")
#canvas akkora amekkora az ablak
canvas.pack(fill = BOTH, expand = 1)

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

fenyo2Masolat=transzformaciok.eltolas(fenyo2,100,100)
#canvas.create_line(fenyo2Masolat,width=5,fill="green")

mate=[[0,0,
   0,100,
   100,100,
   100,500,
   0,500,
   0,600,
   300,600,
   300,500,
   200,500,
   200,100,
   400,300,
   600,100,
   600,500,
   500,500,
   500,600,
   800,600,
   800,500,
   700,500,
   700,100,
   800,100,
   800,0,
   500,0,
   400,200,
   300,0,
   0,0],

   ]
a=[[0,400,
   180,400,
   250,250,
   350,250,
   420,400,
   600,400,
   400,0,
   200,0,
   0,400],

   [250,200,
    340,200,
    370,50,
    280,50,
    250,200],
    ]

t=[0,0,
   0,50,
   175,50,
   175,300,
   225,300,
   225,50,
   400,50,
   400,0,
   0,0]

e=[0,0,
   0,500,
   400,500,
   400,400,
   100,400,
   100,300,
   400,300,
   400,200,
   100,200,
   100,100,
   400,100,
   400,0,
   0,0
   ]

hatter="#ffffff"
betuszinek=["black", hatter, "blue"]

mate2=[[100.0, 100.0, 100.0, 140.0, 140.0, 140.0, 140.0, 300.0, 100.0, 300.0, 100.0, 340.0, 220.0, 340.0, 220.0, 300.0, 180.0, 300.0, 180.0, 140.0, 260.0, 220.0, 340.0, 140.0, 340.0, 300.0, 300.0, 300.0, 300.0, 340.0, 420.0, 340.0, 420.0, 300.0, 380.0, 300.0, 380.0, 140.0, 420.0, 140.0, 420.0, 100.0, 300.0, 100.0, 260.0, 180.0, 220.0, 100.0, 100.0, 100.0],
[450.0, 340.0, 558.0, 340.0, 600.0, 250.0, 660.0, 250.0, 702.0, 340.0, 810.0, 340.0, 690.0, 100.0, 570.0, 100.0, 450.0, 340.0], [600.0, 220.0, 654.0, 220.0, 672.0, 130.0, 618.0, 130.0, 600.0, 220.0],
[750.0, 100.0, 750.0, 140.0, 890.0, 140.0, 890.0, 340.0, 930.0, 340.0, 930.0, 140.0, 1070.0, 140.0, 1070.0, 100.0, 750.0, 100.0],
[1100.0, 100.0, 1100.0, 350.0, 1300.0, 350.0, 1300.0, 300.0, 1150.0, 300.0, 1150.0, 250.0, 1300.0, 250.0, 1300.0, 200.0, 1150.0, 200.0, 1150.0, 150.0, 1300.0, 150.0, 1300.0, 100.0, 1100.0, 100.0]]                                                                                                                                                                                                        
#for e in mate:
        #e=transzformaciok.nagyit(e,0.4)
        #e=transzformaciok.eltolas(e, 100, 100)
        #e=transzformaciok.forgat(e, 45)
        #mate2.append(e)

#mate2=transzformaciok.masol(mate)
#mate2=transzformaciok.nagyit(mate2,0.4)
#mate2=transzformaciok.eltolas(mate2,100,100)


#for e in mate2:
        #canvas.create_line(e,width=5,fill="black")

xMozgas=0.2
yMozgas=0.2
while True:
        canvas.delete("all")
        #mate2=transzformaciok.forgat(mate2,0.02)
        magassag=win.winfo_height()
        szelesseg=win.winfo_width()
        print(magassag)
        print(szelesseg)
        xLista=[]
        yLista=[]
        #koordináták kigyűjtése
        for elem in mate2:
                for i in range(len(elem)):
                        #X koord kigyűjtése
                        if i%2==0:
                                xLista.append(elem[i])
                        #Y koord kigyűjtése
                        else:
                                yLista.append(elem[i])
        #Legnagyobb koordináta megkeresése
        xLegnagyobb=max(xLista)
        yLegnagyobb=max(yLista)
        #Legkisebb koordináta megkeresése
        xLegkisebb=min(xLista)
        yLegkisebb=min(yLista)

        #Változtasson irányt, ha a széléhez ér
        if yLegnagyobb>magassag or yLegkisebb<0:
                yMozgas*=-1
        elif xLegnagyobb>szelesseg or xLegkisebb<0:
                xMozgas*=-1
        
        mate2=transzformaciok.eltolas(mate2,xMozgas,yMozgas)
        for i,e in enumerate(mate2):
                canvas.create_line(e,width=5)
        win.update_idletasks()
        win.update()
win.mainloop()