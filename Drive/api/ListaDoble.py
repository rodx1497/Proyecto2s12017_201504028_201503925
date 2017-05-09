from matDispersa import MatrizDispersa
import os
class Nodo():
	def __init__(self,usuario,password):
		self.usuario=usuario 
		self.sig=None
		self.ant=None
		self.password=password
		self.mt=MatrizDispersa()
		self.usuarioDrive=""
		self.passwordDrive=""
		

	def getUserDrive(self):
		return self.usuarioDrive

	def getUser(self):
		return self.usuario 

	def getMat(self):
		return self.mt
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
		nodotem=self.first
		nodotem2=self.first
		index=index-1

		while(contador<index):
			
			if contador== index:
				print "Entra"
				nodotem.sig=nodotem.sig.sig
				if nodotem.sig.sig!=None:
					nodotem.sig.sig.ant=nodotem
					pass
				break
				return True
				pass
			print "no"
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

	def extraerUsuarioDrive(self, indice):
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
		return nodotem.getUserDrive()

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

	def extraerMD(self, indice):
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
		return nodotem.getMat()

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
				return notem.getMat()
				break
			notem=notem.sig
			pass
		return None

	def buscar2(self,cadena):
		tem=self.first
		while tem!=None:
			if tem.getUser().replace(" ","")==cadena.replace(" ",""):
				return tem.getMat()
				break
			tem=tem.sig
			pass
		return None

	def graficarUsuarios(self):
		body=""
		print self.getSize()
		for x in xrange(0,self.getSize()-1):
			body+=self.extraerUsuario(x).replace(" ","")+self.extraerUsuarioDrive(x)+"->"+self.extraerUsuario(x+1).replace(" ","")+self.extraerUsuarioDrive(x+1)+";"
			body+=self.extraerUsuario(x+1).replace(" ","")+self.extraerUsuarioDrive(x+1)+"->"+self.extraerUsuario(x).replace(" ","")+self.extraerUsuarioDrive(x)+";"
			
			pass
		return body

	def login(self, cadena,password):
		notem=self.first
		cont=0
		for x in xrange(0,self.getSize()):
			if notem.getUser().replace(" ","")==cadena.replace(" ","")and notem.password.replace(" ","")==password:
				return True
				break
			notem=notem.sig
			pass
		return False

	def loginUsuario(self,user,password):
		for x in xrange(0,self.getSize()):
			if self.extraerUsuario(x).replace(" ","")==user and self.extraerPass(x).replace(" ","")==password:
				return True
				pass
			pass
		return False


	def vincularDrive(self,usuario,usuarioDrive,passDrive):
		self.buscar(usuario).usuarioDrive=usuario
		self.buscar(usuario).passDrive=passDrive

	def imprimir(self):
		for x in xrange(0,self.getSize()):
			print "Usuario: "+self.extraerUsuario(x) + " Password: "+self.extraerPass(x)
			pass

	def grafica_Users_Calendar(self):
		archivoDot="digraph grafo{ \n"
		archivoDot+="rank=LR\n color=\"blueviolet\" \n edge [color=red]; \n node [shape=ellipse,color=\"blue\"];"
		archivoDot+=self.graficarUsuarios()
		archivoDot+="}"
		try:
			arch=open("C:\graphviz-2.38\\release\EDD\\"+"listaCalendar.dot","w")
			arch.write(archivoDot)
			arch.close()
			os.system('C:\graphviz-2.38\\release\\bin\dot.exe -Tpng C:\graphviz-2.38\\release\EDD\listaCalendar.dot -o C:\graphviz-2.38\\release\EDD\ListaCalendar.png')
			pass
		except Exception as e:
			raise e