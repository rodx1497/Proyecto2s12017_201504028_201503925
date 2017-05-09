import os 

class Nodo():
	def __init__(self,dato):
		self.dato=dato 
		self.sig=None

	def getDato(self):
		return self.dato 


class ListaSimple():

	def __init__(self):
		self.first=None
		self.last=None
	def isEmpty(self):
		if self.first==None:
			return True
		else:
			return False
	def insertar(self, dato):
		nuevo=Nodo(dato)
		if self.isEmpty() == True:
			self.first=self.last=nuevo
		else:
			self.last.sig=nuevo
			self.last=nuevo

	def eliminar(self,ind):
		index=int(ind)
		contador=0
		nodotem=self.first
		nodotem2=self.first
		index=index-1

		while(contador<=index):
			
			if contador== index:
				nodotem.sig=nodotem.sig.sig
				break
			pass
			nodotem=nodotem.sig
			contador=contador+1
		pass

	def extraer(self, indice):
		nodotem=self.first
		contad=0
		while (contad<indice and nodotem.sig!=None):
			nodotem=nodotem.sig
			contad=contad+1
			pass
		
		if indice>self.getSize():
			return None
		if nodotem==None:
			return "Ya no hay datos"
			pass
		return nodotem.getDato()

	def getSize(self):
		contador=0
		temp=self.first
		while(temp!=None):
			temp=temp.sig
			contador=contador+1
		pass
		return contador


	def buscar(self, cadena):
		notem=self.first
		cont=0
		for x in xrange(0,self.getSize()):
			if notem.getDato()==cadena:
				return "Indice "+ str(x)
				break
			notem=notem.sig
			pass
		return "No se encontro"


	def graficarBitacora(self):
		body=""
		print self.getSize()
		if self.getSize()==1:
			body+=self.getDato().replace(" ","_")+";"
		else:
			for x in xrange(0,self.getSize()-1):
				body+=self.extraer(x).replace(" ","_")+"->"+self.extraer(x+1).replace(" ","_")+";"
				body+=self.extraer(x+1).replace(" ","_")+"->"+self.extraer(x).replace(" ","_")+";"
				pass
			pass
		
		return body

	def grafica_Bitacora_Calendar(self):
		archivoDot="digraph grafo{ \n"
		archivoDot+="rank=LR\n color=\"blueviolet\" \n edge [color=red]; \n node [shape=ellipse,color=\"blue\"];"
		archivoDot+=self.graficarBitacora()
		archivoDot+="}"
		try:
			arch=open("C:\graphviz-2.38\\release\EDD\\"+"bitacoraCalendar.dot","w")
			arch.write(archivoDot)
			arch.close()
			os.system('C:\graphviz-2.38\\release\\bin\dot.exe -Tpng C:\graphviz-2.38\\release\EDD\\bitacoraCalendar.dot -o C:\graphviz-2.38\\release\EDD\\bitacoraCalendar.png')
			pass
		except Exception as e:
			raise e