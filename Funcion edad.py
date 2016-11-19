def anos():
	años = input("Ingrese fecha de nacimiento\n")
	años = años.split("/")
	edad = 2014 - int(años[2])
	print ("Usted tiene ",edad," años")

anos()
