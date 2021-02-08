from datetime import datetime
#CAMBIAR A DATE TIME LAS FECHAS 

class Persona():

    #CONSTRUCTOR 
    def __init__(self, nombre, apellido, fecha_nacimiento, dni, direccion):
        self.nombre = nombre
        self.apellido = apellido
        self.fecha_nacimiento = fecha_nacimiento    # 'dia-mes-año'
        self.dni = dni
        self.direccion = direccion
        self.__dia = self.fecha_nacimiento.split('-')[0]
        self.__mes = self.fecha_nacimiento.split('-')[1]
        self.__año = self.fecha_nacimiento.split('-')[2]

    #FUNCION IMPRIMIR 
    def __str__(self):
        return f'''
        Nombre: {self.nombre}
        Apellido: {self.apellido}
        Fecha de nacimiento: {self.fecha_nacimiento}
        DNI: {self.dni}
        Direccion: {self.direccion}
        '''

    #GETTER Y SETTER
    def getNombreCompleto(self):
        return f'{self.nombre} {self.apellido}'


    def __strFecha__():
        fecha = self.fecha_nacimiento.strptime(self.fecha_nacimiento, '%d,%m,%y')

    '''def getDia(self):
        return self.__dia

    def getMes(self):
        return self.__mes

    def getAño(self):
        return self.__año

    def setDia(self, dia):
        self.__dia = dia
        self.fecha_nacimiento = f'{self.__dia}-{self.__mes}-{self.__año}'

    def setMes(self, mes):
        self.__mes = mes
        self.fecha_nacimiento = f'{self.__dia}-{self.__mes}-{self.__año}'

    def setAño(self, año):
        self.__año = año
        self.fecha_nacimiento = f'{self.__dia}-{self.__mes}-{self.__año}'''



