#!/usr/bin/python3

class Arbol:

    def __init__(self, padre, nivelpadre, elemento):
        self.hijos = []
        self.elemento = elemento
        self.padre = padre
        self.nivel = nivelpadre+1

    def __str__(self, level=0):
        cad = "\t|"*(level)+"-"+str(self.elemento) + "\n"
        for sub in self.hijos:
            cad += sub.__str__(level+1)
        return cad

    def buscarSubA(self, elemento, nivel):
        if self.elemento == elemento and self.nivel == nivel:
            return self
        else:
            for sub in self.hijos:
                buscado = sub.buscarSubA(elemento, nivel)
                if buscado != None:
                    return buscado
        return None

    def agregar(self, padre, nivelpadre, elemento):
        if self.elemento == padre and self.nivel == nivelpadre:
            self.hijos.append(Arbol(self, self.nivel, elemento))
        else:
            tmp = self.buscarSubA(padre, nivelpadre)
            if tmp != None:
                tmp.hijos.append(Arbol(tmp, tmp.nivel, elemento))
            else:
                print ("No se pudo agregar el elemento "+str(elemento)+" no se encontro al padre "+str(padre))

    def borrarSubA (self, elemento, nivel):
        for sub in self.hijos:
            if sub.elemento == elemento and self.nivel == nivel:
                self.hijos.remove(sub)
            else:
                sub.borrarSubA(elemento, nivel)

    def rutaNodoRaiz(self):
        nodo = self
        ruta = [nodo.elemento]
        while nodo.padre != None:
            nodo = nodo.padre
            ruta.append(nodo.elemento)
        return ruta
