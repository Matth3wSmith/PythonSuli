import random

maxWidth=80
maxHeight=25

minFlakes=2
maxFlakes=10


rows=[]
for _ in range(maxHeight):
    actFlakes=random.randint(minFlakes,maxFlakes)
    actRow=" "*maxWidth

    flakes=random.sample(range(maxWidth),actFlakes)

    for i in flakes:
        actRow=actRow[:i]+"*"+actRow[i+1:]
    rows.append(actRow)


print("\n".join(rows))
