def ing_num():
	while(True):
		try:
			n = raw_input("Por favor, ingrese un numero: ")
			if not n.isdigit():
				raise NameError
		except NameError:
			print ("No ha ingresado un numero")
		except KeyboardInterrupt:
			print ("Por favor no interrumpa la secuencia")
		else:
			print ("Secuencia terminada")
			break

ing_num()
