def replaced(nombre, char):
        for i in nombre:
                if i.isalnum() == True:
                        nombre.replace(i, 'a')

def user_valid():
        while True:
                name = raw_input("Ingrese su nombre de usuario: ")
                nombre = name
                if nombre.isalnum() == True:
                        print "El nombre debe contener al menos un caracter no alfanumerico, pero no espacios"
                        replaced(nombre, '0')
                elif nombre.isdigit() == True:
                        print "El nombre debe contener al menos un caracter alfabetico"
                        replaced(nombre, 'a')
                elif nombre.isalpha() == True:
                        print "El nombre debe contener al menor un caracter numerico"
                elif len(name) < 10:
                        print "El nombre no puede contener menos de 10 caracteres"
                elif len(name) > 20:
                        print "El nombre no puede contener mas de 20 caracteres"
                else:
                        return name

print user()
