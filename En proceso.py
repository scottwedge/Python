Python 3.4.1 (v3.4.1:c0e311e010fc, May 18 2014, 10:38:22) [MSC v.1600 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def div_primos():
	n = int(input("Ingrese numero"))
	while n > 1:
		for n2 in range(1,n):
			for n3 in range(1,10):
				if n2 % n3 == 0 and n2 != n3 and n3 != 1:
					break
			else:
				print (n2)
				n = n // n2
				break
