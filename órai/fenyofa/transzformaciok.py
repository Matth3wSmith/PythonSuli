import math

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

if __name__ == '__main__':
    print("Rendesen elindítva")
else:
    print("Modulként betöltve")