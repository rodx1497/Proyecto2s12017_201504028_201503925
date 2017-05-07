#from ArbolB import _Carpeta
from ArbolB import ArbolB
from Cmd import cmd
from subprocess import check_output
import os

class Nodo():
	def __init__(self,usuario,password):
		self.usuario=usuario 
		self.sig=None
		self.ant=None
		self.password=password
		self.arbol=ArbolB(5)
		#self.arbol=_Carpeta("/")

	def getUser(self):
		return self.usuario 

	def getTree(self):
		return self.arbol

	def getPassword(self):
		return self.password

class ListaDoble():

	def __init__(self):
		self.first=None
		self.last=None

	def isEmpty(self):
		if self.first==None:
			return True
		else:
			return False

	def insertar(self, User,password):
		nuevo=Nodo(User,password)
		flag=False
		for x in xrange(0,self.getSize()):
			if User==self.extraerUsuario(x):
				flag=True
				pass
			pass
		if flag==False:
			if self.isEmpty() == True:
				self.first=self.last=nuevo
			else:
				self.last.sig=nuevo
				nuevo.ant=self.last
				self.last=nuevo
			return "Ingreso Correcto"
		else:
			return "Ingreso Incorrecto"


	def eliminar(self,index):
		contador=0
		nodotem=nodotem2=self.first
		index=index-1

		while(contador<index):
			
			if contador== index:
				nodotem.sig=nodotem.sig.sig
				if nodotem.sig.sig!=None:
					nodotem.sig.sig.ant=nodotem
					pass
				break
				return True
				pass
			nodotem=nodotem.sig
			contador=contador+1
			pass
		return False

	def extraerUsuario(self, indice):
		nodotem=self.first
		contad=0
		while (contad<indice and nodotem.sig!=None):
			nodotem=nodotem.sig
			contad=contad+1
			pass
		
		if indice>self.getSize():
			return None
		if nodotem==None:
			return None
			pass
		return nodotem.getUser()

	def extraerPass(self, indice):
		nodotem=self.first
		contad=0
		while (contad<indice and nodotem.sig!=None):
			nodotem=nodotem.sig
			contad=contad+1
			pass
		
		if indice>self.getSize():
			return None
		if nodotem==None:
			return None
			pass
		return nodotem.getPassword()

	def extraerArbol(self, indice):
		nodotem=self.first
		contad=0
		while (contad<indice and nodotem.sig!=None):
			nodotem=nodotem.sig
			contad=contad+1
			pass
		
		if indice>self.getSize():
			return None
		if nodotem==None:
			return None
			pass
		return nodotem.getTree()

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
			print "$"+notem.getUser().replace(" ","")+" "+cadena.replace(" ","")+"$"
			if notem.getUser().replace(" ","")==cadena.replace(" ",""):
				return notem.getTree()
				break
			notem=notem.sig
			pass
		return None

	def imprimir(self):
		for x in xrange(0,self.getSize()):
			print "Usuario: "+self.extraerUsuario(x) + " Password: "+self.extraerPass(x)
			pass

	def graficar(self):
		tem = self.first
		cadenan="digraph g{"


		while (tem!=None):
			tem.getinfo()
			tem= tem.getsig()

		tem = self.first
		while (tem!=None and tem.getsig()!=None):
			cadenan=cadenan+(str(tem.getinfo()))+"->"+ str(tem.getsig().getinfo())+";"
			tem= tem.getsig()
		cadenan = cadenan+(str(tem.getinfo()))+"->"+"None;"
		cadenan=cadenan+"}"
		print(str(cadenan))
		archi=open('datos.txt','w')
		archi.close()
		archi=open('datos.txt','a')
		archi.write(cadenan)

		archi.close()

		check_output('"C:\\graphviz-2.38\\bin\\dot.exe" -Tjpg C:\\Users\\Rod\\datos.txt -o C:\\Users\\Rod\\grafo1.jpg', shell=True)

	def graficarUsuarios(self):
		body=""
		for x in xrange(0,self.getSize()-1):
			body+=self.extraerUsuario(x).replace(" ","")+"->"+self.extraerUsuario(x+1).replace(" ","")+";"
			body+=self.extraerUsuario(x+1).replace(" ","")+"->"+self.extraerUsuario(x).replace(" ","")+";"
			pass
		return body

	def grafica_Users_Calendar(self):
		archivoDot="digraph grafo{ \n"
		archivoDot+="rank=LR\n color=\"blueviolet\" \n edge [color=red]; \n node [shape=ellipse,color=\"blue\"];"
		archivoDot+=self.graficarUsuarios()
		archivoDot+="}"
		try:
			arch=open("C:\graphviz-2.38\\EDD\\"+"listaCalendar.dot","w")
			arch.write(archivoDot)
			arch.close()
			os.system('C:\graphviz-2.38\\bin\dot.exe -Tpng C:\graphviz-2.38\\EDD\listaCalendar.dot -o C:\graphviz-2.38\\EDD\ListaCalendar.png')
			pass
		except Exception as e:
			raise e

if __name__ == '__main__':

	ldb = ListaDoble()

	ldb.insertar("Fierro","Pariente")
	ldb.insertar("Maluma","beibi")
	ldb.insertar("Alcazar","Corollaz")

	#ldb.buscar("Maluma").extraerArbol().agregarCarpeta("pichorizo")

	ldb.imprimir()
	ldb.grafica_Users_Calendar()