pruebita = [2,3,4,5,6]
pruebita2 = [pruebita]
horda = 5

elemento = (pruebita,horda,"caca")

nodo = elemento[0]
heuristica = elemento[1]

if(nodo[4]):
    varAux = nodo[4]
    nodo[4] = 2
    nodo[0] = varAux
else:
    print("No es valida esta opcion")

print(nodo)

if( pruebita in pruebita2):
    print("Si estas")