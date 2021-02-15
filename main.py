
# EJEMPLO DE MANEJO  DE REPOSITORIOS Y CLASES POR MEDIO DE PAQUETES
from package.employee import Employee
from package.department import Department
from package.managaError import ManageError
from package.manage import ManageLadder
from header import header
import csv

def main():
    header()
    obj = ManageLadder()
    shutdown = True
    while shutdown == True:
        option = input("1._DEPARTAMENTOS \n2._EMPLEADOS \n3._SALIR \nELIGA UNA OPCIÓN: ")
        if option == '1':
            go_back_to_main_menu = True
            while go_back_to_main_menu == True:
                department_options = input("1._CREAR DEPARTAMENTOS \n2._ACTUALIZAR DEPARTAMENTOS \
                                        \n3._VER DEPARTAMENTOS \n4._BORRAR DEPARTAMENTOS \n5._VOLVER AL MENÚ PRINCIPAL \
                                        \nELIGA UNA OPCIÓN: ")
                if department_options == '1': obj.createDepartment()
                elif department_options == '2': obj.updateDepartment()
                elif department_options == '3': obj.readDepartment()
                elif department_options == '4': obj.deleteDepartment()
                elif department_options == '5': go_back_to_main_menu = exit()
                else:
                    print("La opción introducida no es válida")        
            
        elif option == '2':
            go_back_to_main_menu = True
            while go_back_to_main_menu == True:
                employee_options = input("1._CREAR DEPARTAMENTOS \n2._ACTUALIZAR DEPARTAMENTOS \
                                        \n3._VER DEPARTAMENTOS \n4._BORRAR DEPARTAMENTOS \n5._VOLVER AL MENÚ PRINCIPAL \
                                        \nELIGA UNA OPCIÓN: ")
                if employee_options == '1': obj.createEmployee()
                elif employee_options == '2': obj.updateEmployee()
                elif employee_options == '3': obj.readEmployee()
                elif employee_options == '4': obj.deleteEmployee()
                else:
                    print("La opción introducida no es válida") 
        elif option == '3':
            shutdown = exit()
        else:
            print('La opción introducida no es válida') 
                


    
    #ma = ManageLadder()
    #ma.updateEmployee()

def exit():
    print("==============================================================")
    print("==================   PROGRAM SHUTDOWN    =====================")
    print("==============================================================")
    return False

main()



