import getpass

def password():
    try:
        passw=getpass.getpass("Ingrese contra: ")
        print "Contra", passw
    except Exception as e:
        print e
    raw_input()

password()
