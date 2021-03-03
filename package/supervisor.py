
# from datetime import time
from .Persona import Persona
from .User import User

class Supervisor(Persona,User):
    def __init__(self,nombre:str,apellido:str,fecha:str,dni:str,direccion:list,email, clave):
        Persona.__init__(self,nombre,apellido,fecha,dni,direccion)
        User.__init__(self,email,clave)
        self.departamento = None
