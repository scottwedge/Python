#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import os
import shutil
from Tkinter import *
from tkFileDialog import *
from tkMessageBox import showerror
from threading import Timer

class BackUper(object):

	def __init__(self, master):
		self.master = master
		self.ruta = ""
		self.tiempo = StringVar()
		self.time = 0
		self.gui()

	def iniciar(self):
		try:
			self.time = float(self.tiempo.get())
			self.iniciar.config(text="Cancelar")
			self.iniciar.config(command=self.frenar)
			self.t = Timer(self.time, self.backup)
			self.t.start()
			self.master.iconify()
		except ValueError:
			showerror("Ingrese un número", "No ha ingresado un número")

	def frenar(self):
		self.t.cancel()
		self.iniciar.config(text="Iniciar")
		self.iniciar.config(command=self.iniciar)

	def gui(self):
		self.select1 = Button(self.master, text="Elegir carpeta a copiar", command=self.elegirUbicacion, font=("Times", "50", "bold italic"))
		self.select1.pack(expand=YES, fill=BOTH)
		self.select2 = Button(self.master, text="Elegir carpeta de destino", command=self.elegirDestino, font=("Times", "50", "bold italic"))
		self.select2.pack(expand=YES, fill=BOTH)
		self.entry = Entry(self.master, textvariable=self.tiempo, justify=CENTER, font=("Times", "50", "bold italic"))
		self.entry.pack(expand=YES, fill=BOTH)
		self.iniciar = Button(self.master, text="Iniciar", command=self.iniciar, font=("Times", "50", "bold italic"))
		self.iniciar.pack(expand=YES, fill=BOTH)

	def backup(self):
		try:
			shutil.rmtree("%s/BackUp" % self.destino)
		except OSError:
			pass
		shutil.copytree("%s" % self.ubicacion, "%s/BackUp" % self.destino)
		self.t = Timer(self.time, self.backup)
		self.t.start()

	def elegirUbicacion(self):
		self.ubicacion = askdirectory()
		if self.ubicacion != "":
			self.select1.config(text=self.ubicacion)

	def elegirDestino(self):
		self.destino = askdirectory()
		if self.destino != "":
			self.select2.config(text=self.destino)

if __name__ == '__main__':
	root = Tk()
	root.attributes("-zoomed", True)
	root.title("BackUper")
	guardar = BackUper(root)
	root.mainloop()