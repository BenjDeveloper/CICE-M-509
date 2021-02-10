
from .empleado import Empleado
class Departamento:
    def __init__ (self, nombre, telefono,lista_empleados = []):
        self.nombre = nombre
        self.telefono = telefono
        self.empleados = lista_empleados

    def __str__ (self):
        cadena = f''' DEPARTAMENTO {self.nombre.upper ()} -- Teléfono del departamento: {self.telefono}
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

    def reporte_empleados (self):
        lis_emple = []
        lis_salar = []
        for empleado in self.empleados:
            lis_emple.append (empleado.nombre)
            lis_salar.append (empleado.salario)
        diccionaro_reporte = dict(zip (lis_emple, lis_salar))
        # diccionaro_reporte = {'nombre:' : lis_emple, 'salario:' : lis_salar}
        
        for k,v  in diccionaro_reporte.items():

            print (f' El salario de {k}  del departamento {self.nombre.upper()} es {v} euros al año')

        

