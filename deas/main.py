import requests as req
import json
response = req.get("https://datos.comunidad.madrid/catalogo/dataset/35609dd5-9430-4d2e-8198-3eeb277e5282/resource/c38446ec-ace1-4d22-942f-5cc4979d19ed/download/desfibriladores_externos_fuera_ambito_sanitario.json").json()
with open("deas/desfibriladores.json", "w") as file:
    json.dump(response, file, indent=4)

def get_data():
    with open ('deas/desfibriladores.json') as file:
        json_reader = json.load(file)
        data = json_reader["data"]
        return data
data = get_data()


public_dea_number = list(map(lambda des:des["tipo_titularidad"] == 'Pública', data))
private_dea_number = list(map(lambda des:des["tipo_titularidad"] == 'Privada', data))

# print(sum(public_dea_number))
# print(sum(private_dea_number))
# print(sum(public_dea_number + private_dea_number))


def m30_dea_number(given):
    postal_code_m30 = ["28029", "28036", "28046", "28039", "28016", "28020", "28002", "28003", "28015", "28010", "28006", "28028", "28008", "28004", "28001", "28013", "28014", "28009", "28007", "28012", "28005", "28045"]
    counter = 0
    for dea in given:
        counter += 1 if dea["direccion_codigo_postal"] in postal_code_m30 else 0
    return counter
a = m30_dea_number(data)
# print(a)

def menu():
    print("DEAS")
    print('Opcion 1: Crear usuario')
    print('Salir')
menu()
user = input('Elija opcion: ')

while user.lower() != 'Salir':
    if user == '1':
        name = input('Introduzca su nombre: ')
        password = input('Introduzca su contraseña: ')
        new_user = {'Nombre': name, 'Contraseña': password}
        def opcion_1():
            with open ('deas/users.json', 'r') as file:
                users = json.load(file)
                return users
        users = opcion_1()
        users['data'].append(new_user)
        with open('deas/users.json') as file:
            json.dump(users, file)
        menu()
        user = input(': ')

        
        
