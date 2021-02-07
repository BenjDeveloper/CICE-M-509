
class Persona(object):
    def __init__ (self, nombre, apellido, fecha_de_nacimiento, dni, direccion ):
        self.nombre = nombre
        self.apellido = apellido
        self.__fecha_de_nacimiento = fecha_de_nacimiento
        self.dni = dni
        self.direccion = direccion

    def __str__ (self):
        return f''': {self.dni} : {self.nombre} {self.apellido}'''

    # return f'''
    #         Nombre : {self.nombre} 
    #         Apellido : {self.apellido}
    #         Fecha de nacimiento : {self.__fecha_de_nacimiento }
    #         DNI : {self.dni} 
    #         Direccion : {self.direccion}'''

    def getNombreCompleto (self):
        return f' El nombre completo de la persona es:  {self.nombre}  {self.apellido}'

    def getDia(self):
        dia_1 = self.__fecha_de_nacimiento.split ('-')
        return dia_1[0]
    def getMes(self):
        mes = self.__fecha_de_nacimiento.split ('-')
        return mes [1]
    def getAño(self):
        año = self.__fecha_de_nacimiento.split ('-')
        return año [2]

    def setDia(self, dia):
        fecha = self.__fecha_de_nacimiento.split ('-') 
        fecha [0] = dia
                                        #TODO: Solo te falto la asignacion de la nueva fecha a al atributo __fecha_de_nacimiento
        self.__fecha_de_nacimiento = str (fecha [0]) +'-'+ str (fecha[1])  +'-'+ str (fecha[2])
        return self.__fecha_de_nacimiento

    def setMes(self, mes):
        fecha = self.__fecha_de_nacimiento.split ('-') 
        fecha [1] = mes
        self.__fecha_de_nacimiento = str (fecha [0]) +'-'+ str (fecha[1])  +'-'+ str (fecha[2])
        return self.__fecha_de_nacimiento

    def setAño(self, año):
        fecha = self.__fecha_de_nacimiento.split ('-') 
        fecha [2] = año
        self.__fecha_de_nacimiento = str (fecha [0]) +'-'+ str (fecha[1])  +'-'+ str (fecha[2])
        return self.__fecha_de_nacimiento

    def setFecha_De_Nacimiento (self, nueva_fecha_de_nacimiento):
        self.__fecha_de_nacimiento = nueva_fecha_de_nacimiento
        

albita = Persona ('alba', 'Herresanchez', '12-05-2002', '1234565', 'torrejon')



# print (albita)
# print (albita.getDia())
# print (albita.getMes ())
# print (albita.getAño ())
# print (albita.setDia(25))
# print (albita.setMes(9))
# print (albita.setAño(2005))


