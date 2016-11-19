# Jodete : juego de cartas

from time import sleep

copa = []
espada = []
basto = []
oro = []
pozot = []
diez = []
podos = False


def que_tirar(palo):
    if (podos is False) and ('2' in palo):
        return '2'
    elif '4' in palo:
        return '4'
    elif '12' in palo:
        return '12'
    else:
        return palo[0]


def agregar(a):
    if a[0] == '10':
        diez.append(a)
    elif a[1] == 'c':
        copa.append(a[0])
    elif a[1] == 'e':
        espada.append(a[0])
    elif a[1] == 'o':
        oro.append(a[0])
    elif a[1] == 'b':
        basto.append(a[0])
    return copa, espada, oro, basto, diez


def correcto(lista):
    try:
        if (lista[0].isdigit()) and ((0 < lista[0]) or (lista[0] < 13)) and (lista[1] in ['c', 'e', 'o', 'b']):
            return True
        else:
            return False
    except:
        print "Carta ingresada incorrecta"


def tiro(num, palo):
    try:
        palo.pop(palo.index(num))
        return True, palo
    except ValueError:
        print "Carta ingresada no se encuentra en la mano"
        return False, palo


def printer():
    print "Ingrese el numero seguido de:"
    print "c para copa"
    print "e para espada"
    print "o para oro"
    print "b para basto"


def jodete():
    print "Configuracion"
    while True:
        try:
            mode = input("Ingrese cantidad de mazos: ")
            break
        except:
            print "Valor ingresado no representa un numero"
    printer()
    i = 0
    while i < 7:
        i += 1
        ing = raw_input("Ingrese cartas en mano: ")
        if ing.isalnum() == False:
            ing = ing.split(" ")
        retorno = correcto(ing)
        if retorno == True:
            copa, espada, oro, basto, diez = agregar(ing)
        else:
            print "Carta ingresada incorrecta"
            i -= 1
    print "Saliendo de configuracion..."
    sleep(1)
    while True:
        while True:
            pozo = raw_input("Ingrese carta en pozo: ")
            if pozo.isalnum() == False:
                response = correcto(pozo.split(" "))
            else:
                response = correcto(pozo)
            if response == True:
                break
            else:
                print "Carta ingresada incorrecta"
        pozot.append(pozo)
        if pozo.isalnum() == False:
            pozo = pozo.split(" ")
        saque = raw_input("Ingrese la carta que saco: ")
        copa, espada, oro, basto, diez = agregar(saque)
        if (pozo[1] == 'c') and (len(copa) > 0):
            aux = que_tirar(copa)
            print "Tirar: ", aux + ' de copa'
            copa.remove(aux)
        elif (pozo[1] == 'e') and len(espada):
            aux = que_tirar(espada)
            print "Tirar: ", aux + ' de espada'
            espada.remove(aux)
        elif (pozo[1] == 'b') and (len(basto) > 0):
            aux = que_tirar(basto)
            print "Tirar: ", aux + ' de basto'
            basto.remove(aux)
        elif (pozo[1] == 'o') and (len(oro) > 0):
            if '7' in oro:
                print "Tirar: 7 de oro"
            else:
                aux = que_tirar(oro)
                print "Tirar: ", aux + ' de oro'
                oro.remove(aux)
        elif pozo[0] in copa:
            print "Tirar: ", pozo[0] + ' de copa'
            copa.remove(pozo[0])
        elif pozo[0] in espada:
            print "Tirar: ", pozo[0] + ' de espada'
            espada.remove(pozo[0])
        elif pozo[0] in basto:
            print "Tirar: ", pozo[0] + ' de basto'
            basto.remove(pozo[0])
        elif pozo[0] in oro:
            print "Tirar: ", pozo[0] + ' de oro'
            oro.remove(pozo[0])
        elif len(diez) > 0:
            print "Tirar: ", diez[0]
            diez.pop(0)
        while True:
            response = raw_input("Correcto: ")
            response = response.upper()
            if response == 'SI':
                copa.pop(0)
                print "Carta descartada"
            elif response == 'NO':
                while True:
                    response = raw_input("Que carta tirar: ")
                    if response.isalnum() == False:
                        response = response.split(" ")
                    retorno = correcto(response)
                    if retorno == True:
                        if response[1] == 'c':
                            aux, copa = tiro(response[0], copa)
                        elif response[1] == 'e':
                            aux, espada = tiro(response[0], espada)
                        elif response[1] == 'b':
                            aux, basto = tiro(response[0], basto)
                        elif response[1] == 'o':
                            aux, oro = tiro(response[0], oro)
                        if aux == True:
                            print "Carta descartada"
                            break
                        else:
                            continue
                    else:
                        print "Carta ingresada incorrecta"
                        continue
            else:
                print "Comando Incomprendido, Utilize Si o No"
                continue
            break

jodete()
