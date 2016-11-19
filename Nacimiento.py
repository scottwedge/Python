from datetime import date

def nacimiento(fecha):
	fecha = fecha.split("/")
	nacido = date(int(fecha[2]), int(fecha[1]), int(fecha[0]))
	hoy = date.today()
	edad = hoy - nacido
	print "Edad en dias: ", edad.days
	print "Edad en meses: ", edad.days / 30
	print "Edad en anos: ", edad.days / 365

try:
	fecha = raw_input("Introduzca su edad: ")
	nacimiento(fecha)
except Exception as e:
	print e
raw_input()