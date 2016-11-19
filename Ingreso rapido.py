from msvcrt import kbhit, getch

cartas = []
n = 0
palo = ""

def ingreso_rapido():
    print "Ingrese el numero de la carta: "
    cr = 0
    while True:
        if kbhit():
            n = getch()
            if (n.isdigit() == False) or (int(n) < 1) or (int(n) > 12):
                print "Numero ingresado incorrecto"
            else:
                n2 = int(n)
                if (cr == 0) and (n2 == 1):
                    tt = n2
                    cr = 1
                elif (cr == 1) and (n2 == 1):
                    n2 += tt
                    break
                else:
                    break
                n = str(n2)
    print "Ingrese el palo de la carta: "
    while True:
        if kbhit():
            palo = getch()
            if palo not in ['c', 'o', 'e', 'b']:
                print "Palo ingresado incorrecto"
            else:
                break
    return n+palo

print ingreso_rapido()
raw_input()
