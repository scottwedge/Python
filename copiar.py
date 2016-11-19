def copiar(src, dest):
    with open(src, "r") as file:
        with open("%s/%s" % (dest, src.split("/")[-1]), "a") as archivo:
            archivo.write(file.read(-1))

copiar("/home/joel/Escritorio/FrameWork/App/Herramientas/index2.html", "/home/joel/Escritorio/Practica")
