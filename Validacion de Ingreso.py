def contrasena():
	contra = input("Ingrese una contraseña segura\n")
	contra2 = contra.isalnum()
	if contra2 == 1:
		print ("La contraseña elegida no es segura,debe contener al menos un caracter no alfanumérico y no debe contener espacio\n")
		contrasena()
	else:
		contra3 = len(contra)
		if contra3 < 8:
			print ("La contraseña elegida no es segura,debe contener un minimo de 8 caracteres")
			contrasena()
		else:
			contra2 = contra.islower()
			if contra2 == 1:
				print ("La contraseña elegida no es segura,debe contener por lo menos un caracter en mayuscula\n")
				contrasena()
			else:
				contra2 = contra.isupper()
				if contra2 == 1:
					print ("La contraseña elegida no es segura,debe contener por lo menos un caracter en minuscula\n")
					contrasena()
				else:
					return "True"

contrasena()

def nombre_usuario():
	nombre = input("Ingrese un nombre de usuario valido\n")
	nombre2 = nombre.isalnum()
	if nombre2 == 0:
		print ("El nombre de usuario puede contener solo letras y números")
		contrasena()
	else:
		nombre2 = len(nombre)
		if nombre2 < 6:
			print ("El nombre de usuario debe contener al menos 6 caracteres")
			contrasena()
		elif nombre2 > 12:
			print ("El nombre de usuario no puede contener más de 12 caracteres")
		else:
			contrasena()

nombre_usuario()
