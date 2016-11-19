def vumetrob():
	import os
	m = 1
	while m > 0:
		os.system('clrscr')
		m = int(input("Ingrese volumen:"))
		vumetro(m)

vumetrob()
