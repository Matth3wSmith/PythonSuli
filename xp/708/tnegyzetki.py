#Gyártó: Kovács Máté
from pynput.keyboard import *
import threading
tomb=[]
def nez():
    with Listener(on_press=press) as listener:
        listener.daemon(True)
        listener.join()

def press(key):
    if key == 0:
        tomb.append(szam)
    print("Lenyomott gomb {}".format(key))

t1=threading.Thread(target=nez, daemon=True)
t1.start()

szam=input("Add meg egy számot, ha nullát az utolsó számjegy akkor automatikusan mentésre kerül:")


print(tomb)
    