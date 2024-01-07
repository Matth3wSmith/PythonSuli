#GRAFIKUS FELHASZNÁLÓI FELÜLET
import tkinter

#adatok a szemely listába rakása
def adatmentes():
    szemely.append(nevEntry.get())
    szemely.append(telepulesEntry.get())
    szemely.append(lakcimEntry.get())
    szemely.append(telszamEntry.get())
    szemely.append(fizetesEntry.get())

#beviteli mezők törlés
def adattorles(event):
    nevEntry.delete(0,tkinter.END)
    telepulesEntry.delete(0,tkinter.END)
    lakcimEntry.delete(0,tkinter.END)
    telszamEntry.delete(0,tkinter.END)
    fizetesEntry.delete(0,tkinter.END)

#kilépés a felületből
def exit(event):
    felulet.destroy()

#function a txt-be íráshoz
def iras(event):
    f=open("szemely.txt","a",encoding="utf-8")
    adatmentes()
    event=szemely
    f.write("Név: "+str(event[0])+"\n")
    f.write("Település: "+str(event[1])+"\n")
    f.write("Lakcím: "+str(event[2])+"\n")
    f.write("Telefonszám: "+str(event[3])+"\n")
    f.write("Fizetés: "+str(event[4])+"\n")
    f.close()

szemely=[]

felulet = tkinter.Tk()

#frame a név bekéréshez
doboz=tkinter.Frame(borderwidth="10",relief="ridge")

#név felirat
nev=tkinter.Label(text="Név:",master=doboz)
nev.pack()

#név bekérés
nevEntry = tkinter.Entry(master=doboz)
nevEntry.pack(pady="5")

#település felirat
telepules=tkinter.Label(text="Település:",master=doboz)
telepules.pack()

#település bekérés
telepulesEntry = tkinter.Entry(master=doboz)
telepulesEntry.pack(pady="5")

#lakcím felirat
lakcim=tkinter.Label(text="Lakcím:",master=doboz)
lakcim.pack()

#lakcím bekérés
lakcimEntry = tkinter.Entry(master=doboz)
lakcimEntry.pack(pady="5")

#telefonszám felirat
telszam=tkinter.Label(text="Telefonszám:",master=doboz)
telszam.pack()

#telefonszám bekérés
telszamEntry = tkinter.Entry(master=doboz)
telszamEntry.pack(pady="5")

#fizetés felirat
fizetes=tkinter.Label(text="Fizetés:",master=doboz)
fizetes.pack()

#fizetés bekérés
fizetesEntry = tkinter.Entry(master=doboz)
fizetesEntry.pack(pady="5")


#hozzádás gomb
hozzadas=tkinter.Button(text="Hozzáadás", master=doboz,)
hozzadas.pack(side="left")

#törlés gomb
torles=tkinter.Button(text="Törlés", master=doboz,)
torles.pack(side="left",padx="15")

#kilépés gomb
kilepes=tkinter.Button(text="Kilépés", master=doboz,)
kilepes.pack(pady="15")


doboz.pack()


#iras function meghívása ha rányomunk a gombra
hozzadas.bind("<Button-1>", iras)

#beviteli mezők törlése
torles.bind("<Button-1>", adattorles)

#kilépés a felületből
kilepes.bind("<Button-1>", exit)

felulet.mainloop()

#MEGJEGYZÉS: Arra nem sikerült rájönnöm, hogy hogyan oldjam meg az karakterkódólási problémát, mert amikor elmenti az adatokat a szemely.txt-be a program, az ékezeteket nem mutatja