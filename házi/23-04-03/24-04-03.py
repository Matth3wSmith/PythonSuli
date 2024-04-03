#Házi 2024.04.03
szorzotabla=[]
class SzorzoTabla:
    def __init__(self, szam):
        self.tablaSor=[i*szam for i in range(1,11)]
        
for i in range(1,11):
    szorzotabla.append(SzorzoTabla(i).tablaSor)

print(szorzotabla)