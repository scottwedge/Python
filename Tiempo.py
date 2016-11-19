def tiempo():
	from time import sleep
	seg = 0
	minute = 0
	hora = 0
	dia = 0
	while True:
		seg+=1
		if seg == 60:
			minute+=1
			seg = 1
		if minute == 60:
			hora+=1
			minute = 1
		if hora == 24:
			hora = 0
		print hora, ":", minute, ":", seg
		sleep(1)

tiempo()
