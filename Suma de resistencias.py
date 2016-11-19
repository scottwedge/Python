def suma_resis():
    n2 = 0
    r1 = raw_input("Ingrese valor de la primera resistencia(Ej: 10 k): ")
    r2 = raw_input("Ingrese valor de la segunda resistencia(Ej: 10 k): ")
    for n2 in range(2):
        if n2 == 0:
            Ir = r1
        elif n2 == 1:
            r1 = Ir2
            Ir = r2
        Ir = Ir.split(" ")
        if Ir[1] == 'k':
            Ir2 = int(Ir[0])*1000
        elif Ir[1] == 'M':
            Ir2 = int(Ir[0])*1000000
        elif Ir[1] == 'G':
            Ir2 = int(Ir[0])*1000000000
        else:
            Ir2 = int(Ir[0])
    r2 = Ir2
    total = r1 + r2
    n3 = 0
    while total > 10:
        total/=10
        n3+=1
    while n3 % 3 != 0:
        total*=10
        n3-=1
        if n3 == 3:
            total = str(total) + " k"
        elif n3 == 6:
            total = str(total) + " M"
        elif n3 == 9:
            total = str(total) + " G"
        return total

suma_resis()
