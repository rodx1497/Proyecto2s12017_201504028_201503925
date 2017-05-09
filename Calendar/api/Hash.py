import os
class TablaHash():
	nombre=""
	direccion=""
	descripcion=""
	hora=""
	dia=0
	mes=""
	anio=0
	estado=0

	def __init__(self):
		pass

		
	def funcionHash(self,n,m):
		key=0
		cad=str(n*n)
		tamanio=len(cad)
		
		if tamanio%2==0:
			pos=tamanio/2
			key=int(cad[pos-1]+cad[pos])
		else:
			pos=(tamanio-1)/2	
			key=int(cad[pos-1]+cad[pos])
		
		print "FINAL KEY: "+str(key)
		return key
		#return key%m
		#return (n+1)%m

	def insertaHash(self, arrHash, m, n,nombre,direccion,hora,desc,month,year,dia):
		print "HASH222---"+nombre+" "+direccion+" "+hora+" "+desc+" "+month+" "+year
		correcto=False
		direccion=direccion+" "
		j=self.funcionHash(n,m)
		while j<m and not correcto:
			if arrHash[j].estado==0 or arrHash[j].estado==1:
				arrHash[j].nombre=nombre
				if not direccion.replace(" ","")=="":
					arrHash[j].direccion=direccion	
					pass
				else:
					arrHash[j].direccion="Sin Direccion"
					pass
				arrHash[j].hora=hora
				arrHash[j].descripcion=desc
				arrHash[j].mes=month
				arrHash[j].anio=year
				arrHash[j].dia=dia
				arrHash[j].estado=2
				correcto=True
				break	
				pass
			else:
				print "OCURRIO UNA COLISION, ---- AUMENTANDO POS "+str(j)
				j+=1
			pass

		if correcto:
			print "Insertado Exitosamente"
			print "Insertado en la posiccion : "+str(j)+" "+arrHash[j].nombre
		else:
			print "Tabla Llena"

	def buscarHash(self, arrHash,m,n,nombre):
		j= self.funcionHash(n,m)
		while j<m:
			if arrHash[j].estado==0:
				return "0"
				pass
			elif arrHash[j].nombre==nombre:
				if arrHash[j].estado==1:
					return "-1"
					pass
				else:
					return str(j)
			else:
				j+=1
			pass
		#return "-1"

	def eliminarHash(self,arrHash,m,n,nombre):
		i=int(self.buscarHash(arrHash,m,n,nombre))
		if i==-1:
			return -1
			pass
		else:
			arrHash[int(i)].estado=1
			print "ELIMINADO DE HASH"
			return 1


class Hash():
	"""docstring for Hash"""
	size=0
	arrHash=[]
	
	def __init__(self):
		size=50
		self.m=100
		self.thash=TablaHash()
		self.arrHash=[TablaHash()]
		for x in xrange(0,self.m):
			self.arrHash.insert(x,TablaHash())
			self.arrHash[x].estado=0
			pass
		

	def insertar(self,nombre,direccion,hora,desc,month,year,dia):
		n=0
		for x in xrange(0,len(nombre)):
			n+=ord(nombre[x])
			pass
			#print "HASH------- "+month+" "+year
		self.thash.insertaHash(self.arrHash,self.m,n,nombre,direccion,hora,desc,month,year,dia)
		
		if self.factor()>=0.8:
			self.rehash()
			pass

	def eliminar(self,nombre):
		n=0
		for x in xrange(0,len(nombre)):
			n+=ord(nombre[x])
			pass
		self.thash.eliminarHash(self.arrHash,self.m,n,nombre)


	def factor(self):
		return self.noData()/self.m
		
	def buscar(self,nombre):
		n=0
		for x in xrange(0,len(nombre)):
			n+=ord(nombre[x])
			pass
		aux= self.thash.buscarHash(self.arrHash,self.m,n,nombre)
		if aux=="-1" or aux=="0":
			print "No Encontrado"
			return "No Encontrado"
			pass
		else:
			print "El Valor es "+self.arrHash[int(aux)].nombre
			return self.arrHash[int(aux)].nombre

		return "No Encontrado"

	def obtenerDatos(self,nombre):
		n=0
		json=""
		for x in xrange(0,len(nombre)):
			n+=ord(nombre[x])
			pass
		aux= self.thash.buscarHash(self.arrHash,self.m,n,nombre)
		if aux=="-1" or aux=="0":
			#print "No Encontrado"
			return "No Encontrado"
			pass
		else:
			print "El Valor es "+self.arrHash[int(aux)].nombre
			return self.arrHash[int(aux)].nombre

		return "No Encontrado"


	def imprimir(self):
		for x in range(0,self.m):
			if self.arrHash[x].estado==2:
				print "POSICION: "+str(x)+" names: "+self.arrHash[x].nombre
				pass
	
	def rehash(self):
		if self.factor()>=0.8:
			self.m*=2
			self.arrHash2=[TablaHash()]
			for x in xrange(0,self.m/2):
				if self.arrHash[x].estado!=1:
					self.arrHash2.insert(x,self.arrHash[x])
					pass
				else:
					self.arrHash2.insert(x,TablaHash())
					self.arrHash2[x].estado=0
				pass
			for x in xrange((self.m/2)+1,self.m):
				self.arrHash2.insert(x,TablaHash())
				self.arrHash2[x].estado=0
				pass
			
			self.arrHash=self.arrHash2
			pass

	def noData(self):
		no=0
		for x in range(0,self.m):
			if self.arrHash[x].estado==2:
				no+=1
				pass
		return no

	def jsonDia(self):
		json=""
		flag=0
		for x in range(0,self.m):
			if self.arrHash[x].estado==2:
				if self.m!=x and flag>0:
					json+=","
					pass
				json+="{"
				json+="\"evento\":\""+str(self.arrHash[x].nombre)+"\","
				json+="\"direccion\":\""+str(self.arrHash[x].direccion)+"\","
				json+="\"descripcion\":\""+str(self.arrHash[x].descripcion)+"\","
				json+="\"hora\":\""+str(self.arrHash[x].hora)+"\","
				json+="\"dia\":\""+str(self.arrHash[x].dia)+"\","
				json+="\"month\":\""+str(self.arrHash[x].mes)+"\","
				json+="\"year\":\""+str(self.arrHash[x].anio)+"\""
				json+="}"
				
				flag=1
				pass
				
				
		return json

	def jsonDiaDia(self):
		json=""
		flag=0
		for x in range(0,self.m):
			if self.arrHash[x].estado==2:
				if self.m!=x and flag>0:
					json+=","
					pass
				json+="{"
				json+="\"evento\":\""+str(self.arrHash[x].nombre)+"\","
				json+="\"hora\":\""+str(self.arrHash[x].direccion)+"\","
				json+="\"direccion\":\""+str(self.arrHash[x].descripcion)+"\","
				json+="\"descripcion\":\""+str(self.arrHash[x].hora)+"\","
				json+="\"dia\":\""+str(self.arrHash[x].dia)+"\","
				json+="\"month\":\""+str(self.arrHash[x].mes)+"\","
				json+="\"year\":\""+str(self.arrHash[x].anio)+"\""
				json+="}"
				
				flag=1
				pass
				
				
		return json


	def json(self):
		json=""
		for x in range(0,self.m):
			if self.arrHash[x].estado==2:
				json+="{"
				json+="\"evento\":\""+str(self.arrHash[x].nombre)+"\","
				json+="\"direccion\":\""+str(self.arrHash[x].direccion)+"\","
				json+="\"descripcion\":\""+str(self.arrHash[x].descripcion)+"\","
				json+="\"hora\":\""+str(self.arrHash[x].hora)+"\","
				json+="\"dia\":\""+str(self.arrHash[x].dia)+"\","
				json+="\"month\":\""+str(self.arrHash[x].mes)+"\","
				json+="\"year\":\""+str(self.arrHash[x].anio)+"\""
				json+="}"
				pass
		return json


	def graficar(self):
		body="tabla[shape=record label=<<TABLE color=\"blueviolet\">"
		for x in range(0,self.m):
			if self.arrHash[x].estado==2:
				body+="<TR> \n"
				body+= "<TD color=\"blue\" ><FONT color=\"red\">"+str(x)+" </FONT></TD> <TD color=\"blue\"><FONT color=\"red\"> "+self.arrHash[x].nombre+"</FONT></TD>\n"
				body+="</TR> \n"
				pass
		body+="</TABLE>> ]"

		return body

	def graficarDia(self):
		archivoDot="digraph grafo{ \n"
		archivoDot+="rank=LR\n color=\"blueviolet\" \n edge [color=red]; \n node [shape=ellipse,color=\"blue\"];"
		archivoDot+=self.graficar()
		archivoDot+="}"
		try:
			arch=open("C:\graphviz-2.38\\release\EDD\\"+"hash.dot","w")
			arch.write(archivoDot)
			arch.close()
			os.system('C:\graphviz-2.38\\release\\bin\dot.exe -Tpng C:\graphviz-2.38\\release\EDD\hash.dot -o C:\graphviz-2.38\\release\EDD\hash.png')
			pass
		except Exception as e:
			raise e