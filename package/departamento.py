
from .empleado import Empleado
class Departamento:
    def __init__ (self, nombre, telefono,lista_empleados = []):
        self.nombre = nombre
        self.telefono = telefono
        self.empleados = lista_empleados

    def __str__ (self):
        cadena = f'''\n DEPARTAMENTO {self.nombre.upper ()} -- Teléfono del departamento: {self.telefono}
        '''
        for empleado in self.empleados:
            cadena += empleado.getEmpleado()
        return cadena

    def media_salarial (self):
        salario_sum = 0
        for x in self.empleados:
            salario_sum += x.salario
            salario_media = salario_sum/ (len (self.empleados))
        return salario_media

    def sort(self,fn_lambda = lambda Empleado : Empleado.salario,  option = False ):
        self.empleados.sort( key = fn_lambda, reverse = option )


