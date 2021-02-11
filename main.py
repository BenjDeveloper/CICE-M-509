

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

    '''#ESCRITURA DEL ARCHIVO 
    fichero = open( path+'/fichero.csv', 'a')
    fichero.write(f'Patricia,Herresanchez,13-08-1993,36476888S,Segovia,patrihf@gmail.com,44raton55,True,1401.5,8:00-15:30')'''
    

    
    
    #EMPLEADOS Y DEPARTAMENTOS
    departamento_programacion = Departamento('Programación Python', '911652637', [emp0,emp1,emp2,emp3,emp4,emp5,emp6,emp7,emp8])

    print(f'Media: {departamento_programacion.media_salarial():.2f}\n')
    print(f'Reporte salarial del departamento "{departamento_programacion.nombre}" ordenado de mayor a menor salario:\n{departamento_programacion.reporte_salarios()}')

    fichero.close()

main()

