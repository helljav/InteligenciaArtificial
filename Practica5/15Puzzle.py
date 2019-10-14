import copy
from Arbol import Arbol

def heuristica(actual,objetivo):
    h=0
    for i in range(0,len(actual)):
        for j in range(0,len(actual[i])):
            if actual[i][j]!=objetivo[i][j]:
                h +=1 
    return h

def determinaPos(origen):
    posF = 0
    posC = 0
    for fila in range(0,len(origen)):
        for columna in range(0,len(origen[fila])):
            if origen[fila][columna] == 0 :
                posF = fila
                posC = columna
    return posF,posC



def PUZZLE(origen, destino):
    raiz = Arbol(None,-1,(origen,0))
    frontera = [raiz]
    visitados = []
    
    while frontera:
            
        menorHeuristica = 9999
        menor = -1
        for i in range(len(frontera)):
            nodo = frontera[i]
            nodoElemento = nodo.elemento[0]
            nodoHeuristica = nodo.elemento[1]
            nodoHeuristica = heuristica(nodoElemento,destino)
            if nodoHeuristica < menorHeuristica:
                menorHeuristica = nodoHeuristica
                menor = i

        
        nodo = frontera.pop(menor)
        nodoE = nodo.elemento[0]
        nodoH = nodo.elemento[1]
        posR, posC = determinaPos(nodoE) #Determina donde esta el cero en este nodo 

        if nodoE == destino:
            print("Arbol generado")
            print (raiz)
            return nodo.rutaNodoRaiz()


        if not (nodo.elemento in visitados):
            try:
                if(nodoE[posR][posC-1]!=0):#Izquierda
                    
                    sinVisitar = copy.deepcopy(nodoE)             

                    varAux = sinVisitar[posR][posC-1]
                    sinVisitar[posR][posC-1] = 0
                    
                    sinVisitar[posR][posC] = varAux
                    nodoEHeuristica = heuristica(sinVisitar,destino)
                    
                        
                    elemento = (sinVisitar,nodoEHeuristica)
                    raiz.agregar(nodo.elemento,nodo.nivel,elemento)#Se va agregando un hijo al nodo padre(nodo donde si huboc enexion)
                    frontera.append(Arbol(nodo,nodo.nivel,elemento))                
            except:
                pass
            try:
                if(nodoE[posR+1][posC]!=0):#Abajo
                    

                    sinVisitar = copy.deepcopy(nodoE)
                    varAux = sinVisitar[posR+1][posC]
                    sinVisitar[posR+1][posC] = 0
                    sinVisitar[posR][posC] = varAux
                    nodoEHeuristica = heuristica(sinVisitar,destino)
                    
                    elemento = (sinVisitar,nodoEHeuristica)
                    raiz.agregar(nodo.elemento,nodo.nivel,elemento)#Se va agregando un hijo al nodo padre(nodo donde si huboc enexion)
                    frontera.append(Arbol(nodo,nodo.nivel,elemento))                
            except:
                pass
            try:
                if(nodoE[posR][posC+1]!=0):#derecha
                    
                    sinVisitar = copy.deepcopy(nodoE)
                    varAux = sinVisitar[posR][posC+1]
                    sinVisitar[posR][posC+1] = 0
                    sinVisitar[posR][posC] = varAux
                    nodoEHeuristica = heuristica(sinVisitar,destino)
                    

                    elemento = (sinVisitar,nodoEHeuristica)
                    raiz.agregar(nodo.elemento,nodo.nivel,elemento)#Se va agregando un hijo al nodo padre(nodo donde si huboc enexion)
                    frontera.append(Arbol(nodo,nodo.nivel,elemento))
            except:
                pass
            try:
                if(nodoE[posR-1][posC]!=0):#Arriba
                    
                    sinVisitar = copy.deepcopy(nodoE)
                    varAux = sinVisitar[posR-1][posC]
                    sinVisitar[posR-1][posC] = 0
                    sinVisitar[posR][posC] = varAux
                    nodoEHeuristica = heuristica(sinVisitar,destino)
                    

                    elemento = (sinVisitar,nodoEHeuristica)
                    raiz.agregar(nodo.elemento,nodo.nivel,elemento)#Se va agregando un hijo al nodo padre(nodo donde si huboc enexion)
                    frontera.append(Arbol(nodo,nodo.nivel,elemento))
                    
            except:
                pass
            


           
            visitados.append(nodo.elemento)
    return None


""" *************************************************************************************************"""

#puzzleI = [[1,2,3],[0,8,6],[7,5,4]]
puzzleOrigen = [[1,5,6],[7,3,4],[2,8,0]]
puzzleDestino = [[1,2,3],[4,5,6],[7,8,0]]



ruta = PUZZLE(puzzleOrigen, puzzleDestino)
if ruta == None:
    print ("No se encontro una ruta")
else:
    ruta.reverse()
    print ("Ruta encontrada")
    print (ruta)


