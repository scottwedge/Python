#!/usr/bin/env
# -*- encoding:utf-8 -*-

from Tkinter import *
from random import randrange
from time import sleep

class Escalonada(Tk):

	def __init__(self, master):
		Tk.__init__(self, master)
		self.master = master
		self.score = 0
		self.high_score = 0
		self.cont = 0
		self.bucle = False
		self.cuerpo()
		self.bind("<Key>", self.start)

	def cuerpo(self):
		self.linea_1()
		self.linea_2()
		self.linea_3()
		self.linea_4()

	def start(self, event):
		try:
			if int(event.char) > 0 and int(event.char) < 5:
				self.bind("<Key>", self.tecla)
				self.random()
				while True:
					self.times()
		except:
			pass

	def act_lin_2(self):
		self.btn5["bg"] = "white"
		self.btn6["bg"] = "white"
		self.btn7["bg"] = "white"
		self.btn8["bg"] = "white"
		if self.btn1["bg"] == "black":
			self.btn1["bg"] = "white"
			self.btn5["bg"] = "black"
		if self.btn2["bg"] == "black":
			self.btn2["bg"] = "white"
			self.btn6["bg"] = "black"
		if self.btn3["bg"] == "black":
			self.btn3["bg"] = "white"
			self.btn7["bg"] = "black"
		if self.btn4["bg"] == "black":
			self.btn4["bg"] = "white"
			self.btn8["bg"] = "black"

	def act_lin_3(self):
		self.btn9["bg"] = "white"
		self.btn10["bg"] = "white"
		self.btn11["bg"] = "white"
		self.btn12["bg"] = "white"
		if self.btn5["bg"] == "black":
			self.btn5["bg"] = "white"
			self.btn9["bg"] = "black"
		if self.btn6["bg"] == "black":
			self.btn6["bg"] = "white"
			self.btn10["bg"] = "black"
		if self.btn7["bg"] == "black":
			self.btn7["bg"] = "white"
			self.btn11["bg"] = "black"
		if self.btn8["bg"] == "black":
			self.btn8["bg"] = "white"
			self.btn12["bg"] = "black"

	def act_lin_4(self):
		self.btn13["bg"] = "white"
		self.btn14["bg"] = "white"
		self.btn15["bg"] = "white"
		self.btn16["bg"] = "white"
		if self.btn9["bg"] == "black":
			self.btn9["bg"] = "white"
			self.btn13["bg"] = "black"
		if self.btn10["bg"] == "black":
			self.btn10["bg"] = "white"
			self.btn14["bg"] = "black"
		if self.btn11["bg"] == "black":
			self.btn11["bg"] = "white"
			self.btn15["bg"] = "black"
		if self.btn12["bg"] == "black":
			self.btn12["bg"] = "white"
			self.btn16["bg"] = "black"

	def linea_1(self):
		frame = Frame(self.master)
		self.btn1 = Button(frame, bg = "white", state = "disabled")
		self.btn1.pack(side = LEFT, fill = BOTH, expand = YES)
		self.btn2 = Button(frame, bg = "white", state = "disabled")
		self.btn2.pack(side = LEFT, fill = BOTH, expand = YES)
		self.btn3 = Button(frame, bg = "white", state = "disabled")
		self.btn3.pack(side = LEFT, fill = BOTH, expand = YES)
		self.btn4 = Button(frame, bg = "white", state = "disabled")
		self.btn4.pack(side = LEFT, fill = BOTH, expand = YES)
		frame.pack(side = TOP, fill = BOTH, expand = YES)

	def linea_2(self):
		frame = Frame(self.master)
		self.btn5 = Button(frame, bg = "white", state = "disabled")
		self.btn5.pack(side = LEFT, fill = BOTH, expand = YES)
		self.btn6 = Button(frame, bg = "white", state = "disabled")
		self.btn6.pack(side = LEFT, fill = BOTH, expand = YES)
		self.btn7 = Button(frame, bg = "white", state = "disabled")
		self.btn7.pack(side = LEFT, fill = BOTH, expand = YES)
		self.btn8 = Button(frame, bg = "white", state = "disabled")
		self.btn8.pack(side = LEFT, fill = BOTH, expand = YES)
		frame.pack(side = TOP, fill = BOTH, expand = YES)

	def linea_3(self):
		frame = Frame(self.master)
		self.btn9 = Button(frame, bg = "white", state = "disabled")
		self.btn9.pack(side = LEFT, fill = BOTH, expand = YES)
		self.btn10 = Button(frame, bg = "white", state = "disabled")
		self.btn10.pack(side = LEFT, fill = BOTH, expand = YES)
		self.btn11 = Button(frame, bg = "white", state = "disabled")
		self.btn11.pack(side = LEFT, fill = BOTH, expand = YES)
		self.btn12 = Button(frame, bg = "white", state = "disabled")
		self.btn12.pack(side = LEFT, fill = BOTH, expand = YES)
		frame.pack(side = TOP, fill = BOTH, expand = YES)

	def linea_4(self):
		frame = Frame(self.master)
		self.btn13 = Button(frame, bg = "white", state = "disabled")
		self.btn13.pack(side = LEFT, fill = BOTH, expand = YES)
		self.btn14 = Button(frame, bg = "white", state = "disabled")
		self.btn14.pack(side = LEFT, fill = BOTH, expand = YES)
		self.btn15 = Button(frame, bg = "white", state = "disabled")
		self.btn15.pack(side = LEFT, fill = BOTH, expand = YES)
		self.btn16 = Button(frame, bg = "white", state = "disabled")
		self.btn16.pack(side = LEFT, fill = BOTH, expand = YES)
		frame.pack(side = TOP, fill = BOTH, expand = YES)

	def reset(self):
		for i in [self.btn1, self.btn2, self.btn3, self.btn4, 
					self.btn5, self.btn6, self.btn7, self.btn8, 
					self.btn9, self.btn10, self.btn11, self.btn12, 
					self.btn13, self.btn14, self.btn15, self.btn16]:
			i["bg"] = "white"

	def not_over(self):
		for i in [self.btn13, self.btn14, self.btn15, self.btn16]:
			if i["bg"] == "black":
				# self.gameover()
				pass
		self.random()

	def times(self):
		self.random()
		self.act_lin_2()
		sleep(100)
		self.act_lin_3()
		self.act_lin_2
		sleep(100)
		self.act_lin_3
		self.act_lin_4()
		sleep(100)
		self.not_over()

	def random(self):
		self.randlista = [self.btn1, self.btn2, self.btn3, self.btn4]
		azar = randrange(4)
		self.randlista[azar].config(bg = "black")

	def continuar(self):
		v2.destroy()
		self.deiconify()
		self.bucle = False

	def gameover(self):
		self.withdraw()
		v2 = Toplevel()
		texto = "El juego ha terminado\nPuntos %s\nPuntaje máximo: %s" % (self.score, self.high_score)
		label = Label(v2, text = texto, justify = CENTER)
		label.pack(fill = BOTH, expand = YES)
		boton = Button(v2, text = "Jugar", command = self.continuar)
		boton.pack(fill = BOTH, expand = YES)
		self.bucle = True
		while self.bucle == True:
			pass

	def click(self, char):
		if char == '1' and self.btn13["bg"] == "black":
			self.btn13["bg"] = "grey"
		elif char == '2' and self.btn14["bg"] == "black":
			self.btn14["bg"] = "grey"
		elif char == '3' and self.btn15["bg"] == "black":
			self.btn15["bg"] = "grey"
		elif char == '4' and self.btn16["bg"] == "black":
			self.btn16["bg"] = "grey"
		else:
			# self.gameover()
			return None
		self.score += 1

	def tecla(self, event):
		try:
			if int(event.char) > 0 and int(event.char) < 5:
				self.click(event.char)
		except:
			pass

if __name__ == '__main__':
	Juego = Escalonada(None)
	Juego.state("zoomed")
	Juego.title("Escalonada")
	Juego.mainloop()