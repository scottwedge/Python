def fib(n):
    a, b, lista = 0, 1, []
    while b < n:
        lista.append(b)
        a, b = b, a+b
    return lista


def multiplos(m, f):
    cont, lista = 0, []
    for i in range(f):
        cont+=1
	if cont % m == 0:
            lista.append(cont)
    return lista


def no_multiplos(m, f):
    cont, lista = 0, []
    for i in range(f):
        cont+=1
	if cont % m != 0:
            lista.append(cont)
    return lista


def n_primos(nn):
    lista = []
    for n in range(1,nn):
        for n2 in range(1,10):
            if n % n2 == 0 and n != n2 and n2 != 1:
                n+=1
                break
	    else:
		listas.append()
		

def bool_azar():
    import random
    co ,c1 = 1, 1
    while co == c1:
        azar = bin(random.randrange(1000))
	c1 = str(azar).count("1")
	c0 = str(azar).count("0")
	if c1 > c0:
            return True
	else:
            return False
        

def n_bool(rango):
    import random
    azar = random.randrange(rango)


def op_exp(r1, r2, op):
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
    if op == '+':
        total = r1 + r2
    elif op == '*':
        total = r1 * r2
    elif op == '-':
        total = r1 - r2
    elif op == '/':
        total = r1 / r2
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
        elif n3 == 12:
            total = str(total) + " T"
        elif n3 == 15:
            total = str(total) + " P"
        elif n3 == 18:
            total = str(total) + " E"
        elif n3 == 21:
            total = str(total) + " Z"
        elif n3 == 24:
            total = str(total) + " Y"
        return total


def abso(n):
    if n < 0:
        n*=-1


def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        total = 1
        for i in range(2, n+1):
            total*=i
        return total


