def time_equi():
	while True:
		try:
			time = input("Ingrese la cantidad de horas: ")
			if time/24 == 1:
				print time/24, "dia"
			else:
				print time/24, "dias"
			if time%24 > 0:
				time = time-(time/24)
				if time/60 == 1:
					print time/60, "minuto"
				else:
					print time/60, "minutos"
				if time%60 > 0:
					time = time-(time/60)
					if time/60 == 1:
						print time/60, "segundo"
					else:
						print time/60, "segundos"
				else:
					print 0, "minutos"
			else:
				print 0, "minutos"
				print 0, "horas"
		except (NameError, SyntaxError, TypeError):
			print "El valor ingresado no es correcto"

time_equi()
