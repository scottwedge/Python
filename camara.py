import numpy as np
import cv2
from Tkinter import *
import tkMessageBox
from time import sleep

def foto():
    cap = cv2.VideoCapture(1)
    img = np.zeros((300,512,3), np.uint8)
    cv2.namedWindow('Camara')
    img = ""
    on = 1
    while on == 1:
        while(True):
            if cap.isOpened():
                ret, frame=cap.read()
                cv2.imshow('Camara',frame)
                if cv2.waitKey(1) & 0xFF == 13:
                    img = frame
                    break
                elif cv2.waitKey(1) & 0xFF == 27:
                    exit(0)
            else:
                cap.open(1)
        while True:
            if cv2.waitKey(1) & 0xFF == ord('s'):
                on = 0
                address = 'C:\Users\Alumno\Desktop\Foto.png'
                cv2.imwrite(address, img)
                tkMessageBox.showinfo("Aviso", "La imagen ha sido guardada")
            elif cv2.waitKey(1) & 0xFF == ord('d'):
                pass
            elif cv2.waitKey(1) & 0xFF == 27:
                on = 0
            else:
                continue
            break
        cap.release()
        cv2.destroyAllWindows()
    exit(0)
    
v1 = Tk()
v1.title('Camara')

btn1 = Button(v1, text = "Iniciar", command = foto).pack(fill = BOTH)
lbl1 = Label(v1, text = "Mantenga ENTER para capturar").pack(fill = BOTH)
lbl2 = Label(v1, text = "Mantenga s para guardar").pack(fill = BOTH)
lbl3 = Label(v1, text = "Mantenga d para descartar").pack(fill = BOTH)
lbl4 = Label(v1, text = "Mantenga ESC para salir").pack(fill = BOTH)

v1.mainloop()
