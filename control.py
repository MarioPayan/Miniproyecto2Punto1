from IO import IO
from monitor import Monitor
from algoritmos import AlgoritmoIngenuo
import sys

class Control:
    fichero = ""
    entrada = ""
    monitores = []
    io = None
    resultado = []
    algoritmo = ""

    def __init__(self, fichero, algoritmo):
        self.io = IO(fichero)
        self.algoritmo = algoritmo

    def leer(self):
    	self.entrada = self.io.leer()

    def escribir(self):
        respuesta = []
        respuesta.append(len(self.resultado[0]))
        respuesta.append(self.resultado[1])
        for monitor in self.resultado[0]:
            respuesta.append(monitor.getNombre())
        self.io.escribir(respuesta)

    def interpretar(self):
        for linea in self.entrada:
            monitorTmp = linea.split(' ')
            nombre = monitorTmp[0]
            horaIni = int(monitorTmp[1].split(':')[0])
            horaFin = int(monitorTmp[3].split(':')[0])
            monitor = Monitor(nombre, horaIni, horaFin)
            self.monitores.append(monitor)

    def resolver(self, arg):
        if(arg==0):
            ingenuo = AlgoritmoIngenuo()
            resultado = ingenuo.resolver(self.monitores)
        if(arg==1):
            pass
        if(arg==2):
            pass
        self.resultado = resultado

    def run(self):
        self.leer()
        self.interpretar()
        if(sys.argv!=None):
            if(self.algoritmo=="ingenuo"):
                self.resolver(0)
            if(self.algoritmo=="voraz"):
                pass
            if(self.algoritmo)=="dinamico":
                pass
            if(len(self.resultado)!=0):
                self.escribir()

def main():
	control = Control(str(sys.argv[1]), str(sys.argv[2]))
	control.run()
	print("Reporte generado exitosamente :D")

if __name__ == '__main__':
    main()