import numpy as np
import cv2
from Tkinter import *
import tkMessageBox

def video():
    on = 0
    cap=cv2.VideoCapture(1)
    while cap.isOpened() == False:
        cap.open(1)
    fourcc = cv2.cv.CV_FOURCC(*'IYUV')
    out=cv2.VideoWriter('output.avi',fourcc,20.0,(640,480))
    while cap.isOpened():
        ret, frame=cap.read()
        if ret==True:
            cv2.imshow('Video', frame)
            if on == 1:
                out.write(frame)
                var.set("Mantenga ENTER para pausar")
            elif on == 2:
                var.set("Mantenga ENTER para continuar")
                break
            if cv2.waitKey(1) & 0xFF == 13:
                on += 1
            elif cv2.waitKey(1) & 0xFF == 27:
                break
    cap.release()
    out.release()
    cv2.destroyAllWindows()

v1 = Tk()
v1.title('Camara')

var = StringVar()
var.set("Mantenga ENTER para iniciar")

btn1 = Button(v1, text = "Iniciar", command = video).pack(fill = BOTH)
lbl1 = Label(v1, textvariable = var).pack(fill = BOTH)
lbl4 = Label(v1, text = "Mantenga ESC para salir").pack(fill = BOTH)

v1.mainloop()
