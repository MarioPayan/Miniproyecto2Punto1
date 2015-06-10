import itertools


class AlgoritmoIngenuo:

	def cruce(self, monitorA, monitorB):
		if monitorA.getHora_inicio() == monitorB.getHora_inicio():
			return True
		elif monitorA.getHora_inicio() < monitorB.getHora_inicio() and monitorA.getHora_final() > monitorB.getHora_inicio():
			return True
		elif monitorA.getHora_inicio() > monitorB.getHora_inicio() and monitorA.getHora_inicio() < monitorB.getHora_final():
			return True
		else: return False

	def disponibilidad(self, listaMonitores):
		horasDisponibles = 0
		for monitor in listaMonitores:
			horasDisponibles = horasDisponibles + (monitor.getHora_final() - monitor.getHora_inicio())
		return horasDisponibles

	def validar(self, listaMonitores):
		listaMonitoresOrdenados = sorted(listaMonitores, key=lambda monitor: monitor.getHora_inicio())
		monitorTmp = listaMonitores[0]
		for monitor in listaMonitores[1:]:
			if self.cruce(monitor, monitorTmp):
				return False
			else:
				monitorTmp = monitor
		return True

	def resolver(self, listaMonitores):
		solucion = [listaMonitores, 0]
		for numeroMonitor in reversed(range(len(listaMonitores))):
			combinacionesN = list(itertools.combinations(listaMonitores, numeroMonitor+1))
			for combinacion in combinacionesN:
				if self.validar(combinacion):
					if self.disponibilidad(combinacion) > solucion[1]:
						solucion = [combinacion, self.disponibilidad(combinacion)]
		return solucion