from .mascota import Mascota

class Persona(object):
    #CONSTRUCTOR
    def __init__ (self, nombre, apellido,direccion , dni, mascotas ):
        self.nombre = nombre
        self.apellido = apellido
        self.direccion = direccion
        self.dni = dni
        self.mascotas = {}

        

