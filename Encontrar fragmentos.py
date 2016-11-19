from maindic import dic

def fragmentos(busq, string):
    for i in range(len(string) - len(busq) + 1):
        if busq == string[i:len(busq)+i]:
            return True
    return False

print fragmentos('tor', 'Aitor')
