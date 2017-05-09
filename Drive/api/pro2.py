from matDispersa import MatrizDispersa
from Hash import Hash
from ListaDoble import ListaDoble
md=MatrizDispersa()
h=Hash()
#admin
#pass: admin123
"""
md.insertar("4500","Noviembre","3")
md.insertar("4500","Noviembre","25")
md.insertar("3220","Junio","10")
md.insertar("5000","Septiembre","9")
"""
"""
md.insertar("928","Abril","5")
md.insertar("2020","Junio","1")
#md.insertar("2020","Abril","7")
"""
"""

md.insertar("2010","Junio","2")
md.insertar("2016","Abril","20")
#md.insertar("2020","Mayo","31")

md.insertar("2017","Marzo","14")
md.insertar("2017","Marzo","4")
md.insertar("2017","Marzo","24")
md.insertar("2017","Marzo","15")

md.insertar("2010","Marzo","8")
md.insertar("2020","Abril","20")
"""
#md.insertar("2020","Marzo","9","Evento")

#md.insertar("2020","Junio","1","Estudiar")
#md.insertar("2020","Junio","27","Leer")
#md.insertar("2020","Junio","12","Corto2")

#md.insertar("1900","Abril","01","Corto Fisica2")

md.insertar("2020","Enero","23","Tarea EDD","Guatemala","15:00","Entrega de Tarea")

md.insertar("2020","Septiembre","3","Practica Compi1","Guatemala","17:00","Entrega")
md.insertar("2020","Agosto","31","Leer Circuitos","Guatemala","11:00","Circuitos RC")

md.insertar("2010","Abril","29","First event","Xela","11:00","Escalar Volcan")

md.insertar("2011","Junio","04","Second Event","Tecpan","09:00","Centro Turistico")
md.insertar("2011","Junio","04","Third Event","Tecpan","09:00","Centro Turistico")
md.insertar("2011","Junio","04","Four Event","Tecpan","09:00","Centro Turistico")


#print (md.obtenerEventosDia("2011","Junio","04"))
print (md.obtenerEventosYear("2011"))
#print (md.obtenerEventosMes("Mayo"))
md.Grafica_Hash_Dia_Especifico("2011","Junio","04")
"""
md.insertar("2012","Marzo","03","Cuarto")
md.insertar("2010","Marzo","26","Quinto")
md.insertar("2016","Marzo","03","Septimo")
md.insertar("2016","Marzo","31","Sexto")
md.insertar("2016","Marzo","31","Probando Eventos")
md.insertar("2016","Marzo","31","Eventos MD")



md.insertar("2011","Junio","04","Nuevo Evento")
md.insertar("2010","Abril","29","Event Event")
#md.insertar("2010","Abril","29","Last Event")
md.insertar("2010","Abril","1","Testing")
"""
md.eliminar("31","Marzo","2016","Sexto")
md.Grafica_Hash_Dia_Especifico("2016","Marzo","31")
#md.Grafica_Hash_Dia_Especifico("2020","Junio","1")
"""
md.eliminar("14","Marzo","2017")

md.eliminar("04","Junio","2011")
"""
md.generarMatriz()
md.imprimir()
"""
h.insertar("HelloWorld")
h.insertar("nuevo")
h.insertar("3r DATOO")
h.insertar("FuncionREHASH")
h.insertar("5taPOS")
h.insertar("REHASH FUNCIONANDO")
print "_--------------------------------------"
h.buscar("REHASH FUNCIONANDO")
print "----------------------------"
h.imprimir()
"""
"""
ld=ListaDoble()
"""

ld=ListaDoble()
ld.insertar("Juan","123412")
ld.insertar(" Pedro Juarez ","233232")
ld.insertar("Jose Luis","121211")
ld.grafica_Users_Calendar()
#ld.extraerMD(0).insertar("2010","Abril","1","Testing")
#ld.extraerMD(0).insertar("2010","Abril","25","Second")
#ld.extraerMD(0).generarMatriz()


ld.buscar2("Pedro Juarez").insertar("2011","Junio","01","First Event","Tecpan","09:00","Centro Turistico")
ld.buscar2("Pedro Juarez").insertar("2011","Junio","02","Second Event","Tecpan","09:00","Centro Turistico")
ld.buscar2("Pedro Juarez").insertar("2011","Mayo","03","Third Event","Tecpan","09:00","Centro Turistico")
ld.buscar2("Pedro Juarez").insertar("2011","Junio","04","Four Event","Tecpan","09:00","Centro Turistico")
#ld.buscar2("Pedro Juarez").generarMatriz()
ld.buscar2("Pedro Juarez").eliminar("04","Junio","2011","Four Event")
ld.buscar2("Pedro Juarez").eliminar("01","Junio","2011","First Event")
#ld.buscar2("Pedro Juarez").eliminar("03","Mayo","2011","Third Event")


ld.buscar2("Pedro Juarez").generarMatriz()
ld.buscar2("Pedro Juarez").Grafica_Hash_Dia_Especifico("2011","Junio","04")
ld.imprimir()
