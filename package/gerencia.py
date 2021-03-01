
class Gerencia():

    #CONSTRUCTOR
    def __init__(self, nombre_empresa):
        self.nombre_empresa = nombre_empresa
from package.empleado import Empleado
import csv
import os

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

    def muestra_departamentos(self):

        for dep in self.departamentos:
            print(dep)

    def menu_crud(opt):

        os.system('cls')
        print('C - Crear un','empleado' if opt == '1' else 'departamento','\nR - Consultar existencias \nU - Editar datos \nD - Eliminar un','empleado' if opt == '1' else 'departamento')
        seleccion = input('\n¿Qué acción desea realizar? (C,R,U ó D): ').upper()
        while not seleccion in ('C','R','U','D'):
            seleccion = input('Opción incorrecta. ¿Qué acción desea realizar? (C,R,U ó D): ')
        
        if seleccion == 'C':
            if opt == '1':
                #*Crear empleado
            else:
                #*Crear departamento
        if seleccion == 'R':
            if opt == '1':
                #*Ver empleados
            else:
                self.muestra_departamentos()
        if seleccion == 'U':
            if opt == '1':
                #*Editar empleado
            else:
                #*Editar departamento
        if seleccion == 'D':
            if opt == '1':
                #*Eliminar empleado
            else:
                #*Eliminar departamento


    def menu_principal():

        os.system('cls')
        print('''\t *MENÚ PRINCIPAL*
        1- Empleados
        2- Departamentos''')
        seleccion = input('\n¿Qué campo desea editar o consultar? (1 ó 2): ')
        while not seleccion in ('1','2'):
            seleccion = input('Opción incorrecta. ¿Qué campo desea editar o consultar? (1 ó 2): ')
        return menu_crud(seleccion)