#!/usr/bin/python3
class Arbol:
	def __init__(self, elemento):        
		self.hijos = []        
		self.elemento = elemento
    
	#Permite impriir el arbol tan solo haciendo: "Print(ObjetoArbol)"
	def __str__(self, level=0):
		cad = "\t|"*(level)+"-"+self.elemento + "\n"
		for sub in self.hijos:
			cad += sub.__str__(level+1)
		return cad

    
	def buscarSubA(self, elemento):
		if(self.elemento == elemento):
			return self
		for subA in self.hijos:
			Areturn = subA.buscarSubA(elemento)
			if Areturn != None:
				return Areturn
			
						

	def agregar(self, padre, elemento):
		father = self.buscarSubA(padre)
		father.hijos.append(Arbol(elemento))
		self = father
		


	def borrarSubA (self, elemento):
		for subA in self.hijos:
			if(subA.elemento == elemento):
				self.hijos.remove(subA)
				print("Se ha removido el elemento ",subA.elemento," con exito ")
				return 0
			else:
				subA.borrarSubA(elemento)



##
# Metodo Main
##
def main():

# Creacion de un objeto de la clase ventana
   A1 = Arbol("1")
   A1.agregar("1","2")
   A1.agregar("1","3")
   A1.agregar("2","4")
   A1.agregar("2","7")
   A1.agregar("2","8")

   print (A1.buscarSubA("3"))
   A1.borrarSubA("2")
   print (A1.buscarSubA("2"))
   print (A1)

main()    
	
