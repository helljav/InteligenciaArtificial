from Arbol import Arbol
import os
import copy
import time
"""
*****************************************************************************************************

                                UNIVERSIDAD AUTONOMA METROPOLITANA
                                
    ALUMNO: CARRILLO PACHECO FRANCISCO JAVIER
    MATRICULA: 2143008102
    PRACTICA 7, Juego del gato con el algoritmo miniMax




******************************************************************************************************
"""


def menu():
    print("************************************************************************************************")
    print("\t\t BIENVENIDO AL JUEGO DEL GATO CON EL ALGORITMO MIN-MAX\n")
    print("\t\t\t ¿QUE MODALIDAD QUIERES JUGAR?\n")
    opcion = int(input(f"\t\tCPU vs CPU ----------> 1\tCPU vs PLAYER ---------->2\n"))
    return opcion


def printTicTacToe(tablero):
    print(' ',str(tablero[0][0]), ' | ' , str(tablero[0][1]) , ' | ' , str(tablero[0][2]))
    print('----------------')
    print(' ',str(tablero[1][0]) , ' | ' , str(tablero[1][1]) , ' | ' , str(tablero[1][2]))
    print('----------------')
    print(' ',str(tablero[2][0]) , ' | ' , str(tablero[2][1]), ' | ' , str(tablero[2][2]))

def movesPlayer(tablero, player, num):
    if tablero[int((num-1)/3)][(num-1)%3] is '':
        tablero[int((num-1)/3)][(num-1)%3] = player
    else:
        num = int(input("El espacio esta lleno bro, vuelve a escoger: "))
        movesPlayer(tablero, player, num)

def movesArbol(tablero, player, num):
    if tablero[int((num-1)/3)][(num-1)%3] is '':
        tablero[int((num-1)/3)][(num-1)%3] = player
        return True
    return False
    




"""Aqui empoezan los algoritmos minMax"""
    
def cpuVSplayer(tablero):
    """El primer turno es del jugador, va a poner su primera o"""
    os.system('clear')
    print("\tCPU juega con->>>>> X     Player juega con->>>>>> O")
    nPlayer = int(input(f"Turno Player, pon O en : "))
    movesPlayer(tablero,'O',nPlayer)
    movesPlayer(tablero,'X',1)
    movesPlayer(tablero,'O',3)
    generaArbol(tablero,'O')    
    printTicTacToe(tablero)

def estado_tablero(tablero):    
    # Check horizontals
    if (tablero[0][0] == tablero[0][1] and tablero[0][1] == tablero[0][2] and tablero[0][0] is not ' '):
        return tablero[0][0], True
    if (tablero[1][0] == tablero[1][1] and tablero[1][1] == tablero[1][2] and tablero[1][0] is not ' '):
        return tablero[1][0], True
    if (tablero[2][0] == tablero[2][1] and tablero[2][1] == tablero[2][2] and tablero[2][0] is not ' '):
        return tablero[2][0], True
    
    # Check verticals
    if (tablero[0][0] == tablero[1][0] and tablero[1][0] == tablero[2][0] and tablero[0][0] is not ' '):
        return tablero[0][0], True
    if (tablero[0][1] == tablero[1][1] and tablero[1][1] == tablero[2][1] and tablero[0][1] is not ' '):
        return tablero[0][1], True
    if (tablero[0][2] == tablero[1][2] and tablero[1][2] == tablero[2][2] and tablero[0][2] is not ' '):
        return tablero[0][2], True
    
    # Check diagonals
    if (tablero[0][0] == tablero[1][1] and tablero[1][1] == tablero[2][2] and tablero[0][0] is not ' '):
        return tablero[1][1], True
    if (tablero[2][0] == tablero[1][1] and tablero[1][1] == tablero[0][2] and tablero[2][0] is not ' '):
        return tablero[1][1], True
    
    # Check if draw
    draw_flag = 0
    for i in range(3):
        for j in range(3):
            if tablero[i][j] is ' ':
                draw_flag = 1
    if draw_flag is 0:
        return None, True
    
    return  None, False

def generaArbol(tablero,player):
    Tablero = tablero[:]
    antPlayer = player
    actPlayer = None
    raiz = Arbol(None,-1,(Tablero, antPlayer))
    frontera = [raiz]
    visitados = []
    while frontera:        
        nodo = frontera.pop(0)
        nodoE,antPlayer = nodo.elemento
        """CAMBIAR LA MANETrueNER LAS HOJAS EN EL ARBOL"""
        if not (nodo.elemento in visitados):
            if(antPlayer is 'O'):
                actPlayer = 'X'
            else:
                actPlayer = 'O'
            for i in range(1,10):
                auxTablero = copy.deepcopy(nodoE) 
                flag = movesArbol(auxTablero,actPlayer,i)
                if(flag):
                    # bandera=estado_tablero(auxTablero)
                    # if(bandera):                        
                    elemento = (auxTablero,actPlayer)
                    raiz.agregar(nodo.elemento,nodo.nivel,elemento)#Se va agregando un hijo al nodo padre(nodo donde si huboc enexion)
                    frontera.append(Arbol(nodo,nodo.nivel,elemento))
                    #print(elemento)
                           
            visitados.append(nodo.elemento)
    print(raiz)




def cpuVScpu(tablero):
    pass




def juego():
    opcion = 0 
    while opcion!=1 and opcion!=2:
        opcion = menu()
        print(opcion)

    tablero = [ ['','',''],
                ['','',''],
                ['','',''] ]
    
    if(opcion == 1):
        cpuVScpu(tablero)
    elif(opcion == 2):
        cpuVSplayer(tablero)


    




    

juego()