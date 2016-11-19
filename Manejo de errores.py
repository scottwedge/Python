while True:
	try:
		x = int(raw_input("Por favor ingrese un número: "))
		break
	except ValueError:
		print "No era valido, intetnte nuevamente..."
	except IOError as (errno, strerror):
                print "Error E/S ({0}): {1}".format(errno, strerror)

