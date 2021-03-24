import json
import os.path
import csv


pwd = os.path.dirname(os.path.realpath(__file__))


o = open(f"{pwd}/data.json")

data = json.load(o)
data = data["data"]
# print(data[1])
o.close()


# genovese.work@gmail.com
# https://github.com/vgenov-py/python_cice/blob/master/density.md
# Ejercicio 1: Obtender la densidad media de los municipios de Madrid
    
def densidad_media(lista):

    lenght = len(lista)
    count = 0

    for densidad in lista:
        count += densidad['densidad_por_km2']
    return count/lenght

# print(densidad_media(data))


# Ejercicio 2: Obtener municipio por codigo ine // Extra: utilizando función filter

def obtener_municipio(lista):
    ine_municipio = input('Introduce el Ine: ')
    for municipio in lista:
        if municipio ["municipio_codigo_ine"] == ine_municipio:
            return municipio

# print(obtener_municipio(data))

# Ejercicio 3: Obtener el municipio más grande

def municipio_mas_grande(lista):
    lista_superficies = []
    for elemento in lista:
        lista_superficies.append(elemento["superficie_km2"])
        #print(lista_superficies)

    

    # for municipio in lista:
    #     if municipio ["superficie_km2"] == max(municipio["superficie_km2"]):
    #         return municipio
    return max(lista_superficies)
    

# print(municipio_mas_grande(data))

# Ejercicio 4: Obtener los 10 municipios con mayor densidad poblacional

def top10_densidad(lista):
    lista_densidad = []
    lista_top10densidad = []
    for elemento in lista:
        lista_densidad.append(elemento["densidad_por_km2"])
    
    print(len(lista_densidad))
    count = 0
    while count != 10:
        for v in range(0, 10):
            x = max(lista_densidad)
            lista_top10densidad.append(x)
            lista_densidad.pop(lista_densidad.index(x))
            count += 1
    return lista_top10densidad
    
# print(top10_densidad(data))

# Ejercicio Bonus: Crea una función que reciba como parametro el dataset y devuelva tres listas con la siguiente condición:

    # la lista 1 tendrá todos los valores de densidad que empiecen por 1
    # la lista 2 tendrá todos los valores de densidad que empiecen por 2 ej: lista_1 = ["134324", "1354211", "349.34"]

def valores_1(lista):
    lista_densidad = []
    lista1 = []
    lista2 = []
    lista3 = []
    lista4 = []
    for elemento in lista:
        lista_densidad.append(elemento["densidad_por_km2"])

    for elemento in lista_densidad:
        if str(elemento).startswith('1'):
            lista1.append(elemento)
        elif str(elemento).startswith('2'):
            lista2.append(elemento)
        elif str(elemento).startswith('3'):
            lista3.append(elemento)
        elif str(elemento).startswith('4'):
            lista4.append(elemento)
    # return lista1, lista2, lista3

    porcentaje1 = len(lista1)*100/len(lista_densidad)
    porcentaje2 = len(lista2)*100/len(lista_densidad)
    porcentaje3 = len(lista3)*100/len(lista_densidad)
    porcentaje4 = len(lista4)*100/len(lista_densidad)
    return f"Lista 1: {len(lista1)}, porcentaje: {porcentaje1:.2f}\nLista 2: {len(lista2)}, porcentaje: {porcentaje2:.2f}\nLista 3: {len(lista3)}, porcentaje: {porcentaje3:.2f}\nLista 4: {len(lista4)}, porcentaje: {porcentaje4:.2f}"

# print(valores_1(data))


# Ejercicio 5: Crear una clase de tipo municipality/municipio

    # Debe tener tantas propiedas como claves en el diccionario

class Municipio:
    counter = 0
    total_population = 0
    anual_growth = 1.02

    def __init__ (self, municipio_nombre, densidad_por_km2, superficie_km2 ):
        self.municipio_nombre = municipio_nombre
        self.densidad_por_km2 = densidad_por_km2
        self.superficie_km2 = superficie_km2

        Municipio.total_population += self.population
        Municipio.counter += 1

# Ejercicio 18: Define un set_anual_growth que permita modificar la tasa de crecimiento

    def apply_anual_growth(self):
        delf.densidad *= Municipio.anual_growth

    @classmethod 
    def set_anual_growth(cls, value):
        cls.anual_growth = value


# Ejercicio 16: Convertir el método del ejercicio 10 en propiedad

    @property
    def population(self):
        return self.densidad_por_km2 * self.superficie_km2

    def __str__ (self):
        return f"\nNombre: {self.municipio_nombre}\nDensidad: {self.densidad_por_km2:.3f}\nSuperficie: {self.superficie_km2:.3f} "


# Ejercicio 7: Crear una función que acepte un solo parámetro (municipio) y que devuleva un objecto con las propiedades (nombre, densidad, superfice)

def municipio(nombre_municipio):
    list_municipio = []
    
    for mun in data:
        if mun['municipio_nombre'] == nombre_municipio:
            list_municipio.append(mun)
            nombre, densidad, superficie = list_municipio[0]['municipio_nombre'], list_municipio[0]['densidad_por_km2'], list_municipio[0]['superficie_km2']
            objeto_municipio = Municipio(nombre, densidad, superficie)
            return objeto_municipio
    return 'Este municipio no existe'

#print(municipio('Villalbilla'))


# Ejercicio 9: Crear una función que acepte como parámetro toda la lista de diccionarios y devuelva una lista de objetos


class Municipio2:
    def __init__ (self, municipio_codigo, densidad_por_km2, municipio_codigo_ine, nuts4_nombre, municipio_nombre, nuts4_codigo, superficie_km2 ):
        self.municipio_codigo = municipio_codigo
        self.densidad_por_km2 = densidad_por_km2
        self.municipio_codigo_ine = municipio_codigo_ine
        self.nuts4_nombre = nuts4_nombre
        self.municipio_nombre = municipio_nombre
        self.nuts4_codigo = nuts4_codigo
        self.superficie_km2 = superficie_km2

    # def __str__ (self):
    #     return f"\nCodigo del Municipio: {self.municipio_codigo}\nDensidad: {self.densidad_por_km2:.3f}\nCodigo Ine: {self.municipio_codigo_ine}\nZona: {self.nuts4_nombre}\nNombre: {self.municipio_nombre}\n Codigo Zona: {self.nuts4_codigo}\nSuperficie: {self.superficie_km2:.3f} "

def objetolistamunicipios(lista):
    lista_municipios = []

    for diccionario in lista:
        obj = Municipio2(diccionario['municipio_codigo'],
                        diccionario['densidad_por_km2'],
                        diccionario['municipio_codigo_ine'],
                        diccionario['nuts4_nombre'],
                        diccionario['municipio_nombre'],
                        diccionario['nuts4_codigo'],
                        diccionario['superficie_km2'])
        lista_municipios.append(obj)
    return lista_municipios


#print(objetolistamunicipios(data))
    

# Ejercicio 10: Considerando que en cada objeto tenemos la superficie y densidad ambas por km2, crear un MÉTODO (una función dentro del objeto) que devuelva la densidad total del municipio dado

def densidad_total_u(nombre_municipio):
    for mun in data:
        if mun['municipio_nombre'] == nombre_municipio:
            densidad = mun['densidad_por_km2']
            superficie_total = mun['superficie_km2']
            densidad_total = densidad * superficie_total
            return f'La densidad total es {densidad_total:.0f}'

#print(densidad_total_u('Villalbilla'))

# todos_municipios = [mun['municipio_nombre'] for mun in data]
# for i in todos_municipios:
#     print(densidad_total_u(i))


def densidad_madrid(lista):

    #lista_densidades = []
    lista_superficie = []
    lista_poblacion = []

    for mun in lista:
        poblacion = mun['densidad_por_km2'] * mun['superficie_km2']
        lista_superficie.append(mun['superficie_km2'])
        lista_poblacion.append(poblacion)

    poblacion_total = sum(lista_poblacion)
    densidad_t = poblacion_total / sum(lista_superficie)
    
    return f'La densidad total de Madrid es {densidad_t:.0f}'

# print(densidad_madrid(data))

# Ejercicio 13: Crea un classmethod llamado from_str que crea una instancia de la siguiente cadena --> "test-3.54-23.86"

@classmethod
def from_str(cls, string_):
    nombre, densidad, superficie = string_.split('-')
    densidad = float(densidad)
    superficie = float(superficie)
    return cls(nombre, densidad, superficie)

# Ejercicio 14: Estable una tasa de crecimiento anual del 2%
# Ejercicio 15: Define un método que aplique el crecimiento anual sobre un objeto

def crecimiento_anual(nombre_municipio):
    for mun in data:
        if mun['municipio_nombre'] == nombre_municipio:
            densidad = mun['densidad_por_km2']
            superficie_total = mun['superficie_km2']
            densidad_total = densidad * superficie_total
            crecimiento_anual_municipio = densidad_total * 0.02
            return f'El creciemiento anual es {crecimiento_anual_municipio:.0f}'

#print(crecimiento_anual('Villalbilla'))

# fichero = open(f'{pwd}/fichero.csv','a')

test_object = objetolistamunicipios(data)
# print(test_object)


with open(f'{pwd}/fichero.csv' , 'w', newline='') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(['Nombre', 'Densidad', 'Superficie'])
    csv_writer.writerow([test_object.municipio_nombre, test_object.densidad_por_km2, test_object.superficie_km2])
    
