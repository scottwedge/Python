def oraciones_palindromas():
	orac2 = ""
	orac = input("Ingrese una oracion:\n")
	orac = orac.split(" ")
	for n in range(len(orac)):
		orac2 = orac2 + orac[n]
	if orac2 == orac2[::-1]:
		return "Es palindromo"
	else:
		return "No es palindromo"

oraciones_palindromas()
