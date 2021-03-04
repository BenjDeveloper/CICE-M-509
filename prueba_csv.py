import csv

class Jugadores:
    def __init__(self, nombre, pais):
        self.nombre = nombre
        self.pais = pais
    def __str__(self):
        return f'{self.nombre} , {self.pais}'


lista_jugadores = []


fichero = open('C:/Users/cice.AULA4POV14S/Documents/CICE-M-509/prueba.csv', 'r')

lectura = csv.reader(fichero)

for fila in lectura:
    jugad = Jugadores(fila[0], fila[1])
    lista_jugadores.append(jugad)
    print(jugad)
    # print(fila[0])
    # print(fila[0], fila[1])

# print(lista_jugadores)
fichero.close()

# # lista_jugadores.append(Jugadores('Federer', 'Suiza'))
# # lista_jugadores.append(Jugadores('Djokovic', 'Serbia'))
# # lista_jugadores.append(Jugadores('Monfils', 'Francia'))


# fichero = open('C:/Users/cice.AULA4POV14S/Videos/prueba_2.csv', 'w')

# primera_linea = True
# for jugador in lista_jugadores:
#     cadena = ''
#     if primera_linea == True:
#         cadena = f'{jugador.nombre}, {jugador.pais}'
#         primera_linea = False
#     else:
#         cadena = f'/n{jugador.nombre}, {jugador.pais}'
#     fichero.write(cadena)

# fichero.close()