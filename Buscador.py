lista = []

def buscador():
    print "Ingrese A para agregar a la lista"
    print "Ingrese B para buscar a la lista" 
    op = raw_input("Ingrese una opcion: ")
    listas =  open('C:\Users\Alumno\Desktop\Lista.txt', 'r+')
    obj = raw_input("Ingrese un objeto a agregar: ")
    obj = obj.upper()
    if op in ['A', 'a']:
        listas.write(obj)
        listas.write('\n')
    elif op in ['B', 'b']:
        for line in listas:
            for i in range(len(line)-len(obj)+1):
                if line[0+i:len(obj)+i] == obj:
                    lista.append(line[0:(len(line)-1)]
    listas.close()
    return lista


while True:
    print buscador()
