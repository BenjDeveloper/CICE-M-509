# 7.- Cree una clase Empleado que herede de Persona y Usuario, adicionalmente posea el atributo:
# #     salario:float
# #     horario:str

from .persona import Persona
from .usuario import Usuario

class Empleado(Persona, Usuario):
    
    def __init__(self, salario:float, horario:str, email, contraseña, nombre:str, apellido:str, fecha_nacimiento, dni:str, direccion:list):
        Usuario.__init__(self,  email, contraseña)
        Persona.__init__(self,nombre, apellido, fecha_nacimiento, dni, direccion)
        self.salario = salario
        self.horario = horario

    def __str__(self):
        return f'\n Nombre: {self.nombre}\n Apellido:{self.apellido}\n DNI: {self.dni}\
            \n Dirección: {self.direccion}\n Horario: {self.horario}\n Email: {self.email }\n Contraseña: {self.contraseña }\n Salario: {self.salario }'

# e1 = Empleado(1400,'L-V 8H a 18H','raulito@gmail.com','asafsfafsf','Raúl','González','10/02/2000', '04358213-Z', 'Calle Piedra 28')
# print('Información del empleado:\n',e1)