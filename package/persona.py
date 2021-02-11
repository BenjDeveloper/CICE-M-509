
class Persona(object):
    def __init__ (self, nombre, apellido, fecha_de_nacimiento, dni, direccion ):
        self.nombre = nombre
        self.apellido = apellido
        self.fecha_de_nacimiento = fecha_de_nacimiento
        self.dni = dni
        self.direccion = direccion

    def __str__ (self):
        return f': {self.dni} : {self.nombre} {self.apellido}'

    def getNombreCompleto (self):
        return f'{self.nombre}  {self.apellido}'

    def getDia(self):
        dia_1 = self.fecha_de_nacimiento.split ('-')
        return dia_1[0]
    def getMes(self):
        mes = self.fecha_de_nacimiento.split ('-')
        return mes [1]
    def getAño(self):
        año = self.fecha_de_nacimiento.split ('-')
        return año [2]

    def setDia(self, dia):
        fecha = self.fecha_de_nacimiento.split ('-') 
        fecha [0] = dia
        self.fecha_de_nacimiento = str (fecha [0]) +'-'+ str (fecha[1])  +'-'+ str (fecha[2])
        return self.fecha_de_nacimiento

    def setMes(self, mes):
        fecha = self.fecha_de_nacimiento.split ('-') 
        fecha [1] = mes
        self.fecha_de_nacimiento = str (fecha [0]) +'-'+ str (fecha[1])  +'-'+ str (fecha[2])
        return self.fecha_de_nacimiento

    def setAño(self, año):
        fecha = self.fecha_de_nacimiento.split ('-') 
        fecha [2] = año
        self.fecha_de_nacimiento = str (fecha [0]) +'-'+ str (fecha[1])  +'-'+ str (fecha[2])
        return self.fecha_de_nacimiento