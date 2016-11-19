def contador_de_codigo():
    cont = 0
    largo = []
    corto = []
    simbolos = raw_input("Ingrese simbolo(s) de comentario(s) separados por coma: ")
    simbolos = simbolos.split(",")
    for i in simbolos:
        if len(i) > 1:
            largo.append(i)
        else:
            corto.append(i) 
    address = raw_input("Ingrese direccion y nombre del archivo separados por '\': ")
    with open(address) as code:
        for line in code:
            line = line[0:(len(line)-1)]
            for l in line:
                if (l.isalnum() is False) and (l not in ['(', ')', '{', '}', '[', ']', '/', '#', '"']):
                    continue
                elif l in corto:
                    break
                for i in largo:
                    if i[0] == l:
                        for i in i:
                            if i != line[l.index()+cont]:
                                break
                            cont += 1
                        else:
                            break
                else:
                    break
                        
