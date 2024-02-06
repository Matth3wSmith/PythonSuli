import time
import threading

done = False
def worker():
    counter = 0
    while not done:
        time.sleep(1)
        counter+=1
        print(counter)


t1=threading.Thread(target=worker)
t1.start()
input("Nyomd meg az Entert a befejezéshez")

done=True