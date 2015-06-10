import os
### Esta clase se encarga de los metodos de escritura y lectura sobre archivos planos que contienen la informacion
### de las entradas y salidas respectivamente
class IO:
    ficheroEntrada = ""

    def __init__(self, ficheroEntrada):
        self.ficheroEntrada = ficheroEntrada

    def leer(self):
        archivo = open(self.ficheroEntrada, "r", 1)
        informacion = []
        numero_lineas = int(archivo.readline())
        for i in range(0, numero_lineas):
            linea = archivo.readline()
            informacion.append(linea)
        archivo.close()
        return informacion

    def escribir(self, informacion):
        archivo = open("reporte.txt", "w")
        for linea in informacion:
            archivo.write(str(linea) + '\n')
        archivo.close()