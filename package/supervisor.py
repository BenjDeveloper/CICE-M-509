from .persona import Persona
from .usuario import Usuario

class Supervisor(Persona, Usuario):
    def __init__ (self, nombre, apellido, fecha_de_nacimiento, dni, direccion, email, clave, activo):
        Persona.__init__(self, nombre, apellido, fecha_de_nacimiento, dni, direccion)
        Usuario.__init__(self,email, clave, activo)
        self.departamento = None
    
    def __str__ (self):

        return f'''\n Supervisor - Nombre:  {self.nombre.upper ()} -- Apellido: {self.apellido} -- Fecha de nacimiento: {self.fecha_de_nacimiento} -- DNI: {self.dni} -- Direccion: {self.direccion} -- Email: {self.email} -- Clave: {self.clave} -- Activo: {self.activo}'''
        
        



