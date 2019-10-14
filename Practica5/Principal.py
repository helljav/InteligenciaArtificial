#!/usr/bin/python3

from Arbol import Arbol

def BCU(origen, destino, grafoP):
    raiz = Arbol(None,-1,(origen,0))
    frontera = [raiz]
    visitados = []
    while frontera:
        menorCosto = 9999
        menor = -1
        for i in range(len(frontera)):
            nodo = frontera[i]
            nodoElemento, nodoCosto = nodo.elemento
            if nodoCosto < menorCosto:
                menorCosto = nodoCosto
                menor = i
        nodo = frontera.pop(menor)
        nodoE, nodoC = nodo.elemento 
        if nodoE == destino:
            print("Arbol generado")
            print (raiz)
            return nodo.rutaNodoRaiz()
        if not (nodo.elemento in visitados):
            for i in range(0,len(grafoP[nodoE])):
                if grafoP[nodoE][i] < 9999:
                    if not ((i,grafoP[nodoE][i]) in visitados):
                        raiz.agregar(nodo.elemento,nodo.nivel,(i,nodoC+grafoP[nodoE][i]))
                        frontera.append(Arbol(nodo,nodo.nivel,(i,nodoC+grafoP[nodoE][i])))
            visitados.append(nodo.elemento)
    return None

def BPP(origen, destino, grafo):
    raiz = Arbol(None,-1,origen)
    frontera = [raiz]
    visitados = []
    while frontera:
        nodo = frontera.pop()
        if nodo.elemento == destino:
            print("Arbol generado")
            print (raiz)
            return nodo.rutaNodoRaiz()
        if not (nodo.elemento in visitados):
            for i in range(0,len(grafo[nodo.elemento])):
                if grafo[nodo.elemento][i] == 1:
                    if not (i in visitados):
                        raiz.agregar(nodo.elemento,nodo.nivel,i)
                        frontera.append(Arbol(nodo,nodo.nivel,i))
            visitados.append(nodo.elemento)
    return None

def BPA(origen, destino, grafo):
    raiz = Arbol(None,-1,origen)
    frontera = [raiz]
    visitados = []
    while frontera:
        nodo = frontera.pop(0)
        if nodo.elemento == destino:
            print("Arbol generado")
            print (raiz)
            return nodo.rutaNodoRaiz()
        if not (nodo.elemento in visitados):
            for i in range(0,len(grafo[nodo.elemento])):
                if grafo[nodo.elemento][i] == 1:
                    if not (i in visitados):
                        raiz.agregar(nodo.elemento,nodo.nivel,i)
                        frontera.append(Arbol(nodo,nodo.nivel,i))
            visitados.append(nodo.elemento)
    return None

archivo = open("Grafo.txt", "r")
grafo = []
for line in archivo.readlines():
    grafo.append( [ int (x) for x in line.split() ] )

origen, destino = input("Ingrese el origen y destino: ").split()
ruta = BPA(int(origen), int(destino), grafo)

rutaPP = BPP(int(origen), int(destino), grafo)

archivoP = open("GrafoP.txt", "r")
grafoP = []
for line in archivoP.readlines():
    grafoP.append( [ int (x) for x in line.split() ] )
rutaP = BCU(int(origen), int(destino), grafoP)

if ruta == None:
    print ("No se encontro una ruta")
else:
    ruta.reverse()
    print ("Ruta encontrada")
    print (ruta)

if rutaPP == None:
    print ("No se encontro una ruta")
else:
    rutaPP.reverse()
    print ("Ruta encontrada")
    print (rutaPP)

if rutaP == None:
    print ("No se encontro una ruta")
else:
    rutaP.reverse()
    print ("Ruta encontrada")
    print (rutaP)
