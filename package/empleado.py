from package.persona import Persona 
from package.usuario import Usuario
from package.departamento import Departamento


class Empleado(Persona, Usuario):

    #CONSTRUCTOR
    def __init__(self, nombre, apellido, fecha_nacimiento, dni, direccion, email, clave, activo, salario, horario):
        Persona.__init__(self, nombre, apellido, fecha_nacimiento, dni, direccion)
        Usuario.__init__(self, email, clave, activo)
        self.salario = salario
        self.horario = horario

    #FUNCION IMPRIMIR
    def __str__(self):
        return f'''
        Los datos que hereda de Persona son: 
            Nombre: {self.nombre}
            Apellido: {self.apellido}
            Fecha de nacimiento: {self.fecha_nacimiento}
            DNI: {self.dni}
            Direccion: {self.direccion}\n
        Los datos que hereda de Usuario son: 
            E-mail: {self.email}
            Clave: {self.clave}
            Activo: {self.activo}\n
        Los datos propios de la clase Empleado son: 
            Horario: {self.horario}
            Salario: {self.salario}
        '''
