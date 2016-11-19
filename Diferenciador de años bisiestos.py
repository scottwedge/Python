def bisiestos(año):
	if (año % 4) == 0:
		if año < 1582:
			return "Es bisiesto"
		elif (año % 400) == 0:
			return "Es bisiesto"
		elif (año % 100) == 0:
			return "No es bisiesto"
		else:
			return "Es bisiesto"
	else:
		"No es bisiesto"

bisiestos(2014)
