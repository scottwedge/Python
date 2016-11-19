# -*- encoding: utf-8 -*-

from random import randrange

def acierto_game(rango):
	azar = randrange(rango)
	user = 0
	while user < 1 or user > 100:
		try:
			user = input("Ingrese un numero del 1 al " + str(rango) + ": ")
		except (TypeError, ValueError):
			print "Ha ingresado un valor incorrecto"
		except KeyboardInterrupt:
			print "Saliendo..."
		except:
			print "Ha ocurrido un error inesperado"
	if azar == user:
		"Felicitaciones, acerto al numero"
	else:
		print "No acerto al numero"
		print "El numero era", azar
		print "La diferencia es de %s" % (abs(azar - user))
	return abs(azar - user)


def main():
	while True:
		while True:
			try:
				rango = input("Introduzca un numero: ")
				break
			except (TypeError, ValueError):
				print "Ha ingresado un valor incorrecto"
			except KeyboardInterrupt:
				print "Saliendo..."
			except:
				print "Ha ocurrido un error inesperado"
		print "Jugador 1"
		jug1_puntos = acierto_game(rango)
		print "Jugador 2"
		jug2_puntos = acierto_game(rango)
		if jug1_puntos < jug2_puntos:
			print "Gano el jugador 1"
		elif jug1_puntos > jug2_puntos:
			print "Gano el jugador 2"
		else:
			print "Empataron"

if __name__ == '__main__':
	main()