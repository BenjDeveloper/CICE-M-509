
from package.persona import Persona 
from package.usuario import Usuario
from package.departamento import Departamento
import re


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

    def create():
        nombre = input('\nNombre:')
        apellido = input('\nApellido:')

        # c) validar que cuando introduzca una fecha pueda convertirla en un Datetime
        fecha_nacimiento = input('\nFecha de nacimiento (dd-mm-aaaa):')
        
        dni = input('\nDNI:')
        direccion = input('\nDireccion:')

        email = input('\nE-mail:')
        patron = '[A-z0-9]{4,30}[@][A-z0-9]{2,10}[.][A-z0-9]{2,4}'
        while not re.match( patron, email):
            email = input('\nEntrada incorrecta. E-mail:')
        
        clave = input('\nClave:')
        activo = 'False'

        # b) tambien debera validar que el salario es un numero y posteriormente convertirlo 
        salario = input('\nSalario:')
        
        horario = input('\nHorario:')
        return Empleado(nombre,apellido,fecha_nacimiento,dni,direccion,email,clave,activo,salario,horario)