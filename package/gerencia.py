
from package.empleado import Empleado, Departamento
import csv, os, sys

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
        while not opc in ('1','2','3','4','5','6','7'):
            opc = input('\nOpcion incorrecta. ¿Qué desea editar de este empleado? (1,2,3,4,5,6 ó 7): ')
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
                    return emp
        for emp in self.emp_sin_dep:
            if emp.dni == dni:
                return emp
        print('\nNo hay coincidencias')
        return None

    def editar_departamento(self, dto):
        opc = input('''\n¿Qué desea editar de este departamento? 
                    1 - Telefono
                    2 - Agregar empleado
                    3 - Quitar empleado
                    4 - CANCELAR''')
        while not opc in ('1','2','3','4'):
            opc = input('\nOpción incorrecta. ¿Qué desea editar de este departamento? (1,2,3 ó 4): ')
        if opc == '1':
            dto.telefono = input('\nIntroduzca el nuevo número de telefono: ')
        if opc == '2':
            emp = self.buscar_empleado(input('\nDNI del empleado que desea agregar: '))
            if emp != None:
                dto.empleados.append(emp)
        if opc == '3':
            if dto.empleados != []:
                cont = 0
                filtro = input('\nDNI del empleado que desea quitar: ')
                for emp in dto.empleados:
                    if filtro == emp.dni:
                        self.emp_sin_dep.append(dto.empleados.pop(cont))
                        print('\nEmpleado quitado del departamento.')
                        return
                    cont += 1
                print('\nEl empleado que busca no pertenece a este departamento. ')
            else:
                print('\nEste departamento no tiene empleados.')
        if opc == '4':
            return

    def buscar_departamento(self,nombre):
        for dto in self.departamentos:
            if dto.nombre == nombre:
                return dto
        print('\nNo hay coincidencias')
        return None

    def eliminar_empleado(self, dni):
        for dep in self.departamentos:
            cont = 0
            for emp in dep.empleados:
                if emp.dni == dni:
                    dep.empleados.pop(cont)
                cont += 1
        cont = 0    
        for emp in self.emp_sin_dep:
            if emp.dni == dni:
                self.emp_sin_dep.pop(cont)
            cont += 1

    def eliminar_departamento(self, nombre):
        cont = 0
        for dto in self.departamentos:
            if dto.nombre == nombre:
                self.departamentos.pop(cont)
            cont += 1

    def menu_crud(self, opt):
        os.system('cls')
        print('C - Crear un','empleado' if opt == '1' else 'departamento','\nR - Consultar existencias \nU - Editar datos \nD - Eliminar un','empleado' if opt == '1' else 'departamento','\nS - SALIR')
        seleccion = input('\n¿Qué acción desea realizar? (C, R, U, D ó S): ').upper()
        while not seleccion in ('C','R','U','D','S'):
            seleccion = input('Opción incorrecta. ¿Qué acción desea realizar? (C, R, U, D ó S): ')
        
        if seleccion == 'C':
            if opt == '1':
                self.emp_sin_dep.append(Empleado.create())
            else:
                self.departamentos.append(Departamento.create())
        if seleccion == 'R':
            if opt == '1':
                self.muestra_empleados()
            else:
                self.muestra_departamentos()
        if seleccion == 'U':
            if opt == '1':
                emp = self.buscar_empleado(input('\nIntroduzca el dni del empleado que desea editar: '))
                if emp != None:
                    self.editar_empleado(emp)
            else:
                dto = self.buscar_departamento(input('\nIntroduzca el nombre del departamento que desea editar: '))
                if dto != None:
                    self.editar_departamento(dto)
        if seleccion == 'D':
            if opt == '1':
                filtro = input('\nIntroduzca el dni del empleado que desea eliminar: ')
                self.eliminar_empleado(filtro)
            else:
                filtro = input('\nIntroduzca el nombre del departamento que desea eliminar: ')
                self.eliminar_departamento(filtro)
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