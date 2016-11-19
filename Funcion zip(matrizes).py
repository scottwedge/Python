mat = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    ]

print [[fila[i] for fila in mat] for i in [012]]

for i in [0, 1, 2]:
    for fila in mat:
        print fila[i]
    print

zip(*mat)
