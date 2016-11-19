def tablas2():
	n = int(input("Ingrese tabla a mostrar:"))
	print("Tabla del",n)
	for n2 in range(1,1000001):
		print (n,"x",n2,"=",n*n2)

tablas2()
