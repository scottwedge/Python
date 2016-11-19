from Tkinter import *
from ScrolledText import Scrollbar
from ttk import Treeview

class GUIBuscador(Tk):

	def __init__(self, master = None):
		Tk.__init__(self, master)
		self.gui(master)
		self.dir = 'D:\Talker\Talker\Biblia'
		self.direc = glob("%s\*" % self.dir)

	def gui(self, master):
		self.frm = Frame(master)
		self.frm.pack(side = LEFT, expand = YES, fill = BOTH)
		self.left_side(self.frm)

		self.frm = Frame(master)
		self.frm.pack(side = RIGHT, expand = YES, fill = BOTH)
		self.right_side(self.frm)

	def left_side(self, master):
		self.nombre = Entry(master, justify = CENTER, bd = 3, font = ('Ravie', 11), textvariable = self.NameVar)
		self.nombre.pack(side = TOP, fill = X)
		self.nombre.bind("<Key>", self.Enter)
		self.texto = Entry(master, justify = CENTER, bd = 3, font = ('Ravie', 11), textvariable = self.TextVar)
		self.texto.pack(side = TOP, fill = X)
		self.texto.bind("<Key>", self.Enter)
		self.tag = Entry(master, justify = CENTER, bd = 3, font = ('Ravie', 11), textvariable = self.TagsVar)
		self.tag.pack(side = TOP, fill = X)
		self.tag.bind("<Key>", self.Enter)
		self.tree = Treeview(master)
		self.tree.pack(side = LEFT, expand = YES, fill = BOTH)
		self.tree.bind("<Double-1>", self.OnDoubleClick)

	def right_side(self, master):
		self.text = Text(master, bg = 'skyblue', bd = 5, 
					font = ('consolas', 12), fg = 'red')
		self.text.pack(expand = YES, side = LEFT, fill = BOTH)
		self.yscroller = Scrollbar(master, command = self.text.yview)
		self.yscroller.pack(side = RIGHT, fill = Y)
		self.text['yscrollcommand'] = self.yscroller

	def OnDoubleClick(self, tree):
		try:
			item = self.tree.selection()[0]
			self.tree.item.open(item)
		except IndexError:
			pass

	def Enter(self, event):
		if event.char == ord(13):
			self.buscar()

	def buscar(self):
		name = NameVar.get()
		text = TextVar().get()
		etiqueta = TagsVar.get().split(',')
		self.aciertos = []
		for carpeta in self.direc:
			root = tree.insert("", 1, name[-3], text = name[-3])
			self.aciertos = []
			for versiculo in glob("%s\*" % carpeta):
				with open(versiculo, 'r') as nota:
					texto = nota.readlines()
					etiquetas = texto[-1].split(',')
					if name != '':
						versiculo = versiculo.replace(".txt", "")
						if re.search('%s' % name, versiculo):
							pass
						else:
							continue
					if etiqueta != []:
						for i in etiquetas:
							if i in etiqueta:
								break
						else:
							continue
					if text != '':
						for line in texto:
							if re.search(r'%s' % text, line):
								break
						else:
							continue
					tree.insert(raiz, "end", name, text = name[-1])
					self.aciertos.append(versiculo)
			if self.aciertos == []:
				self.tree.delete(root)

if __name__ == '__main__':
	GUI = GUIBuscador()
	GUI.state('zoomed')
	GUI.mainloop()