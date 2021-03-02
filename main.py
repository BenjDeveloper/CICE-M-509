
# EJEMPLO DE MANEJO  DE REPOSITORIOS Y CLASES POR MEDIO DE PAQUETES

from os import system
from package.empleado import Empleado
from package.departamento import Departamento
from package.gerencia import Gerencia

def pausa():
    input('presione enter para continuar...') 

def opcion_1(lista_departamento, dic_departamento):
    print('opcion 1 - Departameno - Create')
    objeto_departamento = Departamento('RRHH',
                                        '555-55-55-55',
                                        )
    print(objeto_departamento)
    if objeto_departamento.nombre not in dic_departamento.keys():
        dic_departamento [ objeto_departamento.nombre] = objeto_departamento
    else:
        print('El departamento esta creado')
    # print(objeto_departamento)
    # lista_departamento.append(objeto_departamento)
    pausa()

def opcion_2(dic_departamento):
    print('opcion 2 - Departameno - Read')
    # nombre_departamento = input('Departamento que desea ver')
    # if nombre_departamento in dic_departamento.keys:
    #     print(dic_departamento[nombre_departamento])

    for valor_objeto_departamento in dic_departamento.values():
        print(valor_objeto_departamento)
    pausa()

def opcion_3(dic_departamento):
    print('opcion 3 - Departameno - Update')
    nombre_departamento = input('Departamento que desea ver: ')
    if nombre_departamento in dic_departamento.keys():
        print(dic_departamento[nombre_departamento])
        atributo = input('Nombre del atributo: ') #nombre, telefono, empelados.
        valor = input('Valor atributo: ')

        if atributo in ['nombre', 'telefono']:
            setattr(dic_departamento[nombre_departamento], atributo, valor)

        if atributo == 'Nombre':
            objeto_departamento = dic_departamento.pop(nombre_departamento)
            dic_departamento[objeto_departamento.nombre] = objeto_departamento

            print(dic_departamento[objeto_departamento.nombre1])

    pausa()

def opcion_4(dic_departamento):
    print('opcion 4 - Departameno - Delete')
    nombre_departamento = input('Elimine el departamento: ')
    if nombre_departamento in dic_departamento.keys():
        dic_departamento.pop(nombre_departamento)

    else:
        print('El departamento no existe')
    pausa()

def opcion_5(lista_departamento, dic_departamento):
    print('opcion 5')
    objeto_empleado = Empleado('Ricardo',
                                'Lamas',
                                '16-Julio-87',
                                '87620348T',
                                'Calle pitis 34',
                                'lamas@cice.com',
                                '1234',
                                True,
                                1500.00,
                                'jornada completa')
    print(objeto_empleado)
    nombre_departamento = input('Nombre departamento: ')
    
    #! DICCIONARIO
    if nombre_departamento in dic_departamento.keys():
        if not objeto_empleado.dni in dic_departamento[nombre_departamento].empleados.keys():
            dic_departamento[nombre_departamento].empleado[objeto_empleado.dni] = objeto_empleado
        else:
            print('El empleado esta registrado')
    else:
        print('El departamento no existe')
    
    #! LISTA
    # lista_empleados = []
    # si_existe_empleado = False
    # for departamento in lista_departamento:
    #     if departamento.nombre == nombre_departamento:
    #         print('encontro el departamento')
    #         lista_empleados = departamento.empleados 

    #     for empleados in lista_empleados:
    #         if objeto_empleado.dni == empleado_dni:
    #             si_existe_empleado = True

    #     if si_existe_empleado == False:
    #         departamento.empelados.append(objeto_empleado)
    #         print(departamento)
    pausa()

def opcion_6(dic_departamento):
    print('opcion 6')
    dni_empleado = input('Agregue el DNI: ')
    nombre_departamento = input('Agregue departamento: ')

    if nombre_departamento in dic_departamento.keys():
        if dni_empleado in dic_departamento[nombre_departamento].empelados.keys():
            print(dic_departamento[nombre_departamento].empleados[dni_empleado])


    # for objeto_departamento in dic_departamento.values():
    #     if dni_empleado in objeto_departamento.empelados.keys():
    #         print(objeto_departamento.nombre, objeto_departamento.empleados[dni_empleado])
    pausa()

def opcion_7(dic_departamento):
    print('opcion 7 - Empleados - Update')
    nombre_departamento = input('Departamento que desea ver: ')
    dni_empleado = input('Agregue el DNI: ')

    if nombre_departamento in dic_departamento.keys():
        if dni_empleado in dic_departamento[nombre_departamento].empelados.keys():
            atributo = input('Nombre del atributo: ') 
            valor = input('Valor atributo: ')
            if atributo in ['nombre', 'apellido', 'fecha_de_nacimiento', 'direccion', 'email', 'clave', 'activo', 'salario', 'horario']:
                setattr(dic_departamento[nombre_departamento].empleados[dni_empleado], atributo, valor)

        else:
            print('DNI no registrado')
    else:
        print('El departamento no existe')




    pausa()

def opcion_8(dic_departamento):
    print('opcion 8 - Eliminar empleado')
    dni_empleado = input('Agregue el DNI: ')
    nombre_departamento = input('Elimine empleado: ')
    if nombre_departamento in dic_departamento.keys():
        if dni_empleado in dic_departamento[nombre_departamento].empelados.keys():
            dic_departamento[nombre_departamento].empleados.pop(dni_empleado)
        else:
            print('DNI no registrado')
    else:
        print('El departamento no existe')
    pausa()



def main():

    objeto_gerencia = Gerencia('Dainese')
    objeto_gerencia.dic_departametos = {}

    lista_departamento = []
    dic_departamento = {}
    salida = True
    while salida == True:
        system('clear') # system('cls') 

        print('--- TITULO MENU ---')
        print('1. opcion - Departamento - Create ')
        print('2. opcion - Departamento - Read ')
        print('3. opcion - Departamento - Update ')
        print('4. opcion - Departamento - Delete ')
        print('5. opcion - Empleado - Create')
        print('6. opcion - Empleado - Read')
        print('7. opcion - Empleado - Update')
        print('8. opcion - Empleado - Delete')

        opcion = input('selecione una:')

        if   opcion == '1': opcion_1(lista_departamento, objeto_gerencia.dic_departametos) #Departamento - Create
        elif opcion == '2': opcion_2(objeto_gerencia.dic_departametos) #Departamento - Read  
        elif opcion == '3': opcion_3(objeto_gerencia.dic_departametos) #Departamento - Update
        elif opcion == '4': opcion_4(objeto_gerencia.dic_departametos) #Departamento - Delete
        elif opcion == '5': opcion_5(lista_departamento, objeto_gerencia.dic_departametos) #Empleado - Create
        elif opcion == '6': opcion_6(objeto_gerencia.dic_departametos) #Empleado - Read
        elif opcion == '7': opcion_7(objeto_gerencia.dic_departametos) #Empleado - Update
        elif opcion == '8': opcion_8(objeto_gerencia.dic_departametos) #Empleado - Delete
        elif opcion == '0': 
            print('Adios...')
            pausa()
            salida = False
        else: 
            print('la opcion seleccionada no se encuentra dispobible, intente nuevamente')
            pausa()


main()


Gerencia
        Nombre
        dic_departamentos {
                            'nombre'


                        }