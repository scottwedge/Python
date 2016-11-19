def es_palindromo(string):
	string2 = string[::-1]
	if string == string2:
		return "True"
	else:
		return "False"

es_palindromo(radar)
