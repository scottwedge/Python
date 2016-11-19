class persona(object):
	"""Caracteristicas de cada persona"""
	def __init__(self, nombre, edad, altura, peso):
		self.nombre = nombre
		self.edad = edad
		self.altura = altura
		self.peso = peso

	def printer(self):
		print self.nombre
		print self.edad
		print self.altura
		print self.peso

class gente(persona):
	"""Varias personas en una clase"""
	def __init__(self, pers1, pers2):
		self.pers1 = pers1
		self.pers2 = pers2

	def edad(self):
		print self.pers1.edad
		print self.pers2.edad