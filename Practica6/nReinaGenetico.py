#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
class Cromosoma(object):
	# Constructor
    def __init__(self,tam):
        self.fitness = 0
        self.genes = []
        self.tam = tam
        
    # Crea un cromosoma
    def genera_cromosoma(self):
        numero_genes = 0
        while numero_genes < self.tam:
            gen = random.randint(0,self.tam-1)
            self.genes.append(gen)
            numero_genes = numero_genes + 1
            self.fitness = self.fidoneidad(self.genes)
        return self.genes, self.fitness

    def diagonales(self, gen, posicion):
        genesDiagonal1=[]
        genesDiagonal2=[]
        px=posicion+1
        py=gen+1
        for x in range(self.tam):
            if x==posicion:
                genesDiagonal1.append(gen)
                genesDiagonal2.append(gen)
                continue
            y1 = (x-posicion)*((py-gen)/(px-posicion))+gen
            y2 = (x-posicion)*((py-gen)/((posicion-1)-posicion))+gen
            if y1>=0 and y1<self.tam and y1!=gen:
                genesDiagonal1.append(y1)
            else:
                genesDiagonal1.append(-1)
            if y2>=0 and y2<self.tam and y2!=gen:
                genesDiagonal2.append(y2)
            else:
                genesDiagonal2.append(-1)
        return genesDiagonal1, genesDiagonal2

    def fidoneidad(self, genes):
        fitness=0
        i=0
        for k in range(len(genes)):
            diagonal1, diagonal2 = self.diagonales(genes[k], k)
            for i in range(len(genes)):
                if genes[k]==genes[i]:   # reina en horizontal
                    continue
                elif (len(diagonal1)>i and genes[i]==diagonal1[i]) or (len(diagonal2)>i and genes[i]==diagonal2[i]): # reina en diagonal
                    continue
                else:
                    fitness+=1
        fitness = (fitness*100)/77
        return fitness
# Fin Clase Cromosoma



# Metodo Principal
def AG():
    """Parámetros a modificar para obtener diferente rendimiento del algoritmo """
    #ngeneraciones = 700
    ncromosomas = 50
    #porcentaje_seleccionados = 50
    probabilidad_mutacion = 0.5
    probabilidad_cruzamiento = 0.5
    nReinas = int(input(f"Dame el numero de reinas----> : ")) 
    
    poblacion = []
    """Se crean los objetos Cromosomas"""
    for i in range(ncromosomas):
        poblacion.append(Cromosoma(nReinas))
        
        
    """Se generan los Cromosomas"""
    for i in range(ncromosomas):
        poblacion[i].genera_cromosoma()
        
    print ("\tPoblacion Inicial")
    print ("Cromosoma-Fitnes-Volumen")
    for i in range(ncromosomas):
        print (poblacion[i].genes, poblacion[i].fitness)
    print ("")
    
    
    # for generacion in range(numero_generaciones):
    #     seleccionados = selecciona_progenitores(poblacion, porcentaje_seleccionados, numero_cromosomas, VolMochila)
    #     hijos_cruzamiento = cruza_poblacion(seleccionados, probabilidad_cruzamiento, volumenes,beneficios, VolMochila)
    #     hijos_mutacion = muta_poblacion(seleccionados, probabilidad_mutacion, volumenes,beneficios, VolMochila)
    #     poblacion_temporal = []
    #     """
    #         Se añade al principio de esta lista el mejor elemento de la población
    #         actual para asegurar que sobreviva a la siguiente generación.
    #     """
    #     poblacion_temporal.insert(0,seleccionados[0])				
    #     poblacion_temporal = quicksort_GA(seleccionados+hijos_cruzamiento+hijos_mutacion)
    #     nueva_poblacion = reemplazo_poblacion(poblacion_temporal, numero_cromosomas)
    #     if(generacion==(numero_generaciones-1)):
    #         print ("\tGeneracion", generacion)
    #         print ("Cromosoma-Fitnes-Volumen")
    #         for i in nueva_poblacion:
    #             print(i.solucion,i.fitness,i.volumen)
        
    #     poblacion = nueva_poblacion
    print("FINISH HIM!")

# Fin Metodo Principal

AG()