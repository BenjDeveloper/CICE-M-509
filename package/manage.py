from .department import Department
import csv
import os
from os import remove
from os import path
import re



class ManageLadder:
    

    #===============================================================================================
    #==================================   CRUD DEPARTAMENTOS   =====================================
    #===============================================================================================
    def createDepartment(self):
        """
        This method allow us create a new department
        if it doesnt exist yet   
        """
        nameDepartment = ['.csv']
        while True:
            newDepartment = input("Introduzca el nombre del departamento: ")
            nameDepartment.insert(0, newDepartment)
            newDepartmentExtension = ''.join(nameDepartment)
            try:
                department_file = open(f'DATABASE/{newDepartmentExtension}', 'x')
            except FileExistsError:
                del nameDepartment[0]
                print("El departamento ya existe")
            else:
                telephone_number = int(input("Introduzca el telefono: "))
                attributeDepartment = [newDepartment, str(telephone_number)]
                department = Department(newDepartment, telephone_number)
                data_to_save_in_csv_file = ','.join(attributeDepartment)
                print(data_to_save_in_csv_file)
                if os.stat('DATABASE/DEPARTMENTS.csv').st_size == 0:
                    csv_file = open('DATABASE/DEPARTMENTS.csv', 'a')
                    csv_file.write(f"{data_to_save_in_csv_file}")
                    csv_file.close()
                else:
                    csv_file = open('DATABASE/DEPARTMENTS.csv', 'a')
                    csv_file.write(f"\n{data_to_save_in_csv_file}")
                    csv_file.close()
                print(f"El departamento {newDepartment} ha sido creado exitosamente")                
                return newDepartmentExtension
    
    def readDepartment(self):
        if os.stat('DATABASE/DEPARTMENTS.csv').st_size == 0:
            print('No hay departamentos')
        else:
            department_file = open('DATABASE/DEPARTMENTS.csv', 'r')
            file_d = csv.reader(department_file)
            print("DEPARTAMENTO","\t\t", "TELEFONO")
            print("----------------------------------")
            for index_d, i in enumerate(file_d, start=1):
                if len(i[0]) <= 10:
                    print(f"{index_d}._{i[0]}", "\t\t", i[1])
                else:
                    print(f"{index_d}._{i[0]}", "\t", i[1])
            department_file.close()
    

    def updateDepartment(self):
        if os.stat('DATABASE/DEPARTMENTS.csv').st_size == 0:
            print('No hay ningun departamento')
        else:
            item_list_department = []   
            obj = ManageLadder()
            obj.readDepartment()
            department_file = open("DATABASE/DEPARTMENTS.csv", 'r')
            file_d = csv.reader(department_file)
            list_department = [i[0] for i in file_d]
            department_file.close()
            department_file = open("DATABASE/DEPARTMENTS.csv", 'r')
            file_d = csv.reader(department_file)
            list_department_tel = [i[1] for i in file_d]
            department_file.close()

            lenght_list = len(list_department)
            print("Introduzca el número del departamento que desea eliminar/actualizar")
            number_deparment = obj.checkNumber(lenght_list)
            number_deparment = number_deparment - 1
            
            department_file = open("DATABASE/DEPARTMENTS.csv", 'r')
            file_d = department_file.readlines()
            l = [i for i in file_d if i.__contains__(list_department[number_deparment])]
            department_file.close()
            l_item = l[0].split(',')
            item_input = ['nombre del departamento', 'telefono del departamento']
            department_name, department_tel = l_item[0], l_item[1]

            new_department_list = list_department.copy()
            new_department_list_tel = list_department_tel.copy()
            new_department_list.pop(new_department_list.index(new_department_list[number_deparment]))
            new_department_list_tel.pop(new_department_list_tel.index(new_department_list_tel[number_deparment]))
            for i in item_input:
                choice = input(f"Quieres actualizar el {i} (y/n): ")
                if choice == 'y':
                    if i == item_input[0]:
                        department_name = obj.checkDeparmentName(new_department_list)
                    elif i == item_input[2]:
                        department_tel = obj.checkDeparmentTelephone(new_department_list_tel)
                else:
                    pass
            attributeDepartment = [department_name, str(department_tel)]
            data_to_save_in_csv_file = ','.join(attributeDepartment)
            department_file = open("DATABASE/DEPARTMENTS.csv", 'r')
            file_line = department_file.readlines()
            department_file.close()
            department_file = open("DATABASE/DEPARTMENTS.csv", 'w')
            for line in file_line:
                if list_department[number_deparment] not in line:
                    department_file.write(line)              
            department_file.close()
            csv_file = open('DATABASE/DEPARTMENTS.csv', 'a')
            csv_file.write(f"\n{data_to_save_in_csv_file}")
            csv_file.close()
            print(f"El departamento {department_name} ha sido actualizado")   

    def checkDeparmentName(self, list_department_name):
        while True:
            department_name = input("Introduzca el nuevo nombre del departamento: ")
            if department_name in list_department_name:
                print("El nombre introducido ya existe, intentelo de nuevo")
            else:
                return department_name
    
    def checkDeparmentTelephone(self, list_department_telephone):
        while True:
            department_tel = input("Introduzca el nuevo número del departamento: ")
            if department_tel in list_department_telephone:
                print("Ya hay un departamento utilizando ese número, intentelo de nuevo")
            else:
                try:
                    department_tel = int(department_tel)
                except ValueError:
                    print("El valor introducido no es válido")
                else:
                    if len(department_tel) != 9:
                        print("debe introducir un número de nueve digitos")
                    else:
                        return department_tel

    def checkNumber(self, lenght_list):
        while True:
            number_deparment = input("aqui: ")
            try:
                number_deparment = int(number_deparment)
            except ValueError:
                print('El valor introducido no es válido')
            else:
                if (number_deparment < 1) or (number_deparment > lenght_list):
                    print(f"debe introducir un valor de 1 a {lenght_list}")
                elif 1 <= number_deparment <= lenght_list:
                    return number_deparment


    def deleteDepartment(self):
        if os.stat('DATABASE/DEPARTMENTS.csv').st_size == 0:
            print('No hay ningun departamento')
        else:   
            obj = ManageLadder()
            obj.readDepartment()
            department_file = open("DATABASE/DEPARTMENTS.csv", 'r')
            file_d = csv.reader(department_file)
            list_department = [i[0] for i in file_d]
            department_file.close()
            lenght_list = len(list_department)
            print("Introduzca el número del departamento que desea eliminar/actualizar")
            number_deparment = obj.checkNumber(lenght_list)
            number_deparment = number_deparment - 1
            department_file = open("DATABASE/DEPARTMENTS.csv", 'r')
            file_line = department_file.readlines()
            department_file.close()
            department_file = open("DATABASE/DEPARTMENTS.csv", 'w')
            for line in file_line:
                if list_department[number_deparment] not in line:
                    department_file.write(line)              
            department_file.close()
            #if path.exists('')
            print(f"El departamento {list_department[number_deparment]} ha sido eliminado exitosamente")
    

    #===============================================================================================
    #====================================   CRUD EMPLEADO   ========================================
    #===============================================================================================    
    def checkDNI(self, list_employee):
        while True:
            employee_DNI = input("Introduzca el DNI: ")
            if employee_DNI in list_employee:
                print("El DNI introducido ya está en uso")
            else:
                return employee_DNI
    
    def verifierEmail(self):
        patrones = '[A-z0-9]{4,22}[@][a-z]+[.][a-z]{2,3}'
        while True:
            email = input("Introduce tu E-mail: ")
            if re.match(patrones, email):
                return email
            else:
                print("El correo introducido no es valido")
    
    def choiceDepartment(self):
        nameDepartment = ['.csv']
        obj = ManageLadder()
        obj.readDepartment()
        department_file = open("DATABASE/DEPARTMENTS.csv", 'r')
        file_d = csv.reader(department_file)
        list_department = [i[0] for i in file_d]
        department_file.close()
        lenght_list = len(list_department)
        print("Introduzca el número del departamento \ncuyos empleados deseas ver/actualizar/crear/eliminar")
        choice = obj.checkNumber(lenght_list)
        choice = choice - 1
        nameDepartment.insert(0, list_department[choice])
        chosenDepartment = ''.join(nameDepartment)
        return chosenDepartment

    def createEmployee(self):
        obj = ManageLadder()
        item_employee = ['nombre', 'apellido', 'DNI', 'E-MAIL', 'CLAVE', 'SALARIO', 'HORARIO']
        employee_name, employee_last_name, employee_email, employee_key, employee_salary, employee_schedule, employee_DNI = 'a','b','c','d','e','f','g'
        chosenDepartment = obj.choiceDepartment()
        department_file = open(f"DATABASE/{chosenDepartment}", "r")
        file_d = csv.reader(department_file)
        list_employee = [i[2] for i in file_d]
        department_file.close()
        for employee_info in item_employee:
            if employee_info == 'nombre':
                employee_name = input(f"Introduzca el {employee_info}: ")
            elif employee_info == 'apellido':
                employee_last_name = input(f"Introduzca el {employee_info}: ")
            elif employee_info == 'DNI':
                employee_DNI = obj.checkDNI(list_employee)
            elif employee_info == 'E-MAIL':
                employee_email = obj.verifierEmail()
            elif employee_info == 'CLAVE':
                employee_key = input(f"Introduzca el {employee_info}: ")
            elif employee_info == 'SALARIO':
                employee_salary = input(f"Introduzca el {employee_info}: ")
            elif employee_info == 'HORARIO':
                employee_schedule = input(f"Introduzca el {employee_info}: ")
        employee_data_list = [employee_name, employee_last_name, employee_DNI, employee_email, employee_key, employee_salary, employee_schedule]
        employee_data_joined = ','.join(employee_data_list)
        if os.stat(f'DATABASE/{chosenDepartment}').st_size == 0:
            department_file = open(f"DATABASE/{chosenDepartment}", "a")
            department_file.write(f"{employee_data_joined}")
            department_file.close()
        else:
            department_file = open(f"DATABASE/{chosenDepartment}", "a")
            department_file.write(f"\n{employee_data_joined}")
            department_file.close()
        print(f"El empleado {employee_name} ha sido creado exitosamente")

    def readEmployee(self):
        obj = ManageLadder()
        chosenDepartment = obj.choiceDepartment()
        if os.stat(f'DATABASE/{chosenDepartment}').st_size == 0:
            print("Este departamento no tiene ningun empleado")
        else:
            department_file = open(f"DATABASE/{chosenDepartment}", "r")
            file_d = csv.reader(department_file)
            print("  ","EMPLEADO","\t","DNI","\t\t","E-MAIL")
            print("------------------------------------------------")
            for index_em, employee_info in enumerate(file_d, start=1):
                if len(employee_info[0]) < 5:
                    print(f"{index_em}._{employee_info[0]}\t\t{employee_info[2]}\t{employee_info[3]}")
                else:
                    print(f"{index_em}._{employee_info[0]}\t{employee_info[2]}\t{employee_info[3]}")
            department_file.close()
            

    def updateEmployee(self):
        obj = ManageLadder()
        chosenDepartment = obj.choiceDepartment()
        if os.stat(f'DATABASE/{chosenDepartment}').st_size == 0:
            print("Este departamento no tiene ningun empleado")
        else:
            item_list_employee = []
            obj.readEmployee()
            employee_file = open(f"DATABASE/{chosenDepartment}", "r")
            file_emp = csv.reader(employee_file)
            employee_list = [i[0] for i in file_emp]
            employee_file.close()
            employee_file = open(f"DATABASE/{chosenDepartment}", "r")
            file_emp = csv.reader(employee_file)
            employee_DNI_list = [i[0] for i in file_emp]
            employee_file.close()

            lenght_list = len(employee_list)
            employee_number = obj.checkNumber(lenght_list)
            employee_number = employee_number - 1

            employee_file = open(f"DATABASE/{chosenDepartment}", "r")
            file_emp = employee_file.readlines()
            l = [i for i in file_emp if i.__contains__(employee_list[employee_number])]
            employee_file.close()
            l_item = l[0].split(',')
            item_input = ['Nombre', 'Apellido', 'DNI', 'E-mail', 'Clave', 'Salario', 'Horario']
            employee_name, employee_last_name, employee_DNI, employee_email, employee_key, employee_salary, employee_schedule = l_item[0],l_item[1],l_item[2],l_item[3],l_item[4],l_item[5],l_item[6]
            
            new_employee_DNI_list = employee_DNI_list.copy()
            new_employee_DNI_list.pop(new_employee_DNI_list.index(new_employee_DNI_list[employee_number]))
            for i in item_input:
                choice = input(f"Quieres actualizar {i} (y/n): ")
                if choice == 'y':
                    if i == item_input[0]:
                        employee_name = input(f"Introducir {i}: ")
                    elif i == item_input[1]:
                        employee_last_name = input(f"Introducir {i}: ")
                    elif i == item_input[2]:
                        employee_DNI = obj.checkDNI(new_employee_DNI_list)
                    elif i == item_input[3]:
                        employee_email = input(f"Introducir {i}: ")
                    elif i == item_input[4]:
                        employee_key = input(f"Introducir {i}: ")
                    elif i == item_input[5]:
                        employee_salary = input(f"Introducir {i}: ")
                    elif i == item_input[6]:
                        employee_schedule = input(f"Introducir {i}: ")
                else:
                    pass

            attributeEmployee = [employee_name, employee_last_name, employee_DNI, employee_email, employee_key, employee_salary, employee_schedule]      
            data_to_save = ','.join(attributeEmployee)
            employee_file = open(f"DATABASE/{chosenDepartment}", "r")
            employee_line = employee_file.readlines()
            employee_file.close()
            employee_file = open(f"DATABASE/{chosenDepartment}", "w")
            for employee_l in employee_line:
                if employee_list[employee_number] not in employee_l:
                    employee_file.write(employee_l)
            employee_file.close()
            employee_file = open(f"DATABASE/{chosenDepartment}", "a")
            employee_file.write(f"\n{data_to_save}")
            employee_file.close()
            print(f"El empleado {employee_name} ha sido actualizado") 



    def deleteEmployee(self):
        obj = ManageLadder()
        chosenDepartment = obj.choiceDepartment()
        if os.stat(f'DATABASE/{chosenDepartment}').st_size == 0:
            print("Este departamento no tiene ningun empleado")
        else:
            obj.readEmployee()
            employee_file = open(f'DATABASE/{chosenDepartment}', 'r')
            employee_data = csv.reader(employee_file)
            employee_list = [i[0] for i in employee_data]
            employee_file.close()
            lenght_list = len(employee_list)
            print("Introduzca el número del empleado que desea eliminar/actualizar")
            employee_number = obj.checkNumber(lenght_list)
            employee_number = employee_number - 1
            employee_file = open(f"DATABASE/{chosenDepartment}", "r")
            employee_line = employee_file.readlines()
            employee_file.close()
            employee_file = open(f"DATABASE/{chosenDepartment}", "w")
            for employee_l in employee_line:
                if employee_list[employee_number] not in employee_l:
                    employee_file.write(employee_l)
            employee_file.close()
            print(f"El empleado {employee_list[employee_number]} ha sido eliminado exitosamente")


        
        
















