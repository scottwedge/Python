sum(i*i for i in range(10)) # Suma de cuadrados

xvec = [10, 20, 30]
yvec = [7, 5, 3]
sum(x*y for x, y in zip(xvec, yvec)) # Producto escalar

from math import pi, sin
tabla_de_senos = dict((x, sin(x*pi/180)) for x in range(0, 91))

palabras_unicas = set(word for line in page for word in line.split())

mejor_promedio = max(()alumno.promedio, alumno.nombre) for alumno in graduados)

data = 'golf'
list(data[i] for i in range(len(data)-1,-1,-1))
