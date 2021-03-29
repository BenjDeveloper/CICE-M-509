import requests as req
import os.path
import csv 
import json
import time
import threading # module == threading != Thread

# def get_cpu(seconds):

start = time.perf_counter()

# response = req.get('https://restcountries.eu/rest/v2/name/spain').json()
# response1 = req.get('https://restcountries.eu/rest/v2/name/france').json()
# response2 = req.get('https://restcountries.eu/rest/v2/name/niue').json()
# response3 = req.get('https://restcountries.eu/rest/v2/name/yemen').json()

# time.sleep(8) 

# def cpu_sleep(seconds):
#     time.sleep(seconds)

def req_country():
    time.sleep(1)
    print('finalizado')
    response = req.get('https://restcountries.eu/rest/v2/name/spain').json()
    return response[0]['population']

def add(popt):
    return popt* 1.01

t1 = threading.Thread(target=req_country, args=[1])
# t2 = threading.Thread(target=req_country, args=[1])
a = t1.start()
# t2.start()
# t1.join() #espera a que t1 y t2 hayan finalizado
# t2.join()
# print(t1._target)
finish = time.perf_counter()

print('otra cosa')
print(f'Delta tiempo -->{finish-start}')


# region = input('Introduce el continente: ')
# response2 = req.get(f'https://restcountries.eu/rest/v2/region/{region}').json()
# lista_paises = []
# for element in response2:
#         lista_paises.append(element['name'])

# print(lista_paises)
# # print(response2)
# # print(f"\nName: {response2[0]['name']}")


# name = input('Introduce el pais: ')
# response = req.get(f"https://restcountries.eu/rest/v2/name/{name}").json()
# # print(response)
# print(f"\nName: {response[0]['name']}\nCapital: {response[0]['capital']}\nRegion: {response[0]['region']}\nPopulation: {response[0]['population']}\nArea: {response[0]['area']}\nIdioma: {response[0]['languages'][0]['nativeName']}")




#with open('paises.csv','w', newline='') as file:
#    csv_writer = csv.writer(file)
#    csv_writer.writerow(['nfujy'])


# lista_pablo = ','.join(response[0]['name']response[0]['capital'], response[0]['region'], str(response[0]['population']), str(response[0]['area']), response[0]['languages'][0]['nativeName']])
# file_pablo = open('paises.csv', 'w')
# file_pablo.write('Name, Capital, Region, Population, Area, Idioma')
# file_pablo.write(f"\n{lista_pablo}")
# file_pablo.close()

# tiDict = {
#     'paises':[{
#     'name': response[0]['name'],
#     'capital': response[0]['capital'],
#     'region': response[0]['region'],
#     'population': response[0]['population'],
#     'area': response[0]['area'],
#     'languages': response[0]['languages'][0]['nativeName']
#     }
#     ]
# }

# with open(f"{region}.json", 'w') as file:
#     json.dump(tiDict, file)



    