
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

def cargarEmpleados(path, name_file):
    fichero = open( path + name_file, 'r')

    lista_filas_CSV = csv.reader(fichero) 

    dic_empleados = {}
    tag_departamenos = ['calidad', 'RRHH', 'prevencion', 'IT']
    for tag in tag_departamenos:
        dic_empleados[tag]=[]
    
    for fila in lista_filas_CSV:

        nombre_depart = fila[10]
        empleado = Empleado( fila[0], fila[1], fila[2], fila[3], fila[4], fila[5], fila[6], fila[7], fila[8], fila[9])
        dic_empleados[nombre_depart].append(empleado)

    print()
    for key, lista in dic_empleados.items():
        for ele in lista:
            print(key,ele)
    print()
    
    fichero.close()
    return dic_empleados

def main():
    path = '/Users/benjaminpenaloza/Dropbox/Mi Mac (MacBook Pro de Benjamin)/Documents/MyWorkspace/CICE-M-509'

    #! EMPLEADOS
    name_file = '/fichero.csv'
    # guardaEmpleadoInput(path, name_file)
    dic_empleados = cargarEmpleados(path, name_file) 

    #! DEPARTAMENTOS
    # departamento_calidad = Departamento ('Calidad', '987654321', lista_empleados)

    #! GERENCIA
    # gerencia_corte_ingles = Gerencia('Corte Ingles S.A.')
    # gerencia_corte_ingles.lista_departametos.append( departamento_calidad )

main()


