import time
import os

def syracuse(nombre):
    if(nombre % 2 == 0):
        return nombre / 2
    else:
        return nombre * 3 + 1

tempsDebut = time.time()
def endProgram():
    tempsFin = time.time()
    resultTime = tempsFin - tempsDebut
    print("Temps d'execution : "+str(resultTime)+" secondes")
    os.system("pause")

base = 2
nombreMax=base

while(True):
    nombre = base                  
    while(nombre != 1):
        nombre = syracuse(nombre)
        if(nombre>nombreMax):
            nombreMax = nombre + 0
            print(nombre," pour une valeur de base : ",base)
    base = base + 1
    nombre = 0
    if (base%1000==0):                  # Après 10 000 itération, le programme s'arrête
        endProgram()
