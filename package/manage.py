from .department import Department
import csv
import os



class ManageLadder:
    def __init__(self):
        pass

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
            for index_d, i in enumerate(file_d, start=1):
                print(f"{index_d}._{i[0]}", "\t", i[1])
            department_file.close()
    
    def updateDepartment(self):
        pass
    

    def deleteDepartment(self):
        if os.stat('DATABASE/DEPARTMENTS.csv').st_size == 0:
            print('No hay ningun departamento')
        else:
            department_file = open("DATABASE/DEPARTMENTS.csv", 'r')
            file_d = csv.reader(department_file)
            print(dir(file_d))

        
        
















