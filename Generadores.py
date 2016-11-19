def reversa(datos):
    for indice in range(-1, -1, -1):
        yield datos[indice]

for letra in reversa('golf'):
    print letra
