import requests as req
import os.path
import csv 
import json
import time
import threading # module == threading != Thread
import concurrent.futures

# response = req.get('https://restcountries.eu/data/arg.svg')
# name_img = name.split('-')
# name_img[1]

# print(response.content)

# with open('./images/dell.svg', 'wb') as img:
#     img.write(response.content)


# www.unsplash.com galeria de imagenes
# https://pypi.org/project/PySimpleGUI/


# def get_country(country):
#     response = req.get(f'https://restcountries.eu/rest/v2/name/{country}').json()
#     # return (f"\nName: {response[0]['name']}\nCapital: {response[0]['capital']}\nRegion: {response[0]['region']}\nPopulation: {response[0]['population']} personas\nArea: {response[0]['area']} km2\nIdioma: {response[0]['languages'][0]['nativeName']}")
#     return response

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
        response = req.get(f"https://restcountries.eu/rest/v2/name/{name}").json()
        print(f"\nName: {response[0]['name']}\nCapital: {response[0]['capital']}\nRegion: {response[0]['region']}\nPopulation: {response[0]['population']} personas\nArea: {response[0]['area']} km2\nIdioma: {response[0]['languages'][0]['nativeName']}\nBandera: {response[0]['flag']}")

        # with concurrent.futures.ThreadPoolExecutor() as executor:
        #     future = executor.submit(get_country, name )
        #     print('Su respuesta se esta procesando...')
        #     print(future.result())

        question2 = input('Desea guardar la imagen del pais encontrado: ')
        if question2 != 'no':
            bandera = response[0]['flag']
            bandera1 = req.get(bandera)
            name_bandera = bandera.split('/')
            with open(f'./imagenes/{name_bandera[-1]}', 'wb') as img:
                img.write(bandera1.content)

        # print(f"\nName: {response[0]['name']}\nCapital: {response[0]['capital']}\nRegion: {response[0]['region']}\nPopulation: {response[0]['population']} personas\nArea: {response[0]['area']} km2\nIdioma: {response[0]['languages'][0]['nativeName']}\nBandera: {response[0]['flag']}")

        # response = future.result()

        tiDict = {
            'paises':[{
            'name': response[0]['name'],
            'capital': response[0]['capital'],
            'region': response[0]['region'],
            'population': response[0]['population'],
            'area': response[0]['area'],
            'languages': response[0]['languages'][0]['nativeName'],
            'bandera' : response[0]['flag']
            }
            ]
        }

        with open(f"{region}.json", 'w') as file:
            json.dump(tiDict, file)
    else:

        name = input('Introduce el pais: ')
        response = req.get(f"https://restcountries.eu/rest/v2/name/{name}").json()
        print(f"\nName: {response[0]['name']}\nCapital: {response[0]['capital']}\nRegion: {response[0]['region']}\nPopulation: {response[0]['population']} personas\nArea: {response[0]['area']} km2\nIdioma: {response[0]['languages'][0]['nativeName']}\nBandera: {response[0]['flag']}")

        question2 = input('Desea guardar la imagen del pais encontrado: ')
        if question2 != 'no':
            bandera = response[0]['flag']
            bandera1 = req.get(bandera)
            name_bandera = bandera.split('/')
            with open(f'./imagenes/{name_bandera[-1]}', 'wb') as img:
                img.write(bandera1.content)

        # with concurrent.futures.ThreadPoolExecutor() as executor:
        #     future = executor.submit(get_country, name)
        #     print('Su respuesta se esta procesando...')
        #     print(future.result())
        
        # print(f"\nName: {response[0]['name']}\nCapital: {response[0]['capital']}\nRegion: {response[0]['region']}\nPopulation: {response[0]['population']} personas\nArea: {response[0]['area']} km2\nIdioma: {response[0]['languages'][0]['nativeName']}\nBandera: {response[0]['flag']}")


        lista_pablo = ','.join([response[0]['name'],response[0]['capital'], response[0]['region'], str(response[0]['population']), str(response[0]['area']), response[0]['languages'][0]['nativeName'], response[0]['flag']])
        file_pablo = open('paises.csv', 'a')
        # file_pablo.write('Name, Capital, Region, Population, Area, Idioma')
        file_pablo.write(f"\n{lista_pablo}")
        file_pablo.close()

        print('---HISTORIAL DE BUSQUEDA---')
        with open('paises.csv', "r") as file:
            csv_reader = csv.reader(file)
            lista_band = []
            for e in csv_reader:
                print(e[0], e[3])
                lista_band.append(e[-1])
                
                

            question3 = input('Desea descargar las imagenes del historial: ')
            if question3 == 'si':

                with open(f'./imagenes/{[-1]}', 'wb') as img:
                    img.write(bandera1.content)





        # file_pablo = open('paises.csv', 'r')
        # evanderpringao = csv.read(file_pablo)
        # for e in evanderpringao:
        #     print(e)

        # print('HISTORIAL DE BUSQUEDA')
        # nombre_historial = []
        # poblacion_historial = []
        # for e in response:
        #     nombre_historial.append(e['name'])
        # for e1 in response:
        #     poblacion_historial.append(e1['population'])
        # print(nombre_historial, poblacion_historial)
        

    
    

paises()

# with concurrent.futures.ThreadPoolExecutor() as executor:
#     future = executor.submit(get)
#     print('Su respuesta se esta procesando...')
#     print(future.result())


    #with open('paises.csv','w', newline='') as file:
    #    csv_writer = csv.writer(file)
    #    csv_writer.writerow(['nfujy'])