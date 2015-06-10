class Monitor(object):
    def __init__(self, nombre, hora_inicio, hora_fin):
        self.nombre = nombre
        self.hora_inicio = hora_inicio
        self.hora_final = hora_fin
        self.cruces_horarios = []

    def __lt__(self, compara):
        return len(self.cruces_horarios) > len(compara.cruces_horarios)

    def getNombre(self):
        return self.nombre

    def getHora_inicio(self):
        return self.hora_inicio

    def getHora_final(self):
        return self.hora_final

    def setCruces_horarios(self, monitor_cruce):
        self.cruces_horarios.append(monitor_cruce)

    def getCruces_horarios(self):
        return self.cruces_horarios
