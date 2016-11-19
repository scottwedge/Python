def dib_rec(a, h):
	n = 0
	while n < h:
		print ('*'*a)
		n+=1

dib_rec(3, 4)

def dib_tri(h):
	n = 0
	a = 1
	while n < h:
		print ('*'*a)
		n+=1
		a+=1

dib_tri(4)

def dib_hexa(h):
	n = 0
	a = h
	b = a - 1
	while n < ((h*2)-1):
		print (" "*b,'*'*a)
		n+=1
		if n < 4:
			a+=2
			b-=1
		else:
			a-=2
			b+=1

dib_hexa(4)
