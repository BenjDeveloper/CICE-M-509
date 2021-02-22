
from package.empleado import Empleado
import csv

#? 2) EJERCICIO
# agrege una clase al paquete que permita manejar una lista del departamento 
# llamada Gerencia y posea el nombre de la empresa


class Gerencia():

    def __init__(self, empresa, departamentos = []):
        self.empresa = empresa
        self.departamentos = departamentos


    def __str__(self):
        return f'Nombre empresa: {self.empresa}'

#? 3) EJERCICIO
# # partiendo del ejercicio anterior, cree una carga de datos desde un fichero.csv
# # que permita cargar 3 departamentos que tengan al menos 4 empleados cada uno

    def carga_empleados(self, cargas):

        for depart in cargas:
            if not depart in self.departamentos:
                self.departamentos.append(depart)
                print(f'\n{depart.nombre} agregado a la lista de departamentos de {self.empresa}')    
            f = open(cargas[depart],'r')
            lectura = csv.reader(f)
            for empleado in lectura:
                depart.empleados.append(Empleado(empleado[0],empleado[1],empleado[2],empleado[3],empleado[4],empleado[5],empleado[6],empleado[7],empleado[8],empleado[9]))
                print(f'{empleado[0]} {empleado[1]} agregado/a a la lista de empleados del departamento de {depart.nombre}')
            f.close()

            #             row_count = sum(1 for row in f)
            # if row_count>0:
    def muestra_departamentos(self):
        for dep in self.departamentos:
            print(dep)