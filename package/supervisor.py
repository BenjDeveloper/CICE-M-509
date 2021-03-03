from .persona import Persona
from .usuario import Usuario

class Supervisor(Persona, Usuario):
    def __init__(self, nombre, apellido, fecha_de_nacimiento, dni, direccion, email, clave, activo):
        Persona.__init__(self, nombre, apellido, fecha_de_nacimiento, dni, direccion)
        Usuario.__init__(self, email, clave, activo)
        self.departamento = None