from persona import Persona
from departamento import Departamento
# print(type(Persona),Persona)

class Empleado(Persona,Departamento):
    def __init__(self,nombre:str,apellido:str,fecha:str,dni:str,direccion:list,nombredepartamento, telefonodepartamento, salario,horario):
        # self.datos_persona=Persona(nombre,apellido,fecha,dni,direccion)
        Persona.__init__(self,nombre,apellido,fecha,dni,direccion)
        # self.pertenece_departamento=Departamento(nombredepartamento, telefonodepartamento,self)
        Departamento.__init__(self,nombredepartamento, telefonodepartamento,self)
        self.salario=salario
        self.horario=horario
    # def __str__(self):
    #     return f"Persona:\n{self.datos_persona}\nDepartamento:\n{self.pertenece_departamento}\nempleado:\nsalario: {self.salario}, horario: {self.horario}"

    def __str__(self):
        return f"Persona:\n{Persona.__str__(self)}\nDepartamento:\n{Departamento.__str__(self)}\nempleado:\nsalario: {self.salario}, horario: {self.horario}"

