
# EJEMPLO DE MANEJO  DE REPOSITORIOS Y CLASES POR MEDIO DE PAQUETES

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
        empleado = Empleado( fila[0], fila[1], fila[2], fila[3], fila[4], fila[5], fila[6], fila[7], fila[8], fila[9])
        lista.append(empleado)


    departamento_calidad = Departamento ('calidad', '987654321', lista)
    departamento_calidad.sort( )
    print (departamento_calidad)

    fichero.close()




main()
















#media_salarial (empleados.departamento_calidad)

# peliador = Peliador('Canelo', 80, 30, '12634784') # instancia de Peliador
# temporal = Temporal()
# coach =  Entrenador('Reinoso', '533564232')
# print (peliador)
# print('ANTES DE LA ASIGNACION')
# print(peliador.entrenador)
# print(temporal.entrenador)

# peliador.entrenador = coach
# temporal.entrenador = coach

# print('DESPUES DE LA ASIGNACION')
# print(peliador.entrenador)
# print(temporal.entrenador)

# # coach.nombre = 'envander'             # edicion del objeto desde el mismo
# #temporal.entrenador.nombre = 'Nicole'  # edicion del objeto desde una referencia - instancia ( temporal )
# peliador.entrenador.nombre = 'Veronica' # edicion del objeto desde una referencia - instancia ( peliador )

# print('DESPUES DE LA EDICION DE NOMBRE')
# print(peliador.entrenador)
# print(temporal.entrenador)




















#?File "/Users/patricia/Desktop/practicas_cice/CICE-M-509/main.py", line 4, in <module>
    #?from persona import Persona
#?ModuleNotFoundError: No module named 'persona'

