from maindic import dic

def fragmentos(busq, string):
    for i in range(len(string) - len(busq) + 1):
        if busq == string[i:len(busq)+i]:
            return True
    return False

def search_dic(string):
    lista = []
    string = string.upper().split()
    for word in string:
        for key in dic.keys():
            for pal in dic.get(key):
                if len(word) > len(pal):
                    retorno = fragmentos(pal, word)
                elif len(pal) > len(word):
                    retorno = fragmentos(word, pal)
                else:
                    if word == pal:
                        retorno = True
                if retorno == True:
                    if key not in lista:
                        print word, pal
                        lista.append(key)
    return lista

print search_dic("Buscar informacion en google")
