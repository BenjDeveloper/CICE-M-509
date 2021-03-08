from .persona import Persona 

class Veterinaria(object):
    #CONSTRUCTOR
    def __init__ (self, nombre, direccion , persona ):
        self.nombre = nombre
        self.direccion = direccion
        self.persona = {}