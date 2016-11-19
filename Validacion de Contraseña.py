from maindic import dic

def pass_valid(contra):
        while True:
                punto = 0
                if contra.isalnum() == False:
                        punto += 1
                if contra.isdigit() == False:
                        punto += 1
                if contra.isalpha() == False:
                        punto += 1
                if punto == 1:
                        print "El nivel de seguridad es bajo"
                elif punto == 2:
                        print "El nivel de seguridad es medio"
                elif punto == 3:
                        print "El nivel de seguridad es alto"
                bucle = 0
                while bucle == 0:
                        response = raw_input("Continuar: ")
                        response = response.upper()
                        if response in dic.get("Afirmacion"):
                                break
                        elif response in dic.get("Negacion"):
                                
                                bucle = 1
                        else:
                                print "Comando no comprendido, intente con si o no"
                else:
                        continue
                break

contra = raw_input("Ingrese su contrasena: ")
pass_valid(contra)
