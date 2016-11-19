def contador_de_lineas():
    cont = raw_input("Ingrese archivo con direccion incluida: ")
    count = 0
    with open(cont) as code:
        for line in code:
            line = line[0:(len(line)-1)]
            for i in line:
                if (i.isalnum() is False) and (i not in ['(', '/', '#', '"']):
                    continue
                elif i == '#':
                    break
                elif i == '"':
                    if (line[i+1] + line[i+2]) == '""':
                        pass
                    else:
                        count += 1
                    break
                else:
                    count += 1
                    break
    print "Cantidad de lineas: ", count
    raw_input()

contador_de_lineas()
