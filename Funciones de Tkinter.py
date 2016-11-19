# Funciones de la libreria GUI Tkinter

# FUNCIONES DEL BOTON

import sys # Funcion sys.exit que cierra el programa
from Tkinter import * # Importa todas la funciones de la libreria

button = Button(None, text='Hello World', command=sys.exit) # arg1:ventana, arg2:texto arg3:funcion
button.pack() # Empaquetado
button.mainloop()

root = Tk() # Se crea ventana
Button(root, text='press', command=root.quit).pack(side=LEFT) # Alineacion del boton a la izquierda
root.mainloop()

root = Tk() # Se crea ventana
Button(root, text='press', command=root.quit).pack(side=LEFT, expand=YES, fill=X) # fill=X,Y,BOTH - Expande el boton
root.mainloop()

def hello(event):
    print "Press twice to exit"

def quit(event):
    print "Hello. i must be going"
    import sys; sys.exit()

button = Button(None, text="Hello World")
button.pack()
button.bind('<Button-l>', hello)
button.bind('<Double-l>', quit)
button.mainloop()


# FUNCIONES DEL LABEL


