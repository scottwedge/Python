f = open('C:\Users\Alumno\Desktop\f.txt')
f.write('Hola mundo')
# '5'
f.seek(5) # Va al sexto byte del archivo
f.read(1)
# 'd'
f.seek(-3, 2) # Va al tercer byte antes del final
f.read(1)

f.close()
f.closed()
# True
