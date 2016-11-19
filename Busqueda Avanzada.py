# Realizar busqueda de comando en un comando introducido por teclado

dic = {
"Afirmacion": ["SI", "AFIRMATIVO", "CORRECTO"],
"Negacion": ["NO", "NEGATIVO", "INCORRECTO"],
"Nombre": [],
"Usuarios": [],
"Busqueda": ["BUSCAR", "BUSCA", "BUSQUEDA", "ENCONTRAR", "ENCONTRA",
"ENCUENTRO"],
"Abrir": ["ABRIR", "ABRI", "ABRE", "ABERTURA", "APERTURA"],
"Cerrar": ["CERRAR", "CIERRE", "CERRA", "CERRADO"]
}

def busq_av():
    frase = raw_input("Hola, Soy Talker, digame que puedo hacer por usted\n")
    frase = frase.upper().split(" ")
    for palabra in frase:
            for key in dic.keys():
                if palabra in dic.get(key):
                    return key

print busq_av()
