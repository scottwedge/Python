import serial

cont = 0

def attempt():
    while cont < 11:
        try:
            com = "COM" + str(cont)
            Arduino = serial.Serial("COM4", 9600, timeout = 1)
            print "Conectado al puerto ", com
            break
        except serial.SerialException as e:
            print e
            cont += 1
    else:
        print "Puerto no encontrado"
        raw_input("Pulse ENTER para continuar")
