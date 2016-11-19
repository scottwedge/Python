def loro(tension, estado='rostizado', accion='explotar'):
	print "-- Este loro no va a", accion,
	print "si le aplicas", tension, "voltios."
	print "Esta", estado, "!"

d = {"tension": "cuatro millones", "estado": "demacrado", "accion": "VOLAR"}

loro(**d)
