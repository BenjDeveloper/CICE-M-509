
from package.empleado import Empleado
import csv, os, sys


#? 2) EJERCICIO
# agrege una clase al paquete que permita manejar una lista del departamento 
# llamada Gerencia y posea el nombre de la empresa


class Gerencia():

    def __init__(self, empresa, departamentos = [], emp_sin_dep = []):
        self.empresa = empresa
        self.departamentos = departamentos
        self.emp_sin_dep = emp_sin_dep

    def __str__(self):
        return f'Nombre empresa: {self.empresa}'

    def carga_empleados(self, cargas):
        for depart in cargas:
            if not depart in self.departamentos:
                self.departamentos.append(depart)
                # print(f'\n{depart.nombre} agregado a la lista de departamentos de {self.empresa}')    
            f = open(cargas[depart],'r')
            lectura = csv.reader(f)
            for empleado in lectura:
                depart.empleados.append(Empleado(empleado[0],empleado[1],empleado[2],empleado[3],empleado[4],empleado[5],empleado[6],empleado[7],empleado[8],empleado[9]))
                # print(f'{empleado[0]} {empleado[1]} agregado/a a la lista de empleados del departamento de {depart.nombre}')
            f.close()

    def muestra_departamentos(self):
        print('\n')
        for dep in self.departamentos:
            print(dep)

    def muestra_empleados(self):
        print('\n')
        for dep in self.departamentos:
            for emp in dep.empleados:
                print (emp)
        for emp in self.emp_sin_dep:
            print(emp)

    def editar_empleado(self, emp):
        opc = input('''\n¿Qué desea editar de este empleado? 
                    1 - Direccion
                    2 - Email
                    3 - Clave
                    4 - Activo
                    5 - Salario
                    6 - Horario
                    7 - CANCELAR''')
        if opc == '1':
            emp.direccion = input('\nIntroduzca la nueva dirección: ')
        if opc == '2':
            emp.email = input('\nIntroduzca el nuevo email: ')
        if opc == '3':
            emp.clave = input('\nIntroduzca la nueva clave: ')
        if opc == '4':
            if emp.activo == 'True':
                emp.activo = 'False'
                print('El empleado NO está activo ahora')
            else:
                emp.activo = 'True'
                print('El empleado está activo ahora')
        if opc == '5':
            emp.salario = input('\nIntroduzca el nuevo salario: ')
        if opc == '6':
            emp.horario = input('\nIntroduzca el nuevo horario: ')
        if opc == '7':
            return

    def buscar_empleado(self, dni):
        for dto in self.departamentos:
            for emp in dto.empleados:
                if emp.dni == dni:
                    return self.editar_empleado(emp)
        for emp in self.emp_sin_dep:
            if emp.dni == dni:
                return self.editar_empleado(emp)
        print('\nNo hay coincidencias')

    # def buscar_departamento(self,nombre):

    def menu_crud(self, opt):
        os.system('cls')
        print('C - Crear un','empleado' if opt == '1' else 'departamento','\nR - Consultar existencias \nU - Editar datos \nD - Eliminar un','empleado' if opt == '1' else 'departamento','\nS - SALIR')
        seleccion = input('\n¿Qué acción desea realizar? (C, R, U, D ó S): ').upper()
        while not seleccion in ('C','R','U','D','S'):
            seleccion = input('Opción incorrecta. ¿Qué acción desea realizar? (C, R, U, D ó S): ')
        
    #     if seleccion == 'C':
    #         if opt == '1':
    #             #*Crear empleado
    #         else:
    #             #*Crear departamento
        if seleccion == 'R':
            if opt == '1':
                self.muestra_empleados()
            else:
                self.muestra_departamentos()
        if seleccion == 'U':
            if opt == '1':
                self.buscar_empleado(input('\nIntroduzca el dni del empleado que desea editar: '))
    #         else:
    #             #*Editar departamento
    #     if seleccion == 'D':
    #         if opt == '1':
    #             #*Eliminar empleado
    #         else:
    #             #*Eliminar departamento
        if seleccion == 'S' or opt == '3':
            print("Adiós...")   # Muestra despedida
            sys.exit()          # Salir

    def menu_principal(self):
        os.system('cls')
        print('''\t *MENÚ PRINCIPAL*
        1- Empleados
        2- Departamentos
        3- Salir''')
        seleccion = input('\n¿Qué campo desea editar o consultar? (1 ó 2): ')
        while not seleccion in ('1','2','3'):
            seleccion = input('Opción incorrecta. ¿Qué campo desea editar o consultar? (1 ó 2): ')
        return self.menu_crud(seleccion)