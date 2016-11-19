def dividir(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print "¡Division por cero!"
    else:
        print "El resultado es ", result
    finally:
        print "La division fue finalizada con exito"

dividir(2, 1)
dividir(2, 0)
