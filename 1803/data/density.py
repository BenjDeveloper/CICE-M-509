import json
import os.path
pwd = os.path.dirname(os.path.realpath(__file__))
o = open(f"{pwd}/data.json")

data = json.load(o)
data = data["data"]
# print(data[1])
o.close()

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
    return f"Lista 1: {len(lista1)}, porcentaje: {porcentaje1}\nLista 2: {len(lista2)}, porcentaje: {porcentaje2}\nLista 3: {len(lista3)}, porcentaje: {porcentaje3}\nLista 4: {len(lista4)}, porcentaje: {porcentaje4}"

print(valores_1(data))


# Ejercicio 5: Crear una clase de tipo municipality/municipio

    # Debe tener tantas propiedas como claves en el diccionario

class Municipio:
    def __init__ (self, municipio_nombre, densidad_por_km2, superficie_km2 ):
        self.municipio_nombre = municipio_nombre
        self.densidad_por_km2 = densidad_por_km2
        self.superficie_km2 = superficie_km2

    def __str__ (self):
        return f"\nNombre: {self.municipio_nombre}\nDensidad: {self.densidad_por_km2}\nSuperficie: {self.superficie_km2} "


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

print(municipio('Villalbilla'))
