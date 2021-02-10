
from datetime import time
from .Persona import Persona
from .departamento import Departamento
from .User import User
# print(type(Persona),Persona)

class Empleado(Persona,User):
    def __init__(self,nombre:str,apellido:str,fecha:str,dni:str,direccion:list,email, clave, salario,horario):

        Persona.__init__(self,nombre,apellido,fecha,dni,direccion)
        User.__init__(self,email,clave)
        self.pertenece_departamento=None  #! instancia
        
        self.salario=int(salario)
        self.horario=horario
        self.diainicio=horario.split(" ")[0].split("-")[0]
        self.diafinal=horario.split(" ")[0].split("-")[1]
        self.horainicio=time(hour=int(horario.split(" ")[1].split("-")[0][:-1]))
        self.horafinal=time(hour=int(horario.split(" ")[1].split("-")[1][:-1]))

    def __str__(self):
        return f"Persona:\n{Persona.__str__(self)}\nUsuaro:\n{User.__str__(self)}\nempleado:\nsalario: {self.salario}, horario: {self.horario}"

    def getHorasalDia(self):
        return self.horafinal.hour-self.horainicio.hour
