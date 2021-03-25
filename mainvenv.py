import requests as req
import os.path
import csv 
import json


region = input('Introduce el continente: ')
response2 = req.get(f'https://restcountries.eu/rest/v2/region/{region}').json()
lista_paises = []
for element in response2:
        lista_paises.append(element['name'])

print(lista_paises)
# print(response2)
# print(f"\nName: {response2[0]['name']}")


name = input('Introduce el pais: ')
response = req.get(f"https://restcountries.eu/rest/v2/name/{name}").json()
# print(response)
print(f"\nName: {response[0]['name']}\nCapital: {response[0]['capital']}\nRegion: {response[0]['region']}\nPopulation: {response[0]['population']}\nArea: {response[0]['area']}\nIdioma: {response[0]['languages'][0]['nativeName']}")




#with open('paises.csv','w', newline='') as file:
#    csv_writer = csv.writer(file)
#    csv_writer.writerow(['nfujy'])


# lista_pablo = ','.join(response[0]['name']response[0]['capital'], response[0]['region'], str(response[0]['population']), str(response[0]['area']), response[0]['languages'][0]['nativeName']])
# file_pablo = open('paises.csv', 'w')
# file_pablo.write('Name, Capital, Region, Population, Area, Idioma')
# file_pablo.write(f"\n{lista_pablo}")
# file_pablo.close()

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

with open("archivo.json", 'w') as file:
    json.dump(tiDict, file)



    