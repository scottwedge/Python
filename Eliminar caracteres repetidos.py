def borrar_repeat(string):
    while True:
        for i in range(len(string)):
            if string[i] == string[i-1]:
                string = string.replace(string[i]*2, string[i])
                break
        else:
            break
    return string

print borrar_repeat("Buscar programacioooon avanzada en C++ para Windows")
