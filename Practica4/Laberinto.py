#!/usr/bin/python3

from Arbol import Arbol

def Laberinto(laberinto):
    posR = 0
    posC = 0
    #Se tiene que buscar las coordenadas de I y van a ir como tupla
    for fila in range(0,len(laberinto)):
        for columna in range(0,len(laberinto[fila])):
            if laberinto[fila][columna]=="I":
                posR = fila
                posC = columna
    origen=(posR,posC)
   
    raiz = Arbol(None,-1,origen)
    frontera = [raiz]
    visitados = []
    

    while frontera:# si frontera aun tiene hijos
        nodo = frontera.pop(0)#Sacamos siempre el primero de la frontera  
        posR,posC=nodo.elemento
        if laberinto[posR][posC] == 'S':#Se regresa el arbol desmenuzado cuando se encontro el destino
            print("Arbol generado")
            print (raiz)
            return nodo.rutaNodoRaiz()#Se regresa la ruta segun el metodo del profe
        if not (nodo.elemento in visitados):
            try:
                if(laberinto[posR][posC-1]!='X'):#Izquierda
                    elemento = (posR,posC-1)
                    raiz.agregar(nodo.elemento,nodo.nivel,elemento)#Se va agregando un hijo al nodo padre(nodo donde si huboc enexion)
                    frontera.append(Arbol(nodo,nodo.nivel,elemento))                
            except:
                pass
            try:
                if(laberinto[posR+1][posC]!='X'):#Abajo
                    elemento = (posR+1,posC)
                    raiz.agregar(nodo.elemento,nodo.nivel,elemento)#Se va agregando un hijo al nodo padre(nodo donde si huboc enexion)
                    frontera.append(Arbol(nodo,nodo.nivel,elemento))                
            except:
                pass
            try:
                if(laberinto[posR][posC+1]!='X'):#derecha
                    elemento = (posR,posC+1)
                    raiz.agregar(nodo.elemento,nodo.nivel,elemento)#Se va agregando un hijo al nodo padre(nodo donde si huboc enexion)
                    frontera.append(Arbol(nodo,nodo.nivel,elemento))
            except:
                pass
            try:
                if(laberinto[posR-1][posC]!='X'):#Arriba
                    elemento = (posR-1,posC)
                    raiz.agregar(nodo.elemento,nodo.nivel,elemento)#Se va agregando un hijo al nodo padre(nodo donde si huboc enexion)
                    frontera.append(Arbol(nodo,nodo.nivel,elemento)) 
            except:
                pass
                       
            visitados.append(nodo.elemento)
    return None

archivo = open("Lab.txt", "r")
laberinto = []#En realidad va a ser una matriz, cada fila es un nodo, y la fila describe la conexion entre sus vecinos del grafo
for line in archivo.readlines():
    laberinto.append( line.split() )#Aqui se hace la matriz


ruta = Laberinto(laberinto)
if ruta == None:
    print ("No se encontro una ruta")
else:
    ruta.reverse()
    print ("Ruta encontrada")
    print (ruta)
