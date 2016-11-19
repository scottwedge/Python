def triangulo():
	a = int(input("Lado 1:"))
	b = int(input("Lado 2:"))
	c = int(input("Lado 3:"))
	if a + b < c or a + c < b or b + c > a:
		return "No es un triangulo valido"
	else:
		if a != b and a != c and b != c:
			return "Es un triangulo escaleno"
		else:
			return "Es un triangulo isosceles"

triangulo()
