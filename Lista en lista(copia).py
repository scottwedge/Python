lista = ['a', 'a', ['2', '3'], ['1', '8'], ['3', '2'], '9', 'p']
lista2 = []

def copiatotal():
    for i in range(len(lista)):
        try:
            len(lista[i])
            for i2 in lista[i]:
                lista2.append(i2)
        except TypeError:
            lista2.append(lista[i])
    return lista2

print lentotal()
