
from .persona import Persona
from .usuario import Usuario

class Empleado(Persona, Usuario):
    def __init__(self, nombre, apellido, fecha_de_nacimiento, dni, direccion, email, clave, activo, salario, horario):
        Persona.__init__(self, nombre, apellido, fecha_de_nacimiento, dni, direccion)
        Usuario.__init__(self, email, clave, activo)
        self.salario = salario
        self.horario = horario

    def __str__ (self):
        return 'Empleado : Salario = '+ str (self.salario)+' '+Persona.__str__(self) + Usuario.__str__(self) +' : Horario: '+ self.horario 

    def getEmpleado(self):
        return '\n'+self.__str__()