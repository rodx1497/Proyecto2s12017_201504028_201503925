from matDispersa import MatrizDispersa
class Nodo():
	def __init__(self,usuario,password):
		self.usuario=usuario 
		self.sig=None
		self.ant=None
		self.password=password
		self.mt=MatrizDispersa()
		self.vinculado=False

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
		if self.isEmpty() == True:
			self.first=self.last=nuevo
		else:
			self.last.sig=nuevo
			nuevo.ant=self.last
			self.last=nuevo


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

	def imprimir(self):
		for x in xrange(0,self.getSize()):
			print "Usuario: "+self.extraerUsuario(x) + " Password: "+self.extraerPass(x)
			pass