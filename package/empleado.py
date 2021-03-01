
from package.persona import Persona 
from package.usuario import Usuario
from package.departamento import Departamento


class Empleado(Persona, Usuario):

    def __init__(self, nombre, apellido, fecha_nacimiento, dni, direccion, email, clave, activo, salario, horario):
        Persona.__init__(self, nombre, apellido, fecha_nacimiento, dni, direccion)
        Usuario.__init__(self, email, clave, activo)
        self.salario = salario
        self.horario = horario

    def __str__(self):
        return f'''EMPLEADO : {self.nombre} {self.apellido}
            Fecha de nacimiento: {self.fecha_nacimiento} DNI: {self.dni} Direccion: {self.direccion}\n
            E-mail: {self.email} Clave: {self.clave} Activo: {self.activo}\n
            Horario: {self.horario} Salario: {self.salario}
        '''