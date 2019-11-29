#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

# Lee un archivo el cual contiene los datos del problema tales como sus beneficios y volumenes
def leerMatriz_costoBeneficio(NombreArchivo):
	matrizMochila = []
	contador = 0
	with open(NombreArchivo, 'r') as f:
		for line in f:
			line = line.strip()
			if len(line) > 0 :
				contador+=1
				matrizMochila.append( [int(n) for n in line.split()] )

		beneficios = []
		volumenes = []
		for i  in range(contador):
			beneficios.append(matrizMochila[i][0]);
			volumenes.append(matrizMochila[i][1]);
	return  beneficios, volumenes
# Fin metodo leerMatriz_costoBeneficio

"""
	La clase Cromosoma va a tener instancias de cada caso 
	clase en la cual se generan las soluciones,asi como tambien se calculan 
	sus beneficios y volumenes
"""
class Cromosoma(object):

	# Constructor
	def __init__(self):
		self.fitness = 0
		self.solucion = []
		self.volumen = 0;

	# Crea un cromosoma
	def genera_solucion(self, volumenes,beneficios):
			solucion = []
			n = len(beneficios)
			numero_genes = 0
			while numero_genes < n:
				gen = (random.randint(0,10))/10.0;
				self.solucion.append(gen)
				numero_genes = numero_genes + 1
			return self.solucion
			
	# Calcula el fitness de un cromosoma
	def calcula_fitness(self,volumenes,beneficios):
		n = len(volumenes)
		j = 0
		beneficio = 0
		while(j < n):
			beneficio = beneficio + beneficios[j]*self.solucion[j]
			j = j+1
		self.fitness = beneficio

	# Calcula el volumen del cromosoma
	def calcula_volumen(self,volumenes):
		vol = 0;
		n = len(volumenes)
		for i in range (n):
			vol = vol + volumenes[i]*self.solucion[i];	
		self.volumen = vol
# Fin Clase Cromosoma

################## Metodos de Cromosomas #################

def selecciona_progenitores(poblacion, porcentaje_seleccionados,num_cromosomas, VolMochila):
	poblacion_ordenada = quicksort_GA(poblacion)
	num_seleccionados = (porcentaje_seleccionados*num_cromosomas)//100
	preseleccionados = []
	# Seleccionamos el porcentaje definido de los mejores cromosomas
	for i in range(num_seleccionados):
		preseleccionados.append(poblacion_ordenada[i])
	# Creamos un excedente para realizar suficientes copias de los seleccionados
	for i in range(5):
		preseleccionados = preseleccionados+preseleccionados
	seleccionados = []
	# Acotamos los preseleccionados con excedente al número original de la poblacion
	for i in range(num_cromosomas):
		seleccionados.append(preseleccionados[i])
	return seleccionados
# Fin de selecciona_progenitores

"""
	Este método recibe los cromosomas seleccionados, crea parejas
	y los cruza tomando en cuenta la probabilidad de cruzamiento.
	Finalmente, regresa los hijos generados.
"""
def cruza_poblacion(seleccionados, probabilidad_cruzamiento, volumenes,beneficios, VolMochila):
	num_cromosomas = len(seleccionados)
	hijos_de_cruzamiento = []

	for i in range(num_cromosomas):
			a = 0
			b = 0
			# Dentro del arreglo de cromosomas seleccionados elegimos dos índices diferentes
			while(a == b):
				a = random.randint(0,num_cromosomas-1)
				b = random.randint(0,num_cromosomas-1)

			# Generamos un aleatorio entre 1 y 0 para determinar si se cruzan los cromosomas seleccionados
			r = random.random()
			
			# Si r es menor que Pc (prob. de cruzamiento)  entonces se cruzan
			if r < probabilidad_cruzamiento:
				hijos = cruzamiento(seleccionados[a], seleccionados[b], volumenes,beneficios)
				#Verifica si el hijo creado excede el volumen de la mochila,de ser asi genera otro hijo
				while (hijos[0].volumen > VolMochila) or (hijos[1].volumen > VolMochila):
					while(a == b):
						a = random.randint(0,num_cromosomas-1)
						b = random.randint(0,num_cromosomas-1)
				
					hijos = []
					hijos = cruzamiento(seleccionados[a], seleccionados[b], volumenes,beneficios)
				hijos_de_cruzamiento.append(hijos[0])
				hijos_de_cruzamiento.append(hijos[1])
	return hijos_de_cruzamiento
#  Fin de cruza_poblacion
"""
	Metodo cruzamiento en el cual se generan hijos en base a las particiones de dos de sus padres
	colocando la particion de uno en otro y visceversa
"""
def cruzamiento(padre1, padre2, volumenes,beneficios):
	n = len(padre1.solucion)
	solucion_hijo = [-1]*n

	r = random.randint(0,n-1)
	aux1 = padre1.solucion[:r] #izquierda
	aux2 = padre2.solucion[r:] #derecha
	aux3= padre1.solucion[r:]
	aux4 = padre2.solucion[:r]
	hijo1 = aux1 + aux2
	hijo2 = aux4 + aux3

	Obj_hijo1 = Cromosoma()
	Obj_hijo1.solucion = hijo1

	Obj_hijo1.calcula_fitness(volumenes,beneficios)
	Obj_hijo1.calcula_volumen(volumenes)		

	Obj_hijo2 = Cromosoma()
	Obj_hijo2.solucion = hijo2

	Obj_hijo2.calcula_fitness(volumenes,beneficios)
	Obj_hijo2.calcula_volumen(volumenes)
	return Obj_hijo1, Obj_hijo2
# Fin de cruzamiento
		
def muta_poblacion(seleccionados, probabilidad_mutacion, volumenes,beneficios, VolMochila):

	num_cromosomas = len(seleccionados)
	hijos_de_mutacion = []
	
	"""
		Para cada uno de los cromosomas seleccionados se 
		genera un aleatorio entre cero y uno. Si éste es menor
		que la prob. de mutación entonces se muta el
		cromosoma correspondiente.
	"""
	
	for i in seleccionados:
		r = random.random()
		if r < probabilidad_mutacion:
			hijo = mutacion_inversion(i, volumenes,beneficios)
			while(hijo.volumen > VolMochila):
				#print "Me estaba pasando xD pero corregi"
				hijo =[]
				hijo = mutacion_inversion(i, volumenes,beneficios)
			hijos_de_mutacion.append(hijo)
	return hijos_de_mutacion
# Fin de muta_poblacion
	
"""
	Mutación: consiste en intercambiar únicamente
	dos elementos de un cromosoma
"""
def mutacion_inversion(cromosoma, volumenes,beneficios):

	pos1 = 0
	pos2 = 0
	n = len(cromosoma.solucion)

	# Seleccionamos los puntos de corte.

	while(pos1 >= pos2):
		pos1 = random.randint(0,n-1)
		pos2 =  random.randint(0,n-1)

	aux = cromosoma.solucion[pos1]
	cromosoma.solucion[pos1] = cromosoma.solucion[pos2]
	cromosoma.solucion[pos2] = aux

	hijo = Cromosoma()
	hijo.solucion = cromosoma.solucion
	hijo.calcula_fitness(volumenes,beneficios)
	hijo.calcula_volumen(volumenes)
	
	return hijo
# Fin de mutacion_inversion


"""
	Este método selecciona a los cromosomas aptos para pasar a la siguiente
	generación manteniendo el número de poblacion intacto
"""
def reemplazo_poblacion(poblacion, numero_cromosomas):
	nueva_poblacion = []
	for i in range(numero_cromosomas):
		nueva_poblacion.append(poblacion[i])			
	return nueva_poblacion
# Fin de reemplazo_poblacion

# Metodo de ordenamiento
def quicksort_GA(Poblacion):
	n = len(Poblacion)
	if n <= 1:
		return Poblacion
	
	centro = n//2	
	pivote = Poblacion[centro]
	Poblacion.pop(centro)
	menores = []
	mayores = []

	for i in range(0,n-1):
		if Poblacion[i].fitness > pivote.fitness:
			 mayores.append(Poblacion[i])
		else:
			menores.append(Poblacion[i])

	menores_ordenados = quicksort_GA(menores)
	mayores_ordenados = quicksort_GA(mayores)
	ordenados = mayores_ordenados+[pivote]+menores_ordenados
	return ordenados
# Fin QuickSort

# Metodo Principal
def AG():
	#Parametros iniciales y a tener encuenta para cada solucion
	NombreArchivo = "clase.txt"
	matriz_mochila = leerMatriz_costoBeneficio(NombreArchivo)
	beneficios = matriz_mochila[0];
	volumenes= matriz_mochila[1];
	VolMochila = 341045
	
	print ("\tLos beneficios a tener en cuenta son: ", beneficios)
	print ("\tLos volumenes a tener en cuenta son: ", volumenes)
	print ("\tEl volumen de la mochila es: ", VolMochila, "\n");
	
	# Parámetros a modificar para obtener diferente rendimiento del algoritmo
	numero_generaciones = 700
	numero_cromosomas = 20
	porcentaje_seleccionados = 50
	probabilidad_mutacion = 0.1
	probabilidad_cruzamiento = 0.5

	poblacion = []
	# Se crean los objetos Cromosomas
	for i in range(numero_cromosomas):
			poblacion.append(Cromosoma())

	# Se generan los Cromosomas
	for i in range(numero_cromosomas):
			poblacion[i].genera_solucion(volumenes,beneficios)
			poblacion[i].calcula_volumen(volumenes)
			while(poblacion[i].volumen > VolMochila):
				poblacion[i].solucion = []
				poblacion[i].genera_solucion(volumenes,beneficios)
				poblacion[i].calcula_volumen(volumenes)
			poblacion[i].calcula_fitness(volumenes,beneficios)

	print ("\tPoblacion Inicial")
	print ("Cromosoma-Fitnes-Volumen")
	for i in range(numero_cromosomas):
			print (poblacion[i].solucion, poblacion[i].fitness, poblacion[i].volumen);
	print ("");

	for generacion in range(numero_generaciones):

			seleccionados = selecciona_progenitores(poblacion, porcentaje_seleccionados, numero_cromosomas, VolMochila)
			hijos_cruzamiento = cruza_poblacion(seleccionados, probabilidad_cruzamiento, volumenes,beneficios, VolMochila)
			hijos_mutacion = muta_poblacion(seleccionados, probabilidad_mutacion, volumenes,beneficios, VolMochila)
			poblacion_temporal = []
			"""
				Se añade al principio de esta lista el mejor elemento de la población
				actual para asegurar que sobreviva a la siguiente generación.
			"""
			poblacion_temporal.insert(0,seleccionados[0])				
			poblacion_temporal = quicksort_GA(seleccionados+hijos_cruzamiento+hijos_mutacion)
			nueva_poblacion = reemplazo_poblacion(poblacion_temporal, numero_cromosomas)
			if(generacion==(numero_generaciones-1)):
				print ("\tGeneracion", generacion)
				print ("Cromosoma-Fitnes-Volumen")
				for i in nueva_poblacion:
					print(i.solucion,i.fitness,i.volumen)
			
			poblacion = nueva_poblacion
	print("FINISH HIM!")

# Fin Metodo Principal

AG()