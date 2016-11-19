def difdias():
	f1 = raw_input("Introduzca la primera fecha(con '/')")
	f2 = raw_input("Introduzca la segunda fecha(con '/')")
	f1 = f1.split("/")
	f2 = f2.split("/")
	m = ((((int(f1[1])-int(f2[1]))*30)+int(f1[0]))-int(f2[0]))
	print (m)

difdias()
