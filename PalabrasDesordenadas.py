#!/usr/bin/env python
# -*- encoding:utf-8 -*-

from string import join
    
def function(string):
    lista = string.split(" ")
    newList = []
    for i in range(len(lista)):
        auxList = []
        auxList.append(lista[i][0])
        for i2 in range(len(lista[i])-2,0,-1):
            auxList.append(lista[i][i2])
        auxList.append(lista[i][-1])
        newList.append(join(auxList, ''))
    return join(newList, ' ')

print function("hola que hace")
