#Készítő: Kovács Máté
import math
print("Hatszög alakú gyep területének kiszámítása")

telek1 =input("Add meg az első hexagon alakú telek hosszát!")
telek2 =input("Add meg az második hexagon alakú telek hosszát!")

terulet= 3/2*math.sqrt(3)*(int(telek1)**2+(int(telek2)**2)/2)
print("Ennyi négyzetméter gyeptégla szükséges a két telek gyepesítéséhez: "+str(terulet))