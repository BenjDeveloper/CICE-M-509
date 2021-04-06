import requests as req
import json

# response = req.get('https://datos.comunidad.madrid/catalogo/dataset/7da43feb-8d4d-47e0-abd5-3d022d29d09e/resource/ead67556-7e7d-45ee-9ae5-68765e1ebf7a/download/covid19_tia_muni_y_distritos.json').json()

# print(response.content)

# with open("COVID-19/fichero.json", 'w') as file:
#     json.dump(response, file)

def total_municipality():
    with open('COVID-19/fichero.json', 'r') as data:    
            lectura = json.load(data)
            print(lectura['data'][0])

            contador = 0
            for municipio in lectura['data']:
                if municipio['municipio_distrito'] == 'Valdemorillo':
                    contador += 1
            print(f'El total de municipios es: {25237/contador:.0f}')

def get_tia_final():
    with open('COVID-19/fichero.json', 'r') as data:    
        lectura = json.load(data)
        lista_casos = []
        # contador = 0
        for municipio in lectura['data'][:199]:
            # if contador <= 198:
            try:
                assert 'casos_confirmados_totales' in list(municipio.keys())
            except AssertionError:
                pass
            else:
                lista_casos.append(municipio['casos_confirmados_totales'])
                # contador += 1
        print(f'La TIA final es: {sum(lista_casos)}')



def get_tia_inicial():
    with open('COVID-19/fichero.json', 'r') as data:    
        lectura = json.load(data)
        lista_casos = []
        # contador = 0
        for municipio in lectura['data'][-200:-1]:
            # if contador <= 198:
            try:
                assert 'casos_confirmados_totales' in list(municipio.keys())
            except AssertionError:
                pass
            else:
                lista_casos.append(municipio['casos_confirmados_totales'])
                # contador += 1
                # total = sum(lista_casos)
        print(f'La TIA inicial es: {sum(lista_casos)}')

def fecha():
    with open('COVID-19/fichero.json', 'r') as data:    
        lectura = json.load(data)
        lista_fecha = []
        contador = 0
        for municipio in lectura['data']:
            if municipio['fecha_informe'] == f"2020/02/{26} 07:00:00":
                contador += 1
                lista_fecha.append(contador)

# def tia_diaria():
#     with open('COVID-19/fichero.json', 'r') as data:    
#         lectura = json.load(data)
#         lista_tia_diaria = []


total_municipality()
get_tia_inicial()
get_tia_final()






