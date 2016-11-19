#!/usr/bin/env

from glob import glob
from os import mkdir
from shutil import move
from time import sleep

lista = []
enlista = []
direccion = "C:/Users/Alumno/Desktop"

def guardar(enlista):
	for i in lista:
		move("%s/%s" % (direccion, i), "D:\Talker\Talker\Escuela\Electronica\Lenguaje Electronico\III")
		sleep(1)

def mover(i):
	global enlista
	enlista.append(i)
	mkdir("%s/%s" % (direccion, i))
	try:
		move(("%s/%s.exe" % (direccion, i)), ("%s/%s" % (direccion, i)))
		move(("%s/%s.cpp" % (direccion, i)), ("%s/%s" % (direccion, i)))
	except IOError, e:
		pass

def joiner():
	global enlista
	archivos = glob("%s/*.*" % direccion)
	for i in archivos:
		i = i.replace("%s\\" % direccion , "")
		lista.append(i.split(".")[0])
	for i in lista:
		if lista.count(i) == 2:
			lista.remove(i)
			mover(i)
	guardar(enlista)

joiner()