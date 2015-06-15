import itertools

class Algoritmo:

	solucion = [[], 0]

	def disponibilidad(self, listaMonitores):
		horasDisponibles = 0
		for monitor in listaMonitores:
			horasDisponibles = horasDisponibles + (monitor.getHora_final() - monitor.getHora_inicio())
		return horasDisponibles

	def cruce(self, monitorA, monitorB):
		if monitorA.getHora_inicio() == monitorB.getHora_inicio():
			return True
		elif monitorA.getHora_inicio() < monitorB.getHora_inicio() and monitorA.getHora_final() > monitorB.getHora_inicio():
			return True
		elif monitorA.getHora_inicio() > monitorB.getHora_inicio() and monitorA.getHora_inicio() < monitorB.getHora_final():
			return True
		else: return False

	def validar(self, listaMonitores):
		if(len(listaMonitores)==0 or len(listaMonitores)==1):
			return True
		listaMonitoresOrdenados = sorted(listaMonitores, key=lambda monitor: monitor.getHora_inicio())
		monitorTmp = listaMonitores[0]
		for monitor in listaMonitores[1:]:
			if self.cruce(monitor, monitorTmp):
				return False
			else:
				monitorTmp = monitor
		return True

class AlgoritmoIngenuo(Algoritmo):

	def resolver(self, listaMonitores):
		for numeroMonitor in reversed(range(len(listaMonitores))):
			combinacionesN = list(itertools.combinations(listaMonitores, numeroMonitor+1))
			for combinacion in combinacionesN:
				if self.validar(combinacion):
					if self.disponibilidad(combinacion) > self.solucion[1]:
						self.solucion = [combinacion, self.disponibilidad(combinacion)]
		return self.solucion

class AlgoritmoVoraz(Algoritmo):

	def ordenar(self,listaMonitores):
		listaMonitoresOrdenados = sorted(listaMonitores, key=lambda monitor: monitor.getHora_final() - monitor.getHora_inicio(), reverse=True)
		return listaMonitoresOrdenados

	def escoger(self,listaMonitores):
		listaMonitoresEscogidos = []
		cruzado = False
		for monitorEntrante in listaMonitores:
			for monitor in listaMonitoresEscogidos:
				if(self.cruce(monitorEntrante,monitor)):
					cruzado = True
			if(cruzado==False):
				listaMonitoresEscogidos.append(monitorEntrante)
			cruzado = False
		return listaMonitoresEscogidos

	def resolver(self,listaMonitores):
		
		listaMonitores = self.ordenar(listaMonitores)
		listaMonitores = self.escoger(listaMonitores)
		self.solucion = [listaMonitores,self.disponibilidad(listaMonitores)]
		return self.solucion

class AlgoritmoDinamico(Algoritmo):

	def recursion(self, listaMonitoresEscogidos, listaMonitoresRestantes, valor):
		if(len(listaMonitoresRestantes)==0):
			if(self.solucion[1]<valor):
				self.solucion = [listaMonitoresEscogidos, valor]
		else:
			listaMonitoresRestantesX = listaMonitoresRestantes[:]
			listaMonitoresX = listaMonitoresEscogidos[:]
			listaMonitoresX.append(listaMonitoresRestantes[-1])
			monitorNuevo = listaMonitoresRestantes[-1]
			if(len(listaMonitoresRestantesX)!=0):
				listaMonitoresRestantesX.pop()
			self.recursion(listaMonitoresEscogidos, listaMonitoresRestantesX, valor) #NO TOMA NADA
			if(self.validar(listaMonitoresX)):
				self.recursion(listaMonitoresX, listaMonitoresRestantesX, (valor+self.disponibilidad([monitorNuevo])))

	def resolver(self,listaMonitores):
		self.recursion([],listaMonitores,0)
		return self.solucion




