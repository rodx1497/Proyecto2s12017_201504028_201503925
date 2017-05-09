import os
from Hash import Hash

class Nodo():
	def __init__(self,dato,f="",c="",ids=0):
		self.dato=dato 
		self.sig=None
		self.ant=None
		self.arriba=None
		self.abajo=None
		self.atras=None
		self.frente=None
		self.f=f
		self.c=c
		self.id=ids
		self.tablaHash=Hash()


	def getHash(self):
		return self.h
	def getDato(self):
		return self.dato 
	def getFi(self):
		return self.f
	def getCol(self):
		return self.c
	def setDato(self,data):
		self.dato=data
	def getID(self):
		return str(self.id)+""

class MatrizDispersa():
	def __init__(self):
		self.first=None

	def existeCol(self,nombre):
		aux=self.first
		while aux!=None:
			if aux.getDato()==nombre:
				return True
				break
				pass
			aux=aux.sig
			pass
		return False

	def existeFila(self,nombre):
		aux=self.first
		while aux!=None:
			if aux.getDato()==nombre:
				return True
				break
				pass
			aux=aux.abajo
			pass
		return False

	def Grafica_Hash_Dia_Especifico(self,col,fil,dia):
		aux=self.first
		while aux!=None:
			if aux.getDato()==fil:
				aux=aux.sig
				while aux!=None:
					if aux.getCol()==col:
						while aux!=None:
							if aux.getDato()==dia:
								print "####---------GRAFICANDO_DIA---------####"
								#Comprobar que la tabla no tenga un elemento igual
								aux.tablaHash.graficarDia()
							else:
								print "--------------BUSCANDO--------"

							aux=aux.atras
							pass						

						pass
					if aux!=None:
						aux=aux.sig
						pass
					pass
				pass
			if aux!=None:
				aux=aux.abajo
				pass
			pass



	def Si_Existe_Insertar_Dato(self,col,fil,dia,evento,desc,direccion,hora):

		aux=self.first
		while aux!=None:
			if aux.getDato()==fil:
				print "FILA IGUAL A FILA -----------"
				aux=aux.sig
				while aux!=None:
					if aux.getCol()==col:
						print "----------COL IGUAL A COL-----------------"
						
						while aux!=None:
							if aux.getDato()==dia:
								#print "####---------EXISTEDATO---------####"
								#print "Existe Dato, Insertando en Tabla Hash"
								#Comprobar que la tabla no tenga un elemento igual
								aux.tablaHash.insertar(evento,direccion,hora,desc,fil,col,dia)
								return 0
								if aux.tablaHash.buscar(evento)=="No Encontrado":
									#print "Ya existe un valor igual"
									return 0
									break
									pass
								else:
									#"############################INSERTADO"
									aux.tablaHash.insertar(evento,direccion,hora,desc,fil,col,dia)
									break
									return 1
								pass
							else:
								#print ".---------------------------NO ESTA"
								print aux.getDato()+" "+str(dia)
								pass


							aux=aux.atras
							pass
						

						pass
					if aux!=None:
						aux=aux.sig
						pass
					pass
				pass
			if aux!=None:
				aux=aux.abajo
				pass
			pass
		return 2		

	def insertar(self, col,fil,dia,evento,direccion,hora,desc):
		
		dato=Nodo(dia,fil,col)
		nuevaCol=Nodo(col)
		nuevaFila=Nodo(fil)
		existencia=self.Si_Existe_Insertar_Dato(col,fil,dia,evento,desc,direccion,hora)
		
		if existencia==1 or existencia==0:

			pass
		elif existencia==2:
		
			if self.first == None:
				self.first=Nodo("i")
				columna=Nodo(col)
				fila=Nodo(fil)
				self.first.sig=columna
				self.first.abajo=fila
				columna.ant=self.first
				fila.arriba=self.first
				columna.abajo=dato
				fila.sig=dato
				dato.arriba=columna
				dato.ant=fila
				dato.tablaHash.insertar(evento,direccion,hora,desc,fil,col,dia)
			elif self.first.sig==None and self.first.abajo==None:
				self.first.sig=columna
				self.first.abajo=fila
				columna.ant=self.first
				fila.arriba=self.first
				columna.abajo=dato
				fila.sig=dato
				dato.arriba=columna
				dato.ant=fila
				dato.tablaHash.insertar(evento,direccion,hora,desc,fil,col,dia)

			elif not self.existeCol(col) and not self.existeFila(fil):
				aux=self.first.sig
				aux2=self.first.abajo
				while int(col)>int(aux.getDato()):
					if aux.sig!=None:
						aux=aux.sig
					else:
						break
				while aux2.getDato()<fil:
					if aux2.abajo!=None:
						aux2=aux2.abajo
					else:
						break
				if int(col)>int(aux.getDato()):
					print "col > aux.getDato() "+col+" "+aux.getDato()
					nuevaCol.sig=aux.sig #aplicar apuntador de regreso
					nuevaCol.ant=aux
					aux.sig=nuevaCol
				else:
					print "col < aux.getDato() "+col+" "+aux.getDato()
					nuevaCol.ant=aux.ant
					nuevaCol.sig=aux
					aux.ant.sig=nuevaCol
					aux.ant=nuevaCol

				if fil[0]>aux2.getDato()[0]:
					print "fil > aux2.getDato() "+fil+" "+aux2.getDato()
					nuevaFila.abajo=aux2.abajo
					nuevaFila.arriba=aux2
					aux2.abajo=nuevaFila
				else:
					print "fil < aux2.getDato() "+fil+" "+aux2.getDato()
					nuevaFila.arriba=aux2.arriba
					
					nuevaFila.abajo=aux2
					aux2.arriba.abajo=nuevaFila
					aux2.arriba=nuevaFila
					#posible error
				nuevaCol.abajo=dato
				nuevaFila.sig=dato
				dato.arriba=nuevaCol
				dato.ant=nuevaFila
				dato.tablaHash.insertar(evento,direccion,hora,desc,fil,col,dia)
			elif self.existeCol(col)==True and self.existeFila(fil)==True:
				print "******Insercion en columna y fila existente******"
				aux=self.first.sig
				aux2=self.first.abajo
				while aux!=None and col!=aux.getDato():
					aux=aux.sig
					pass
				aux=aux.abajo
				
				while aux!=None:
					encontrado=False
					if aux.getFi()==fil and aux.getCol()==col:
						#Insercion de otro dia en 3ra dimension
						if aux.getCol()==col:
							print "aux.getFi()==fil "+aux.getFi()+" "+fil+" || "+aux.getCol()+" = "+col
							encontrado=True	
							pass
						
						if aux.atras==None:
							print "Insercion con dos datos----"
							if int(dia)>int(aux.getDato()):		
								aux.atras=dato
								dato.frente=aux
								pass
							else:
								dato.arriba=aux.arriba
								dato.abajo=aux.abajo
								dato.ant=aux.ant
								dato.sig=aux.sig
								dato.atras=aux
								aux.arriba.abajo=dato
								if aux.abajo!=None:
									aux.abajo.arriba=dato
									pass
								aux.ant.sig=dato
								if aux.sig!=None:
									aux.sig.ant=dato	
									pass
								aux.frente=dato
								#Hacer Nulo los demas punteros del aux		
							pass
						else:
							print "Insercion con mas datos"
							auxN=aux
							while auxN.atras!=None and int(dia)>int(auxN.getDato()):
								print "+++dia > auxN.getDato() "+dia+" "+auxN.getDato()
								auxN=auxN.atras
								pass
							#Insercion al inicio

							if auxN.frente==None:
								print "Insercion al inicio"
								self.insercionInicio(dia,auxN,dato)
							#Insercion al final
							elif auxN.atras==None:
								print "insercion al final"
								self.insercionFinal(dia,auxN,dato)
							#Insercion en medio
							elif auxN.frente!=None and auxN.atras!=None:
								print "insercion en el centro"
								self.insercionCentro(dia,auxN,dato) 
						pass
					elif aux.getFi()[0]>fil[0]:
						#Insercion de nuevo nodo
						break
					aux=aux.abajo
					pass

				aux=self.first.sig
				while aux!=None and col!=aux.getDato():
					aux=aux.sig
					pass
				aux=aux.abajo

				#Encontrar apuntadores de fila
				auxF=self.first.abajo
				while auxF!=None and fil!=auxF.getDato():
					auxF=auxF.abajo
					pass
				auxF=auxF.sig
				print str(int(auxF.getDato()))+" > "+col+" -------------"
				#print "sig de auxF.sig= "+str(auxF.sig.getDato())
				#Se cambio el signo :C <
				while int(auxF.getCol())<int(col) and auxF.sig!=None:
					print auxF.getDato()+" #### "+str(auxF.sig.getDato())
					auxF=auxF.sig
					pass
				print "valor de encontrado= "+str(encontrado)
				if encontrado==False:
					#Insercion antes de col y fila
					print "insertando en fila y col EXISTENTE SIN DATOS"
					if aux.getFi()[0]>fil[0] and int(auxF.getCol())>int(col):
						print "los dos mayores"
						#AUX fila > fila
						dato.abajo=aux
						dato.arriba=aux.arriba
						aux.arriba.abajo=dato
						aux.arriba=dato
						# auxF col > col
						dato.ant=auxF.ant
						dato.sig=auxF
						auxF.ant.sig=dato
						auxF.ant=dato
						pass
					elif aux.getFi()[0]<fil[0] and int(auxF.getCol())<int(col):
						print "los dos menores"
						print "Ingresando dato "+dato.getDato()+" valor aux: "+aux.getDato()+"  auxF: "+auxF.getDato() #+" auxF.sig: "+auxF.sig.getDato()
						print aux.getFi()+" < "+fil+" ... "+auxF.getCol()+" < "+col
						dato.arriba=aux	
						dato.abajo=aux.abajo
						if aux.abajo!=None:
							aux.abajo.arriba=dato
						aux.abajo=dato

						dato.sig=auxF.sig
						dato.ant=auxF
						if auxF.sig!=None:
							auxF.sig.ant=dato
						auxF.sig=dato
						

					elif aux.getFi()[0]>fil[0] and int(auxF.getCol())<int(col):
						print "mayor y menor"
						print aux.getDato()+" "+aux.getDato() +" "+fil+" "+auxF.getDato()+" "+dato.getDato()
						dato.abajo=aux
						dato.arriba=aux.arriba
						aux.arriba.abajo=dato
						aux.arriba=dato

						dato.sig=auxF.sig
						dato.ant=auxF
						if auxF.sig!=None:
							auxF.sig.ant=dato
						auxF.sig=dato
					elif aux.getFi()[0]<fil[0] and int(auxF.getCol())>int(col):
						print "menor y mayor"
						print aux.getFi() +" "+fil+" "+auxF.getCol()+" "+col
						dato.arriba=aux	
						dato.abajo=aux.abajo
						if aux.abajo!=None:
							aux.abajo.arriba=dato
						aux.abajo=dato

						dato.ant=auxF.ant
						dato.sig=auxF
						auxF.ant.sig=dato
						auxF.ant=dato
						
					pass
				dato.tablaHash.insertar(evento,direccion,hora,desc,fil,col,dia)
			elif self.existeCol(col) and not self.existeFila(fil):
				print "EXISTE COLUMNA PERO NO FILA"
				aux=self.first.sig
				aux2=self.first.abajo
				while aux.sig!=None and col!=aux.getDato():
					print "aux "+aux.getDato()
					aux=aux.sig
					pass
				aux=aux.abajo
				while aux.abajo!=None and fil[0]>aux.getFi()[0]:
					aux=aux.abajo
					pass
				while aux2.abajo!=None and fil[0]>aux2.getDato()[0]:
					aux2=aux2.abajo
					pass
				
				if (aux.getFi()[0]>fil[0] or aux.getFi()>fil) and aux2.getDato()>fil:
					print "MAYOR, MAYOR"
					#AUX fila > fila
					self.insertarAntes(aux,dato)
					nuevaFila.sig=dato
					dato.ant=nuevaFila
					self.insertarAntesFila(nuevaFila,aux2)
					pass
				elif (aux.getFi()[0]<fil[0] or aux.getFi()<fil) and aux2.getDato()<fil:
					print "MENOR, MENOR"
					self.insertarDespues(aux,dato)
					nuevaFila.sig=dato
					dato.ant=nuevaFila
					self.insertarDespuesFila(nuevaFila,aux2)
					pass
				elif (aux.getFi()[0]>fil[0] or aux.getFi()>fil) and aux2.getDato()<fil:
					print "MAYOR, MENOR"
					#AUX fila > fila
					self.insertarAntes(aux,dato)
					nuevaFila.sig=dato
					dato.ant=nuevaFila
					self.insertarDespuesFila(nuevaFila,aux2)
					pass
				elif (aux.getFi()[0]<fil[0] or aux.getFi()<fil) and aux2.getDato()>fil:
					print "MENOR, MAYOR"
					#AUX fila > fila
					self.insertarDespues(aux,dato)
					nuevaFila.sig=dato
					dato.ant=nuevaFila
					self.insertarAntesFila(nuevaFila,aux2)
					pass
				dato.tablaHash.insertar(evento,direccion,hora,desc,fil,col,dia)
			elif not self.existeCol(col) and self.existeFila(fil):
				print "EXISTE FILA PERO NO COLUMNA"
				aux=self.first.abajo
				aux2=self.first.sig
				while aux.abajo!=None and fil!=aux.getDato():
					aux=aux.abajo
					pass
				aux=aux.sig
				while aux.sig!=None and int(col)>int(aux.getCol()):
					aux=aux.sig
					pass
				while aux2.sig!=None and int(col)>int(aux2.getDato()):
					print str(int(col))+" > "+str(int(aux2.getDato()))
					print "VALOR ACTUAL DE AUX2:  "+aux2.getDato()
					aux2=aux2.sig
					pass
				
				if int(aux.getCol())>int(col) and int(aux2.getDato())>int(col):
					print "MAYOR, MAYOR"
					self.insertarAntesC(aux,dato)
					nuevaCol.abajo=dato
					dato.arriba=nuevaCol
					self.insertarAntesCol(nuevaCol,aux2)
					pass
				elif int(aux.getCol())<int(col) and int(aux2.getDato())<int(col):
					print "MENOR, MENOR"
					self.insertarDespuesC(aux,dato)
					nuevaCol.abajo=dato
					dato.arriba=nuevaCol
					self.insertarDespuesCol(nuevaCol,aux2)
					pass
				elif int(aux.getCol())>int(col) and int(aux2.getDato())<int(col):
					print "MAYOR, MENOR"
					self.insertarAntesC(aux,dato)
					nuevaCol.abajo=dato
					dato.arriba=nuevaCol
					self.insertarDespuesCol(nuevaCol,aux2)
					pass
				elif int(aux.getCol())<int(col) and int(aux2.getDato())>int(col):
					print "MENOR, MAYOR"
					self.insertarDespuesC(aux,dato)
					nuevaCol.abajo=dato
					dato.arriba=nuevaCol
					self.insertarAntesCol(nuevaCol,aux2)
					pass
				dato.tablaHash.insertar(evento,direccion,hora,desc,fil,col,dia)

	def insertarAntesFila(self,nuevaFila,aux):
		nuevaFila.abajo=aux
		nuevaFila.arriba=aux.arriba
		aux.arriba.abajo=nuevaFila
		aux.arriba=nuevaFila
	def insertarAntes(self, aux,dato):
		print "dato entrante: "+dato.getDato()+" valor entrante: "+aux.getDato()
		dato.abajo=aux
		dato.arriba=aux.arriba
		aux.arriba.abajo=dato
		aux.arriba=dato
	def insertarDespues(self,aux,dato):
		dato.arriba=aux	
		dato.abajo=aux.abajo
		if aux.abajo!=None:
			aux.abajo.arriba=dato
		aux.abajo=dato
	def insertarDespuesFila(self,nuevaFila,aux):
		nuevaFila.arriba=aux
		nuevaFila.abajo=aux.abajo
		if aux.abajo!=None:
			aux.abajo.arriba=nuevaFila	
			pass
		aux.abajo=nuevaFila
	
	def insertarAntesCol(self,nuevaCol,aux):
		print "AUX: "+aux.getDato()+" NUEVACOL:: "+nuevaCol.getDato()
		nuevaCol.sig=aux
		nuevaCol.ant=aux.ant
		aux.ant.sig=nuevaCol
		aux.ant=nuevaCol
	def insertarAntesC(self, aux,dato):
		dato.sig=aux
		dato.ant=aux.ant
		aux.ant.sig=dato
		aux.ant=dato
	def insertarDespuesC(self,aux,dato):
		dato.ant=aux	
		dato.sig=aux.sig
		if aux.sig!=None:
			aux.sig.ant=dato
		aux.sig=dato
	def insertarDespuesCol(self,nuevaCol,aux):
		nuevaCol.ant=aux
		nuevaCol.sig=aux.sig
		if aux.sig!=None:
			aux.sig.ant=nuevaCol	
			pass
		aux.sig=nuevaCol

	def insercionInicio(self,dia,auxN,dato):
		if int(dia)>int(auxN.getDato()):
			dato.frente=auxN
			dato.atras=auxN.atras
			auxN.atras.frente=dato
			auxN.atras=dato

		else:
			dato.arriba=auxN.arriba
			dato.abajo=auxN.abajo
			dato.ant=auxN.ant
			dato.sig=auxN.sig
			dato.atras=auxN
			auxN.arriba.abajo=dato
			if auxN.abajo!=None:
				auxN.abajo.arriba=dato
				pass
			auxN.ant.sig=dato
			if auxN.sig!=None:
				auxN.sig.ant=dato	
				pass
			auxN.frente=dato
			#Hacer Nulo los demas punteros del aux		
	def insercionCentro(self,dia,auxN,dato):
		if int(dia)>int(auxN.getDato()):
			print " insercion atras "+dia+" > "+auxN.getDato()
			dato.frente=auxN
			dato.atras=auxN.atras
			auxN.atras.frente=dato
			auxN.atras=dato
			pass
		else:
			dato.atras=auxN
			dato.frente=auxN.frente
			auxN.frente.atras=dato
			auxN.frente=dato
			
	def insercionFinal(self,dia,auxN,dato):
		if int(dia)>int(auxN.getDato()):
			dato.frente=auxN
			auxN.atras=dato
			pass
		else:
			dato.atras=auxN
			dato.frente=auxN.frente
			auxN.frente.atras=dato
			auxN.frente=dato

	def eliminar(self,dia,mes,anio,evento):
		print "Eliminar "+dia+" "+mes+" "+anio+" "+evento
		aux=self.first.sig
		eliminado=False

		while aux!=None and not eliminado:
			print aux.getDato()+" YEAR"
			if aux.getDato()==anio:
				aux=aux.abajo
				while aux!=None:
					if aux.getFi()==mes:
						print "Mes encontrado "+aux.getDato()
						if aux.getDato()==dia:
							print "DIA ENCONTRADO"
							#Eliminacion de primer nodo unico
							if aux.ant.ant==None and aux.sig==None and aux.arriba.arriba==None and aux.abajo==None and aux.atras==None:
								print "1111111"
								self.eliminarInicioUnico(aux,evento)	
								pass
							elif aux.atras!=None:
								print "22222"
								#Eliminar un nodo inicio con nodos atras
								self.eliminarInicialLista(aux,evento)
								pass
							elif aux.atras==None and aux.ant.ant==None and aux.sig==None and (aux.arriba.arriba!=None or aux.abajo!=None):
								#Eliminar dato y fila
								print "33333"
								self.eliminarDatoFila(aux,evento)
								pass
							elif aux.atras==None and  aux.arriba.arriba==None and aux.abajo==None and (aux.ant.ant!=None or aux.sig!=None):
								#Eliminar dato y columna
								print "4444"
								self.eliminarDatoColumna(aux,evento)
								pass
							elif aux.atras==None and (aux.ant.ant!=None or aux.sig!=None) and (aux.arriba.arriba!=None or aux.abajo!=None):
								#Eliminar un nodo inicio con datos en sus lados
								print "5555"
								self.eliminarDatoCentro(aux,evento)
								pass
							pass

						else:
							print "No es igual al dia"
							while aux!=None:
								print "Buscando dia "+aux.getDato()
								if aux!=None and aux.getDato()==dia:
									print "DIA ENCONTRADO ELSE"
									#Eliminacion en 3ra dimension
									self.eliminarCentro(aux,evento)
									break
									pass
								aux=aux.atras
								pass
							pass
						eliminado=True
						break
						pass
					aux=aux.abajo
					pass
				pass
			if aux!=None:
				aux=aux.sig
				pass
			pass

	def eliminarDatoCentro(self,aux,evento):
		
		if aux.tablaHash.noData()>1:
			aux.tablaHash.eliminar(evento)
			pass
		else:
			aux.ant.sig=aux.sig
			if aux.sig!=None:
				aux.sig.ant=aux.ant	
				pass
			aux.arriba.abajo=aux.abajo
			if aux.abajo!=None:
				aux.abajo.arriba=aux.arriba	
				pass
			aux=None		

	def eliminarDatoColumna(self,aux,evento):
		if aux.tablaHash.noData()>1:
			aux.tablaHash.eliminar(evento)
			pass
		else:
			aux.arriba.ant.sig=aux.arriba.sig
			if aux.arriba.sig!=None:
				aux.arriba.sig.ant=aux.arriba.ant
				pass
			aux.arriba=None
			aux.ant.sig=aux.sig
			if aux.sig!=None:
				aux.sig.ant=aux.ant
				pass
			aux=None
			pass

	def eliminarDatoFila(self,aux,evento):
		if aux.tablaHash.noData()>1:
			aux.tablaHash.eliminar(evento)
			pass
		else:
			aux.arriba.abajo=aux.abajo
			if aux.abajo!=None:
				aux.abajo.arriba=aux.arriba
				pass
			aux.ant.arriba.abajo=aux.ant.abajo
			if aux.ant.abajo!=None:
				aux.ant.abajo.arriba=aux.ant.arriba	
				pass
			aux=None	
			pass

	def eliminarInicioUnico(self,aux,evento):
		if aux.tablaHash.noData()>1:
			aux.tablaHash.eliminar(evento)
			pass
		else:
			if aux.ant.ant==None and aux.sig==None and aux.arriba.arriba==None and aux.abajo==None:
				aux.arriba.ant.sig=aux.arriba.sig
				if aux.arriba.sig!=None:
					aux.arriba.sig.ant=aux.arriba.ant
					pass
				aux.ant.arriba.abajo=aux.ant.abajo
				if aux.ant.abajo!=None:
					aux.ant.abajo.arriba=aux.ant.arriba	
					pass
				aux=None
				pass
			pass
	def eliminarInicialLista(self,aux,evento):
		if aux.tablaHash.noData()>1:
			aux.tablaHash.eliminar(evento)
			pass
		else:
			if aux.atras!=None:
			
				aux.atras.frente=aux.frente
				aux.atras.arriba=aux.arriba
				aux.atras.abajo=aux.abajo
				aux.atras.ant=aux.ant
				aux.atras.sig=aux.sig
				
				aux.arriba.abajo=aux.atras
				if aux.abajo!=None:
					aux.abajo.arriba=aux.atras	
					pass
				if aux.sig!=None:
					aux.sig.ant=aux.atras	
					pass
				aux.ant.sig=aux.atras
				aux=None
			
				pass


	def eliminarCentro(self, aux,evento):
		if aux.tablaHash.noData()>1:
			aux.tablaHash.eliminar(evento)
			pass
		else:
			if aux.frente!=None:
				aux.frente.atras=aux.atras
				if aux.atras!=None:
					aux.atras.frente=aux.frente	
					pass
				pass
				aux=None
			pass


	def imprimir(self):
		aux=self.first.sig
		while aux!=None:
			print "Dato Cabeza: "+aux.getDato()
			print "Dato Hijo: "+aux.abajo.getDato()
			if aux.abajo.abajo!=None:
				print "Dato Hijo2: "+str(aux.abajo.abajo.getDato())	
				pass
			
			print "Dato FilaN: "+aux.abajo.ant.getDato()
			data3=aux.abajo
			while data3.atras!=None:
				print "-------ATRAS: "+data3.atras.getDato()
				data3=data3.atras
				pass
			#print "Dato FilaNARR: "+aux.abajo.ant.arriba.getDato()
			#print "Dato FilaNARRabajo: "+aux.abajo.ant.arriba.abajo.getDato()
			aux=aux.sig
			pass

		aux=self.first
		while aux!=None:
			print "Dato Fila: "+aux.getDato()
			print "Dato Hijo: "+aux.sig.getDato()
			
			aux=aux.abajo
			pass

	def asignarID(self):
		auxC=self.first
		auxAB=self.first
		auxAT=self.first
		cont=1
		cad=""
		while auxC!=None:
			auxC.id=cont
			cad+=str(auxC.id)+" [label=\""+auxC.getDato()+"\"]; \n"
			auxAB=auxC.abajo			
			while auxAB!=None:
				cont+=1	
				auxAB.id=cont
				cad+=str(auxAB.id)+" [label=\""+auxAB.getDato()+"\"]; \n"
				auxAT=auxAB.atras
				while auxAT!=None:
					cont+=1
					auxAT.id=cont
					cad+=str(auxAT.id)+" [label=\""+auxAT.getDato()+"\"]; \n"
					auxAT=auxAT.atras
					pass
				auxAB=auxAB.abajo
				pass
			cont+=1
			auxC=auxC.sig
			pass
		print cad
		return cad

	def obtenerEventosDia(self,year, month,day):
		aux=self.first.sig
		json=""
		while aux!=None:
			if int(aux.getDato())==int(year):
				aux=aux.abajo
				while aux!=None:
					if aux.getFi()==month:
						while aux!=None:
							if aux.getDato()==day:
								json="["
								json+=aux.tablaHash.jsonDia()
								json+="]"
								return json
								pass
							aux=aux.atras
							pass
						pass
					if aux!=None:
						aux=aux.abajo	
						pass
					pass
				pass
			if aux!=None:
				aux=aux.sig	
				pass
			pass

	def obtenerEventosYear(self,year):
		aux=self.first.sig
		aux2=self.first
		aux3=self.first

		json="["
		while aux!=None:
			if int(aux.getDato())==int(year):
				aux=aux.abajo
				aux2=aux
				while aux!=None:
					aux2=aux
					while aux2!=None:						
						json+=aux2.tablaHash.jsonDia()
						if aux2.atras!=None:		
							print "SOME"
							json+=","	
							pass
						else:
							if aux.abajo!=None:
								print "SOME2"
								json+=","
								pass
						aux2=aux2.atras
						pass
					aux=aux.abajo	
					pass
				pass
			if aux!=None:
				aux=aux.sig	
				pass
			pass
		json+="]"
		return json

	def obtenerEventosMes(self,mes):
		aux=self.first.abajo
		aux2=self.first
		aux3=self.first

		json="["
		while aux!=None:
			if aux.getDato()==mes:
				aux=aux.sig
				while aux!=None:
					aux2=aux
					while aux2!=None:						
						json+=aux2.tablaHash.jsonDia()

						if aux2.atras!=None:
							json+=","
							pass
						else:
							if aux.sig!=None:
								json+=","
								pass
						aux2=aux2.atras
						pass
					aux=aux.sig	
					pass
				pass
			if aux!=None:
				aux=aux.abajo	
				pass
			pass
		json+="]"
		return json

	def generarMatriz(self):
		archivoDot="digraph grafo{ \n"
		archivoDot+=" color=\"blueviolet\" \n edge [color=red]; \n node [shape=ellipse,color=\"blue\"];"
		
		titulos=self.first
		body=""
		body+="{ "+self.asignarID()+"\n }"
		while titulos.sig!=None:
			body+=titulos.getID()+" -> "+titulos.sig.getID()+" [constraint=false]; \n"
			body+=titulos.sig.getID()+" -> "+titulos.getID()+" [constraint=false]; \n"
			body+="{ rank=same "+ titulos.getID()+" "+titulos.sig.getID() + " } \n" 
			datos=titulos
			datos2=titulos.sig
			while datos.abajo!=None:
				body+=datos.getID()+" -> "+datos.abajo.getID()+";"
				"""
				if datos.abajo.tablaHash.noData()>0:
					body+="S"+datos.abajo.getID()+datos.abajo.tablaHash.graficar()+";\n"
					body+=datos.abajo.getID()+"->"+"S"+datos.abajo.getID()+"tabla ;"
					pass
				"""
				print datos.getID()+" -> "+datos.abajo.getID()
				#while datos.atras!=None:
				#	body+=datos.getID()+" -> "+datos.atras.getID()+";"
				#	pass
				if datos2.sig==None:
					while datos2.abajo!=None:
						body+=datos2.getID()+" -> "+datos2.abajo.getID()+";"
						"""
						if datos2.abajo.tablaHash.noData()>0:
							body+="S"+datos2.abajo.getID()+datos2.abajo.tablaHash.graficar()+";\n"
							body+=datos2.abajo.getID()+"->"+"S"+datos2.abajo.getID()+"tabla ;"
							pass
						"""
						print datos2.getID()+" -> "+datos2.abajo.getID()+";"
						datos2=datos2.abajo
						pass
					#body+= datos2.abajo.getID()+" -> "+datos2.abajo.abajo.getID()+";"
					#datos3=datos2.abajo
					#while datos3.atras!=None:
					#	body+=datos3.getID()+" -> "+datos3.atras.getID()+" [style=dotted];"
					#	datos3=datos3.atras
					#	pass
					pass
				datos=datos.abajo 	
				pass
			titulos=titulos.sig
		titulos=self.first.abajo


		if titulos!=None and titulos.abajo==None:
			datos=titulos
			datos2=titulos.abajo
			while datos.sig!=None:
				body+=datos.getID()+" -> "+datos.sig.getID()+" [constraint=false];  \n"
				body+=datos.sig.getID()+" -> "+datos.getID()+" [constraint=false];  \n"
				print datos.getID()+" -> "+datos.sig.getID() 
				body+="{ rank=same "+ datos.getID()+" "+datos.sig.getID() + " } \n"
				body+="{ rank=same "+ datos.sig.getID()+" "+datos.getID() + " } \n"
				datos=datos.sig 	
				pass
			titulos=titulos.abajo
			pass
		elif titulos!=None:
			while titulos.abajo!=None:
				#body+=titulos.getID()+" -> "+titulos.abajo.getID()+" ; \n"
				datos=titulos
				datos2=titulos.abajo
				while datos.sig!=None:
					body+=datos.getID()+" -> "+datos.sig.getID()+" [constraint=false];  \n"
					body+=datos.sig.getID()+" -> "+datos.getID()+" [constraint=false];  \n"
					
					print datos.getID()+" -> "+datos.sig.getID() 
					body+="{ rank=same "+ datos.getID()+" "+datos.sig.getID() + " } \n"
					body+="{ rank=same "+ datos.sig.getID()+" "+datos.getID() + " } \n"
					
					"""
					if datos2.abajo==None:
						body+=datos2.getID()+" -> "+datos2.sig.getID()+" [constraint=false]; \n"
						print "***"+datos2.getID()+" -> "+datos2.sig.getID() 
						body+="{ rank=same "+ datos2.getID()+" "+datos2.sig.getID() + " } \n"
						pass
					"""
					datos=datos.sig 	
					pass
				titulos=titulos.abajo
			if titulos!=None:
				while titulos.sig!=None:
					body+=titulos.getID()+" -> "+titulos.sig.getID()+" [constraint=false]; \n"
					body+="{ rank=same "+ titulos.getID()+" "+titulos.sig.getID() + " } \n"
					body+=titulos.sig.getID()+" -> "+titulos.getID()+" [constraint=false]; \n"
					
					titulos=titulos.sig
					pass
				pass
		aux=self.first.sig
		while aux!=None:
			aux2=aux.abajo
			while aux2!=None:
				aux3=aux2
				while aux3.atras!=None:
					body+=aux3.getID()+" -> "+aux3.atras.getID()+" [style=dotted];"
					body+=aux3.atras.getID()+" -> "+aux3.getID()+" [style=dotted];"
					"""
					if aux3.atras.tablaHash.noData()>0:
						body+="S"+aux3.atras.getID()+aux3.atras.tablaHash.graficar()+";\n"
						body+=aux3.atras.getID()+"->"+"S"+aux3.atras.getID()+"tabla ;"
						pass
					"""
					aux3=aux3.atras
					pass
				aux2=aux2.abajo
				pass
			aux=aux.sig
			pass
		
		archivoDot +=body
		archivoDot +="\n }"
		try:
			arch=open("C:\graphviz-2.38\\release\EDD\\"+"ortogonal.dot","w")
			arch.write(archivoDot)
			arch.close()
			os.system('C:\graphviz-2.38\\release\\bin\dot.exe -Tpng C:\graphviz-2.38\\release\EDD\ortogonal.dot -o C:\graphviz-2.38\\release\EDD\ortogonal.png')
			pass
		except Exception as e:
			raise e

