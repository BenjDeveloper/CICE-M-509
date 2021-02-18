
# EJEMPLO DE MANEJO  DE REPOSITORIOS Y CLASES POR MEDIO DE PAQUETES

from package.persona import Persona
from package.empleado import Empleado
from package.departamento import Departamento
from package.gerencia import Gerencia # importamos la clase nueva llamada gerencia
import csv


def guardaEmpleadoList(path, name_file, lista):
    
    fichero = open( path + name_file, 'a')
    
    fichero.write(f'{lista[0]},{lista[1]},{lista[2]},{lista[3]},{lista[4]},{lista[5]},{lista[6]},{lista[7]},{lista[9]},{lista[10]}\n')
    
    fichero.close()

def guardaEmpleadoInput(path, name_file):
    
    fichero = open( path + name_file, 'a')
    
    nombre = input('Agregar nombre: ')
    apellido = input('Agregar apellid0: ')
    fecha_de_nacimiento = input('Agregar Fec. Nac.: dd-mm-yyyy : ')
    dni = input('Agregar DNI: ')
    direccion = input('Agregar direccion: ')
    email = input('Agregar email: ')
    clave = input('Agregar clave: ')
    activo = True
    salario = input('Agregar Salario (Solo Numeros): ')
    horario = input('Agregar Horario (partido, tiempo completo)')
    
    fichero.write(f'{nombre},{apellido},{fecha_de_nacimiento},{dni},{direccion},{email},{clave},{activo},{salario},{horario}\n')
    
    fichero.close()

def ver_informacion(dic_departamentos):
    print()
    for nombre_depart, depar in dic_departamentos.items():
        print(nombre_depart)
        for emple in depar.empleados:
            print(nombre_depart,emple)
    print()




def cargar_gerencia(nombre):
    gerencia = Gerencia(nombre):
    return gerencia

def cargar_departamenos(path, name_file):
    fichero = open( path + name_file, 'r')

    lista_filas_CSV = csv.reader(fichero) 

    dic_departamentos = {} 

    for fila in lista_filas_CSV:
        nombre_depart = fila[0]
        departamento = Departamento( fila[0], fila[1])
        dic_departamentos[nombre_depart] = departamento

    fichero.close()
    return dic_departamentos   

def cargar_empleados(path, file_empleados, file_departamentos):
    fichero = open( path + file_empleados, 'r')
    lista_filas_CSV = csv.reader(fichero) 

    dic_departamentos = cargar_departamenos(path,file_departamentos)
    
    for fila in lista_filas_CSV:
        nombre_depart = fila[10]
        empleado = Empleado( fila[0], fila[1], fila[2], fila[3], fila[4], fila[5], fila[6], fila[7], fila[8], fila[9])
        dic_departamentos[nombre_depart].empleados.append(empleado)

    ver_informacion(dic_departamentos)

    fichero.close()
    return dic_departamentos

def main():
    path = '/Users/benjaminpenaloza/Dropbox/Mi Mac (MacBook Pro de Benjamin)/Documents/MyWorkspace/CICE-M-509'
    file_empleados = '/fichero_empleados.csv'
    file_departamentos = '/fichero_departamentos.csv'
    
    #! CARGA GLOBAL
    gerencia = cargar_gerencia('McDonals')
    gerencia.lista_departametos = cargar_empleados(path, file_empleados, file_departamentos) 

main()




#! PARTE 1
# {
#     'calidad': [<package.empleado.Empleado object at 0x7fa3fc239ca0>], 
#     'RRHH': [<package.empleado.Empleado object at 0x7fa3fc238370>], 
#     'prevencion': [<package.empleado.Empleado object at 0x7fa3fc238610>], 
#     'IT': [<package.empleado.Empleado object at 0x7fa3fc2385e0>]
# }

#! PARTE 2
# {
#     'calidad': [<package.empleado.Empleado object at 0x7fc437a2fca0>], 
#     'RRHH': [<package.empleado.Empleado object at 0x7fc437a2e370>], 
#     'prevencion': [<package.empleado.Empleado object at 0x7fc437a2e610>], 
#     'IT':   [<package.empleado.Empleado object at 0x7fc437a2e5e0>, 
#             <package.empleado.Empleado object at 0x7fc437a2e640>, 
#             <package.empleado.Empleado object at 0x7fc437a2d670>]
# }

#! PARTE 3 - ESTRUCTURA AUXILIAR PARA ORDENAR LOS EMPLEADOS SEGUN SU DEPARTAMENTO
# {
#     'calidad': [], 
#     'RRHH': [], 
#     'prevencion': [], 
#     'IT':   []
# }

#! PARTE 4
# Gerencia
#     nombre_empresa : str
#     lista_departamentos :   {
#                                 Departamento.nombre : Departamento
#                                                                 nombre:str  
#                                                                 telefono:str
#                                                                 lista_empleados:[e1,e2,e3...en]

#                                 'calidad' : Departamento_1 - objectos
#                                 'RRHH': Departamento:_2, 
#                                 'prevencion': Departamento_3, 
#                                 'IT':   Departamento_4
#                             }



