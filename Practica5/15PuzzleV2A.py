"""
*****************************************************************************************************

                                UNIVERSIDAD AUTONOMA METROPOLITANA
                                
    ALUMNO: CARRILLO PACHECO FRANCISCO JAVIER
    MATRICULA: 2143008102
    PRACTICA 5, Simulacion del juego 15 Puzzle con algoritmo A*




******************************************************************************************************
"""
import copy
from Arbol import Arbol

def manhattan(actual,objetivo):
    ArrI= []
    ArrF = []
    h = 0

    for valor in range(1,len(actual)*len(actual)):
        for i in range(0,len(actual)):
            for j in range(0,len(actual[i])):
                if actual[i][j] == valor:
                    pos = (i,j)
                    ArrI.append(pos)

                if objetivo[i][j] == valor:
                    pos = (i,j)
                    ArrF.append(pos)
        
    for iterator in range(0,len(ArrF)):
        posIA = ArrI[iterator]
        posFO = ArrF[iterator]
        h += abs(posIA[0]-posFO[0])+abs(posIA[1]-posFO[1])
    
    return h
        



def PUZZLE(origen, destino):
    posR = 0
    posC = 0
    for fila in range(0,len(origen)):
        for columna in range(0,len(origen[fila])):
            if origen[fila][columna] == 0 :
                posR = fila
                posC = columna
    
    gn = 0
    heuri = manhattan(origen,destino)
    raiz = Arbol(None,-1,(origen,heuri,posR,posC,gn))
    frontera = [raiz]
    visitados = []
    
    while frontera:
            
        menorHeuristica = 9999
        menor = -1
        for i in range(len(frontera)):
            nodo = frontera[i]
            nodoHeuristica = nodo.elemento[1] 
            if nodoHeuristica < menorHeuristica:
                menorHeuristica = nodoHeuristica
                menor = i

        
        nodo = frontera.pop(menor)
        nodoE, nodoH, posR, posC,gn = nodo.elemento       
        
        if nodoE == destino:
            print("Arbol generado")
            print (raiz)
            return nodo.rutaNodoRaiz()


        if not (nodo.elemento in visitados):
            try:
                if(nodoE[posR][posC-1]!=0):#Izquierda
                    auxgn = gn
                    auxgn +=1                    
                    sinVisitar = copy.deepcopy(nodoE)            
                    varAux = sinVisitar[posR][posC-1]
                    sinVisitar[posR][posC-1] = 0                    
                    sinVisitar[posR][posC] = varAux
                    nodoEHeuristica = manhattan(sinVisitar,destino) + auxgn                        
                    elemento = (sinVisitar,nodoEHeuristica,posR,posC-1,auxgn)
                    raiz.agregar(nodo.elemento,nodo.nivel,elemento)#Se va agregando un hijo al nodo padre(nodo donde si huboc enexion)
                    frontera.append(Arbol(nodo,nodo.nivel,elemento))                
            except:
                pass
            try:
                if(nodoE[posR+1][posC]!=0):#Abajo
                    auxgn = gn
                    auxgn +=1                    
                    sinVisitar = copy.deepcopy(nodoE)
                    varAux = sinVisitar[posR+1][posC]
                    sinVisitar[posR+1][posC] = 0
                    sinVisitar[posR][posC] = varAux
                    nodoEHeuristica = manhattan(sinVisitar,destino) + auxgn
                    elemento = (sinVisitar,nodoEHeuristica,posR+1,posC,auxgn)
                    raiz.agregar(nodo.elemento,nodo.nivel,elemento)#Se va agregando un hijo al nodo padre(nodo donde si huboc enexion)
                    frontera.append(Arbol(nodo,nodo.nivel,elemento))                
            except:
                pass
            try:
                if(nodoE[posR][posC+1]!=0):#derecha
                    auxgn = gn
                    auxgn +=1                   
                    sinVisitar = copy.deepcopy(nodoE)
                    varAux = sinVisitar[posR][posC+1]
                    sinVisitar[posR][posC+1] = 0
                    sinVisitar[posR][posC] = varAux
                    nodoEHeuristica = manhattan(sinVisitar,destino) + auxgn
                    elemento = (sinVisitar,nodoEHeuristica,posR,posC+1,auxgn)
                    raiz.agregar(nodo.elemento,nodo.nivel,elemento)#Se va agregando un hijo al nodo padre(nodo donde si huboc enexion)
                    frontera.append(Arbol(nodo,nodo.nivel,elemento))
            except:
                pass
            try:
                if(nodoE[posR-1][posC]!=0):#Arriba
                    auxgn = gn
                    auxgn +=1                    
                    sinVisitar = copy.deepcopy(nodoE)
                    varAux = sinVisitar[posR-1][posC]
                    sinVisitar[posR-1][posC] = 0
                    sinVisitar[posR][posC] = varAux
                    nodoEHeuristica = manhattan(sinVisitar,destino) + auxgn
                    elemento = (sinVisitar,nodoEHeuristica,posR-1,posC,auxgn)
                    raiz.agregar(nodo.elemento,nodo.nivel,elemento)#Se va agregando un hijo al nodo padre(nodo donde si huboc enexion)
                    frontera.append(Arbol(nodo,nodo.nivel,elemento))
                    
            except:
                pass
            


           
            visitados.append(nodo.elemento)
    return None


""" *************************************************************************************************"""

#puzzleOrigen = [[1,2,3],[0,8,6],[7,5,4]]
#puzzleDestino = [[1,2,3],[4,5,6],[7,8,0]]
puzzleOrigen = [[1,2,3,11],[7,8,10,13],[6,9,15,4],[12,14,0,5]]
puzzleDestino = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,0]]
# puzzleOrigen = [[2,1],[0,3]]
# puzzleDestino = [[1,2],[3,0]]


ruta = PUZZLE(puzzleOrigen, puzzleDestino)
if ruta == None:
    print ("No se encontro una ruta")
else:
    ruta.reverse()
    print ("Ruta encontrada")
    print (ruta)


