import requests as req
import os.path
import csv 
import json
import time
import threading # module == threading != Thread
import concurrent.futures


# www.unsplash.com galeria de imagenes
# https://pypi.org/project/PySimpleGUI/


def get_country(country):
    response = req.get(f'https://restcountries.eu/rest/v2/name/{country}').json()
    # return (f"\nName: {response[0]['name']}\nCapital: {response[0]['capital']}\nRegion: {response[0]['region']}\nPopulation: {response[0]['population']} personas\nArea: {response[0]['area']} km2\nIdioma: {response[0]['languages'][0]['nativeName']}")
    return response

# user = input('Que pais: ')
# with concurrent.futures.ThreadPoolExecutor() as executor:
#     future = executor.submit(get_country, user) # == threading.Thread(target=la funcion que queramos ejecutar)
#     print('Loading...')
#     print(future.result())




# def get_spain():
#     response = req.get(f'https://restcountries.eu/rest/v2/name/spain').json()
#     return response

# with concurrent.futures.ThreadPoolExecutor() as executor:
#     future = executor.submit(get_spain)
#     print('Loading...')
#     print(future.result())



# start = time.perf_counter()

# def req_country():
#     time.sleep(1)
#     print('finalizado')
#     response = req.get('https://restcountries.eu/rest/v2/name/spain').json()
#     return response[0]['population']

# def add(popt):
#     return popt* 1.01

# t1 = threading.Thread(target=req_country)
# # t2 = threading.Thread(target=req_country, args=[1])
# a = t1.start()
# # t2.start()
# # t1.join() #espera a que t1 y t2 hayan finalizado
# # t2.join()
# # print(t1._target)
# finish = time.perf_counter()

# print('otra cosa')
# print(f'Delta tiempo -->{finish-start}')


def paises():
    question1 = input('Elige continente o pais: ')
    if question1 == 'continente':
        region = input('Introduce el continente: ')
        response2 = req.get(f'https://restcountries.eu/rest/v2/region/{region}').json()
        lista_paises = []
        lista_poblaciones = []
        for element in response2:
                lista_paises.append(element['name'])

        for e in response2:
                lista_poblaciones.append(e['population'])

        print(f'{sum(lista_poblaciones)} personas')

        name = input('Introduce el pais: ')
        # response = req.get(f"https://restcountries.eu/rest/v2/name/{name}").json()
        # print(f"\nName: {response[0]['name']}\nCapital: {response[0]['capital']}\nRegion: {response[0]['region']}\nPopulation: {response[0]['population']} personas\nArea: {response[0]['area']} km2\nIdioma: {response[0]['languages'][0]['nativeName']}")

        with concurrent.futures.ThreadPoolExecutor() as executor:
            future = executor.submit(get_country, name )
            print('Su respuesta se esta procesando...')
            print(future.result())

        # print(f"\nName: {response[0]['name']}\nCapital: {response[0]['capital']}\nRegion: {response[0]['region']}\nPopulation: {response[0]['population']} personas\nArea: {response[0]['area']} km2\nIdioma: {response[0]['languages'][0]['nativeName']}")

        response = future.result()

        tiDict = {
            'paises':[{
            'name': response[0]['name'],
            'capital': response[0]['capital'],
            'region': response[0]['region'],
            'population': response[0]['population'],
            'area': response[0]['area'],
            'languages': response[0]['languages'][0]['nativeName']
            }
            ]
        }

        with open(f"{region}.json", 'w') as file:
            json.dump(tiDict, file)
    else:

        name = input('Introduce el pais: ')
        response = req.get(f"https://restcountries.eu/rest/v2/name/{name}").json()
        # print(f"\nName: {response[0]['name']}\nCapital: {response[0]['capital']}\nRegion: {response[0]['region']}\nPopulation: {response[0]['population']} personas\nArea: {response[0]['area']} km2\nIdioma: {response[0]['languages'][0]['nativeName']}")

        with concurrent.futures.ThreadPoolExecutor() as executor:
            future = executor.submit(get_country, name)
            print('Su respuesta se esta procesando...')
            # print(future.result())
        
        print(f"\nName: {response[0]['name']}\nCapital: {response[0]['capital']}\nRegion: {response[0]['region']}\nPopulation: {response[0]['population']} personas\nArea: {response[0]['area']} km2\nIdioma: {response[0]['languages'][0]['nativeName']}")


        lista_pablo = ','.join([response[0]['name'],response[0]['capital'], response[0]['region'], str(response[0]['population']), str(response[0]['area']), response[0]['languages'][0]['nativeName']])
        file_pablo = open('paises.csv', 'a')
        # file_pablo.write('Name, Capital, Region, Population, Area, Idioma')
        file_pablo.write(f"\n{lista_pablo}")
        file_pablo.close()

    
    

paises()

# with concurrent.futures.ThreadPoolExecutor() as executor:
#     future = executor.submit(get)
#     print('Su respuesta se esta procesando...')
#     print(future.result())


    #with open('paises.csv','w', newline='') as file:
    #    csv_writer = csv.writer(file)
    #    csv_writer.writerow(['nfujy'])