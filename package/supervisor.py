
from .persona import Persona
from .usuario import Usuario

class Supervisor(Persona,Usuario):
    def __init__(self, nombre, apellido, fecha_de_nacimiento, dni, direccion, email, clave, activo):
        Persona.__init__(self, nombre, apellido, fecha_de_nacimiento, dni, direccion)
        Usuario.__init__(self, email, clave, activo)
        self.departamento = None

    def __str__ (self):
        return 'SUPERVISOR \nNombre: ' + self.nombre +'\nApellido: ' + self.apellido + '\nFecha de nacimiento: ' + self.fecha_de_nacimiento +'\nDni: ' + self.dni +'\nEmail: ' + self.email 