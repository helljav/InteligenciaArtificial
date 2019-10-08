#!/usr/bin/python3
from Arbol import Arbol
A1 = Arbol("1")
A1.agregar("1","1.1")
A1.agregar("1","1.2")
A1.agregar("1","1.3")
A1.agregar("1.1","1.1.1")
A1.agregar("1.2","1.2.1")
A1.agregar("1.2","1.2.2")
A1.agregar("1.1.1","1.1.1.1")
A1.agregar("1.1.1","1.1.1.2")
A1.agregar("1.1.1","1.1.1.3")
A1.agregar("1.2.1","1.2.1.1")
A1.agregar("1.2.2","1.2.2.1")
A1.agregar("1.2.2","1.2.2.2")
print ("Arbol inicial")
print (A1)
flag = True
while flag:
    print ("1) Agregar elemento")
    print ("2) Borrar elemento")
    print ("3) Imprimir sub-arbol")
    print ("4) Salir")
    opc = int(input("Eliga una opción: "))
    if opc == 1:
        padre, elemento = input("Ingrese el padre y elemento: ").split()
        A1.agregar(padre,elemento)
    elif opc == 2:
        elemento = input("Ingrese el elemento para borrar: ")
        A1.borrarSubA(elemento)
    elif opc == 3:
        buscar = input("Indique el sub arbol que desea imprimir: ")
        print (A1.buscarSubA(buscar))
    elif opc == 4:
        flag = False
    else:
        print ("Opcion no valida")