
# EJEMPLO DE MANEJO  DE REPOSITORIOS Y CLASES POR MEDIO DE PAQUETES
from package.persona import Persona

from package.persona import Persona
from package.empleado import Empleado
from package.departamento import Departamento
import csv

def main():
    path = '/Users/benjaminpenaloza/Dropbox/Mi Mac (MacBook Pro de Benjamin)/Documents/MyWorkspace/CICE-M-509'
    fichero = open( path+'/fichero.csv', 'r')

    lectura = csv.reader(fichero) 
    lista = [] 
    for fila in lectura:
        print(fila)
        empleado = Empleado( fila[0], fila[1], fila[2], fila[3], fila[4], fila[5], fila[6], fila[7], fila[8], fila[9])
        lista.append(empleado)


    departamento_calidad = Departamento ('calidad', '987654321', lista)
    departamento_calidad.sort( )
    print (departamento_calidad)

    fichero.close()

main()


