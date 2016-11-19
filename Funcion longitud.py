def longitud(string):
	n2 = 0
	string2 = ""
	string3 = "5"
	while string3 != string2:
		n2+=1
		string3 = string2
		string2 = string[:n2]
	n2-=1
	return n2

longitud("Hola")
