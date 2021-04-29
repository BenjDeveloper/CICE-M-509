import requests as req
import json
from models import Dea, User
# response = req.get("https://datos.comunidad.madrid/catalogo/dataset/35609dd5-9430-4d2e-8198-3eeb277e5282/resource/c38446ec-ace1-4d22-942f-5cc4979d19ed/download/desfibriladores_externos_fuera_ambito_sanitario.json").json()
# with open("deas/desfibriladores.json", "w") as file:
#     json.dump(response, file, indent=4)

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
x = m30_dea_number(data)
# print(x)

def menu():
    print("DEAS")
    print('Opcion 1: Crear usuario')
    print('Opcion 2: Acceder ')
    print('Salir')
menu()

def sub_menu():
    print('1.DEA por codigo ')
    print('2.DEA por distancia')
    print('3.Salir')


user = input('Elija opcion: ')

while user.lower() != 'Salir':
    if user == '1':
        name = input('Introduzca su nombre: ')
        password = input('Introduzca su contraseña: ')
        new_user = {'Nombre': name, 'Password': password}
        with open ('deas/users.json') as file:
            users = json.load(file)
        users["data"].append(new_user)
        with open('deas/users.json', 'w', encoding= 'UTF-8') as file:
            json.dump(users, file, ensure_ascii=False, indent=4)
    elif user == '2':
        password = input('Introduce contraseña: ')
        with open ('deas/users.json') as file:
            users = json.load(file)["data"]
        confirm_user = filter(lambda user: True if user["Password"] == password else False, users )
        if next(confirm_user):
            sub_menu()
            pregunta_2 = input('Elija opcion: ')
            if pregunta_2 == '1':
                dea_code = input('Introduzca el codigo DEA: ')
                with open('deas/desfibriladores.json') as file:
                    dea_reader = json.load(file)["data"]
                    show_dea = filter(lambda dea:dea['codigo_dea'] == dea_code, data)
                    print(next(show_dea))
                sub_menu()
            elif pregunta_2 == '2':
                user_x = int(input('Introduzca la coordenada x: '))
                user_y = int(input('Introduzca la coordenada y: '))
                with open('deas/desfibriladores.json') as file:
                    dea_reader = json.load(file)["data"]
                    user = User(user_x, user_y)
                    dea = user.get_nearest_dea(data)
                    print(dea)



    else:
        print('La contraseña no es correcta')        
        menu()
        

        
        
