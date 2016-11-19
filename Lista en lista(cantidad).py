lista = ['a', 'a', ['2', '3'], ['1', '8'], ['3', '2'], '9', 'p']

def lentotal():
    cont = 0
    for i in range(len(lista)):
        try:
            n = len(lista[i])
            cont += n
        except TypeError:
            cont += 1
    return cont

print lentotal()
