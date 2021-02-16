

#IMPORTACION DE LA CLASE PERSONA,USUARIO,EMPLEADO Y DEPARTAMENTO
from package.persona import Persona
from package.usuario import Usuario
from package.empleado import Empleado
from package.departamento import Departamento
import csv

#FUNCION MAIN
def main():

    #LECTURA DEL ARCHIVO 
    path = '/Users/veronica/Documents/GitHub/CICE-M-509'
    fichero = open( path+'/fichero.csv', 'r')

    lectura = csv.reader(fichero) 
    lista = [] 
    for fila in lectura:
        print(fila)
        empleado = Empleado( fila[0], fila[1], fila[2], fila[3], fila[4], fila[5], fila[6], fila[7], fila[8], fila[9])
        lista.append(empleado)

    #CREACION DEL MENU
    #ESCRITURA DEL ARCHIVO 
    fichero = open( path+'/fichero.csv', 'a')
    nombre = input ('Agregar nombre: ')
    apellido = input ('Agregar apellido: ')
    fecha_nacimiento = input ('Agregar fecha de nacimiento: ')
    dni = input ('Agregar DNI: ')
    direccion = input ('Agregar direccion: ')
    mail = input ('Agregar mail: ')
    clave = input ('Agregar clave: ')
    activo = True
    salario = input ('Agregar salario: ')
    horario = input ('Agregar horario: ')
    fichero.write(f'{nombre},{apellido},{fecha_nacimiento},{dni},{direccion},{mail},{clave},{True},{salario},{horario}')

    

    
    
    '''#EMPLEADOS Y DEPARTAMENTOS
    departamento_programacion = Departamento('Programación Python', '911652637', [emp0,emp1,emp2,emp3,emp4,emp5,emp6,emp7,emp8])

    print(f'Media: {departamento_programacion.media_salarial():.2f}\n')
    print(f'Reporte salarial del departamento "{departamento_programacion.nombre}" ordenado de mayor a menor salario:\n{departamento_programacion.reporte_salarios()}')'''

    fichero.close()

main()

