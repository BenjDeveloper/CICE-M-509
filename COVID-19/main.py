import requests as req
import json

response = req.get('https://datos.comunidad.madrid/catalogo/dataset/7da43feb-8d4d-47e0-abd5-3d022d29d09e/resource/ead67556-7e7d-45ee-9ae5-68765e1ebf7a/download/covid19_tia_muni_y_distritos.json').json()

# print(response.content)

with open("COVID-19/fichero.json", 'w') as file:
    json.dump(response, file)



def cantidad_municipios():

    lista_municipios = []
    for element in response:
        lista_municipios.append(element['municipio_distrito'])

print(cantidad_municipios)  