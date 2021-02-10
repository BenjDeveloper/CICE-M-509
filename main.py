
# EJEMPLO DE MANEJO  DE REPOSITORIOS Y CLASES POR MEDIO DE PAQUETES
from package.persona import Persona

from package.persona import Persona
from package.empleado import Empleado
from package.departamento import Departamento

def main():

    # empleado_1 = Empleado ('Federico', 'Martinez',' 18-02-1987', '223647114T', 'povedilla', 'federico@gmail.com','jfjfur123', True, 42000, 'partido')
    # empleado_1 = Empleado ('Federico', 'Martinez',' 18-02-1987', '223647114T', 'povedilla', 'federico@gmail.com','jfjfur123', True, 42000, 'partido')
    # empleado_2 = Empleado ('Nacho', 'Sevillano', '19-07-1985', '12347828K', 'marques de zafra', 'nachete@gmail.com', '12345', True, 95000, 'mañana')
    # empleado_3 = Empleado ('Benja', 'lopez', '1-10-1975', '17647145K', 'sancho davila 39', 'benjamito@gmail.com', '67584', True, 45000, 'mañana')
    # empleado_4 = Empleado ('Gorka', 'bilbao', '29-11-1998', '123458765H', 'peñascales 14', 'gorki@gmail.com', '9875766', True, 120000, 'partido')
    # empleado_5 = Empleado ('Rosa ', 'melano', '14-07-1985', '123484567P', 'Sepulveda 80', 'ana@gmail.com', '12678', True, 420000, 'tarde')
    # empleado_6 = Empleado ('Elber', 'galarga', '12-01-1986', '12398778L', 'corredera 10', 'eva@gmail.com', '129889', True, 55000, 'tarde')
    # empleado_7 = Empleado ('Marina', 'jimenez',' 15-09-67', '22765894T', 'lanuza 11', 'antonio@gmail.com','123423', True, 40000, 'partido')
    # empleado_8 = Empleado ('Elena', 'rincon', '08-05-1980', '12345678K', 'arroyo 30', 'elena@gmail.com', '98745', True, 50000, 'mañana')
    # empleado_9 = Empleado ('Mariano', 'rojo', '18-10-1990', '98756045K', 'la paz 99', 'mariano@gmail.com', '98764', True, 45000, 'tarde')
    # empleado_10 = Empleado('Luis', 'sanz', '29-12-1999', '123498675H', 'pinar 30', 'luis@gmail.com', '7658476', True, 30000, 'partido')

    # x =  [empleado_1, empleado_2, empleado_3, empleado_4, empleado_5, empleado_6, empleado_7, empleado_8, empleado_9, empleado_10   ]

    departamento_calidad = Departamento ('calidad', '987654321', x)

    departamento_calidad.sort( )

    print (departamento_calidad)


    path = 'C:/Users/cice/Pictures/Screenshots/CICE-M-509/CICE-M-509-1'
    fichero = open( path+'/fichero.csv', 'w')

    lectura =csv.reader(fichero)
    lista=[]
    for fila in lectura:
        print(fila)
        empleado = Empleado(fila[0],fila[1],fila[2],fila[3],fila[4],fila[5],fila[6],fila[7])

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

