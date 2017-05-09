from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from matDispersa import MatrizDispersa
from ListaDoble import ListaDoble
from serializers import LoginSerializer
from listaSimple import ListaSimple
import json

md=MatrizDispersa()
ld=ListaDoble()
ls=ListaSimple()

def helloWorld(self):
		html= "<html><body>Hola Mundo desde DJANGO</body></html>"
		try:
			md.imprimir()
			pass
		except Exception as e:
			raise e
		return HttpResponse(html)

def pruebaJSON(self):
		json="[{\"usuario\":\"user\",\"password\":\"11\",\"year\":\"2015\",\"month\":\"12\",\"dia\":\"14\",\"evento\":\"Primer JSON\",\"direccion\":\"Guatemala\",\"descripcion\":\"Creando peticiones\",\"hora\":\"12:30\"}]" 
		md.insertar("928","Enero","23","Tarea EDD","Guatemala","15:00","Entrega de Tarea")
		md.insertar("928","Septiembre","3","Practica Compi1","Guatemala","17:00","Entrega")
		try:
			md.generarMatriz()
			md.imprimir()
			pass
		except Exception as e:
			
			raise e
		
		return HttpResponse(json)

@csrf_exempt
def eventosPorAnio(self):
		try:
			resp=md.obtenerEventosYear("1900")
			pass
		except Exception as e:
			resp="NO SE PUDO COMPLETAR"
			#raise e
		return HttpResponse(resp)

@csrf_exempt
def eventosPorDia(self):
		try:
			resp=md.obtenerEventosDia("04")	
			pass
		except Exception as e:
			resp="NO SE PUDO COMPLETAR"
			#raise e
		return HttpResponse(resp)

@csrf_exempt
def eventosPorMes(request):
		if request.method=='POST':
			mes=request.POST['mes']
			pass
		try:
			resp=md.obtenerEventosMes("Junio")	
			pass
		except Exception as e:
			resp=""
			#raise e	
		return HttpResponse(resp)

@csrf_exempt
def login(request):

	if request.method=='POST':
		data=json.loads(request.body.decode("utf-8"))
		#dat=request.raw_post_data
		print "---------------------------"
		us=data['usuario']
		pas=data['password']
		print us+" "+pas
		try:
			resp=ld.loginUsuario(us,pas)
			print "La respuesta es: "+str(resp)
			if resp==True:
				ls.insertar("Login Usuario")
				return HttpResponse("True")	
				pass
			else:
				ls.insertar("Intento Login")
				return HttpResponse("False")
			pass
		except Exception as e:
			return HttpResponse("False")
		pass

@csrf_exempt
def eventosG(request):
	if request.method=='POST':
		data=json.loads(request.body.decode("utf-8"))
		i=data['var']
		us=data['usuario']
		y=data['year']
		m=data['mes']
		d=data['dia']
		try:
			print y+ " "+" "+m+" "+d
			if i=="0":
				resp=ld.buscar(us).obtenerEventosDia(y,m,d)
				return HttpResponse(resp)	
				pass
			elif i=="1":
				resp=ld.buscar(us).obtenerEventosMes(m)
				return HttpResponse(resp)
			elif i=="2":
				resp=ld.buscar(us).obtenerEventosYear(y)
				return HttpResponse(resp)
			pass
		except Exception as e:
			return HttpResponse("{}")
		pass

@csrf_exempt
def modificarEliminar(request):
	print "ModificarEliminar"
	try:
		if request.method=='POST':
			data=json.loads(request.body.decode("utf-8"))
			#dat=request.raw_post_data
			decis=data['decision']
			us=data['usuario']
			year=data['year']
			m=data['mes']
			d=data['dia']
			name=data['evento']
			direc=data['direccion']
			h=data['hour']
			desc=data['descripcion']
			yE=data['yearE']
			mE=data['mesE']
			dE=data['diaE']
			eE=data['nombreevento']

			print decis
			print dE+" "+mE+" "+yE+" "+eE
			print "MOD: "+year+" "+mE+" "+dE+" "+name+" "+direc+" "+h+" "+desc
					
			try:
				if decis=="0":
					ld.buscar2(us).eliminar(d,m,year,name)
					ld.buscar2(us).insertar(year,mE,dE,name,direc,h,desc)

					ls.grafica_Bitacora_Calendar()

					ld.buscar2(us).generarMatriz()
					print "EVENTO MODIFICADO"
					ls.insertar("EVENTO MODIFICADO "+name)
					return HttpResponse("Realizado")
					pass
				else:
					ld.buscar2(us).eliminar(d,m,year,name)
					ld.buscar2(us).generarMatriz()
					ld.buscar2(us).imprimir()
					print "EVENTO ELIMINADO"
					ls.insertar("EVENTO ELIMINADO "+name)
					return HttpResponse("Eliminado")

					pass
				pass
			except Exception as e:
				print e
				return HttpResponse("Fallido")
			pass
		pass
	except Exception as e:
		print e
		HttpResponse("Fallido")	




@csrf_exempt
def crearE(request):
	try:
		if request.method=='POST':
			data=json.loads(request.body.decode("utf-8"))
			#dat=request.raw_post_data
			us=data['usuario']
			year=data['year']
			m=data['mes']
			d=data['dia']
			name=data['evento']
			direc=data['direccion']
			h=data['hour']
			desc=data['descripcion']


			try:
				print data
				ld.buscar2(us).insertar(year,m,d,name,direc,h,desc)
				ld.buscar2(us).generarMatriz()
				ls.insertar("Crear Evento "+name)
				ls.grafica_Bitacora_Calendar()
				return HttpResponse("Ingresado")
				pass
			except Exception as e:
				print e
				ls.insertar("Intento Crear Evento")
				return HttpResponse("No Creado")
			pass
		pass
	except Exception as e:
		return HttpResponse("No Creado")
	

@csrf_exempt
def registrar(request):
	try:
		if request.method=='POST':
			data=json.loads(request.body.decode("utf-8"))
			#dat=request.raw_post_data
			us=data['usuario']
			pas=data['password']
			try:
				resp=ld.insertar(us,pas)
				ld.grafica_Users_Calendar()
				ls.insertar("REGISTRO "+us)
				return HttpResponse(resp)
				pass
			except Exception as e:
				resp="No se completo el registro"
				print resp
				return HttpResponse(resp)
			pass
		pass
	except Exception as e:
		raise e
	