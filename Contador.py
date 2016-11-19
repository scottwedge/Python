def contador():
	import msvcrt
	n=0
	while (True):
		if msvcrt.kbhit():
			c = msvcrt.getch()
			if c != 'x':
				n+=1
				c=''
				print n
			else:
				break;

contador()
