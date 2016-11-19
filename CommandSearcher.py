#!/usr/bin/python

def Buscar(s):
	posibles = []
	pos, neg = 0, 0
	with open("Comandos.txt") as archivo:
		for linea in archivo:
			for palabra in linea:
				for letra in palabra:
					for pal in s:
						if letra in s:
							pos++;
						else:
							neg++;
				if pos > neg:
					posibles.append(linea)
				pos, neg = 0, 0