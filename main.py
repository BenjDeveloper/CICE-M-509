
# EJEMPLO DE MANEJO  DE REPOSITORIOS Y CLASES POR MEDIO DE PAQUETES
from package.employee import Employee
from package.department import Department
from package.managaError import ManageError
from package.manage import ManageLadder
from header import header
import csv

def main():
    header()
    
                
    #print("1._Administrar departamentos \n2._Administrar Empleados")
    #option = int(input("Eliga una option: "))

    #data_file = open('data_file.csv', 'a')
    #read_data_file = csv.reader(data_file)
    #for i in read_data_file:
    #   print(i)
    #data_file.writelines('\nKalaella,davos,F-010105-M,davos@gmail.com,deRitio,60000,14PM')
    #data_file1 = open('DATABASE/HHRR.csv', 'w')
    
    ma = ManageLadder()
    ma.deleteDepartment()


main()



