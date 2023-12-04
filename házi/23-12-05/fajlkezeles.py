import random

file = open("500szam.txt","w")

for i in range(500):
    file.write(str(random.randrange(1,300)))
    file.write(" ")
file.close()