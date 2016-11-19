caballeros = {'gallahad': 'el puro', 'robin': 'el valiente'}
for k, v in caballeros.iteritems():
    print k, v

# Devuelve:
# gallahad el puro
# robin el valiente

for i, v in enumerate(['ta', 'te', 'ti']):
    print i, v

# Devuelve:
# 0 ta
# 1 te
# 2 ti

preguntas = ['nombre', 'objetivo', 'color favorito']
respuestas = ['Lancelot', 'El santo grial', 'azul']
for p, r in zip(preguntas, respuestas):
    print 'Cual es tu {0}? {1}.'.format(p, r)

# Devuelve:
# Cual es tu nombre? Lancelot.
# Cual es tu objetivo? El santo grial.
# Cual es tu color favorito azul.

for i in reversed(range(1,10,2)):
    print i

# Devuelve:
# 9
# 7
# 5
# 3
# 1

canasta = ['manzana', 'naranja', 'manzana', 'pera', 'naranja', 'banana']
for f in sorted(set(canasta)):
    print f

# Devuelve:
# banana
# naranja
# manzana
# pera
