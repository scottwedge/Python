def tecla():
	import msvcrt
	ch = 0
	while ch != 'x':
		if msvcrt.kbhit():
			ch = msvcrt.getch()
			print ch

tecla()
