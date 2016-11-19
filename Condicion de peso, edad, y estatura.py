def masa_corporal():
	est = float(input("Ingrese estatura"))
	peso = float(input("Ingrese peso"))
	edad = float(input("Ingrese edad"))
	masa = peso / (est * est)
	if edad < 45:
		if masa < 22:
			return "Condicion de riesgo:Baja"
		else:
			return "Condicion riesgo:Media"
	else:
		if masa >= 22:
			return "Condicion de riesgo:Media"
		else:
			return "Condicion de riesgo:Alta"

masa_corporal()
