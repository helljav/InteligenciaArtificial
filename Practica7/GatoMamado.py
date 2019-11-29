from Arbol import Arbol
import copy

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
    if tablero[int((num-1)/3)][(num-1)%3] is ' ':
        tablero[int((num-1)/3)][(num-1)%3] = player
    else:
        num = int(input("El espacio esta lleno, vuelve a escoger: "))
        moves(tablero, player, num)

def movesCPU(auxTablero, player, pos):
    if auxTablero[int((pos-1)/3)][(pos-1)%3] is ' ':
        auxTablero[int((pos-1)/3)][(pos-1)%3] = player




def estado_tablero(tablero):    
    # Check horizontals
    if (tablero[0][0] == tablero[0][1] and tablero[0][1] == tablero[0][2] and tablero[0][0] is not ' '):
        return tablero[0][0], "Victoria"
    if (tablero[1][0] == tablero[1][1] and tablero[1][1] == tablero[1][2] and tablero[1][0] is not ' '):
        return tablero[1][0], "Victoria"
    if (tablero[2][0] == tablero[2][1] and tablero[2][1] == tablero[2][2] and tablero[2][0] is not ' '):
        return tablero[2][0], "Victoria"
    
    # Check verticals
    if (tablero[0][0] == tablero[1][0] and tablero[1][0] == tablero[2][0] and tablero[0][0] is not ' '):
        return tablero[0][0], "Victoria"
    if (tablero[0][1] == tablero[1][1] and tablero[1][1] == tablero[2][1] and tablero[0][1] is not ' '):
        return tablero[0][1], "Victoria"
    if (tablero[0][2] == tablero[1][2] and tablero[1][2] == tablero[2][2] and tablero[0][2] is not ' '):
        return tablero[0][2], "Victoria"
    
    # Check diagonals
    if (tablero[0][0] == tablero[1][1] and tablero[1][1] == tablero[2][2] and tablero[0][0] is not ' '):
        return tablero[1][1], "Victoria"
    if (tablero[2][0] == tablero[1][1] and tablero[1][1] == tablero[0][2] and tablero[2][0] is not ' '):
        return tablero[1][1], "Victoria"
    
    # Check if draw
    draw_flag = 0
    for i in range(3):
        for j in range(3):
            if tablero[i][j] is ' ':
                draw_flag = 1
    if draw_flag is 0:
        return None, "Empate"
    
    return  None, "Sin resultado"


def generaArbol(tablero,player):
    Tablero = tablero[:]
    antPlayer = player
    raiz = Arbol(None,-1,Tablero)
    frontera = [raiz]
    visitados = []
    i = 1

    while frontera:
        nodo = frontera.pop(0)
        nodoE = nodo.elemento
        if not (nodo.elemento in visitados):
            if(antPlayer is "O"):
                actualPlayer = "X"
            elif(antPlayer is "X"):
                actualPlayer = "O"
            for i in range(1,10):
                auxTablero = copy.deepcopy(nodoE)
                movesCPU(auxTablero,actualPlayer,i)
                raiz.agregar(nodo.elemento,nodo.nivel,auxTablero)
                frontera.append(Arbol(nodo,nodo.nivel,auxTablero))
            visitados.append(nodo.elemento)
    print(raiz)
    return None

    
def cpuVSplayer(tablero):
    #os.system('clear')
    print("\tCPU juega con X     Player juega con O")

    Ganador = estado_tablero(tablero)[0]
    while Ganador == None:
        nPlayer = int(input(f"Turno Player: "))
        movesPlayer(tablero,'O',nPlayer)
        printTicTacToe(tablero)
        
        generaArbol(tablero,'O')
        #printTicTacToe(tablero)
        Ganador=estado_tablero(tablero)[0]

    if (Ganador=="O"):
        print("Gano Player")
    if(Ganador=="X"):
        print("Gano CPU")
    
    print("Fin del juego")

    #printTicTacToe(tablero)

def cpuVScpu(tablero):
    pass

def juego():
    opcion = 0 
    while opcion!=1 and opcion!=2:
        opcion = menu()
        print(opcion)

    tablero = [[' ',' ',' '],[' ',' ',' ' ],[' ',' ',' ']]

    printTicTacToe(tablero)
    
    if(opcion == 1):
        cpuVScpu(tablero)
    elif(opcion == 2):
        cpuVSplayer(tablero)


    

juego()