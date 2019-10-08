#!/usr/bin/python3

from Arbol import Arbol

def BPA(origen, destino, grafo):
    raiz = Arbol(None,-1,origen)#Se crea el nodo de origen
    frontera = [raiz]#Se almacena los nodos ha ser desmenuzados jeje
    visitados = []#Este arrglo avita hacer visitas inecesarias si ya fue visitado anteriormente un nodo
    while frontera:# si frontera aun tiene hijos
        nodo = frontera.pop(0)#Sacamos siempre el primero de la frontera  
        if nodo.elemento == destino:#Se regresa el arbol desmenuzado cuando se encontro el destino
            print("Arbol generado")
            print (raiz)
            return nodo.rutaNodoRaiz()#Se regresa la ruta segun el metodo del profe
        if not (nodo.elemento in visitados):
            for i in range(0,len(grafo[nodo.elemento])):#Va a recorrer la fila del nodo en especifico(conexiones entre los demas nodos)
                if grafo[nodo.elemento][i] == 1:#Va a checar las conexiones que tiene con otros nodos(vecinos)
                    if not (i in visitados):
                        raiz.agregar(nodo.elemento,nodo.nivel,i)#Se va agregando un hijo al nodo padre(nodo donde si huboc enexion)
                        frontera.append(Arbol(nodo,nodo.nivel,i))
            visitados.append(nodo.elemento)
    return None

archivo = open("Grafo.txt", "r")
grafo = []#En realidad va a ser una matriz, cada fila es un nodo, y la fila describe la conexion entre sus vecinos del grafo
for line in archivo.readlines():
    grafo.append( [ int (x) for x in line.split() ] )#Aqui se hace la matriz

origen, destino = input("Ingrese el origen y destino: ").split()
ruta = BPA(int(origen), int(destino), grafo)
if ruta == None:
    print ("No se encontro una ruta")
else:
    ruta.reverse()
    print ("Ruta encontrada")
    print (ruta)
