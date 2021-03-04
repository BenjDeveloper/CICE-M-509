
# EJEMPLO DE MANEJO  DE REPOSITORIOS Y CLASES POR MEDIO DE PAQUETES

from os import system
from package.empleado import Empleado
from package.departamento import Departamento
from package.gerencia import Gerencia
from package.supervisor import Supervisor
import csv

def pausa():
    input('presione enter para continuar...') 

def opcion_1(dic_departamento):
    print('opcion 1 - Departameno - Create')
    nombre = input('Agrege departamento: ')
    telefono = input('Agrege telefono: ')
    objeto_departamento = Departamento(nombre, telefono)

    if objeto_departamento.nombre not in dic_departamento.keys():
        dic_departamento [ objeto_departamento.nombre] = objeto_departamento
        print(objeto_departamento)
    else:
        print('El departamento esta creado')
    # print(objeto_departamento)
    # lista_departamento.append(objeto_departamento)
    pausa()

def opcion_2(dic_departamento):
    print('opcion 2 - Departamento - Read')
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

            print(dic_departamento[objeto_departamento.nombre])


    pausa()

def opcion_4(dic_departamento):
    print('opcion 4 - Departameno - Delete')
    nombre_departamento = input('Elimine el departamento: ')
    if nombre_departamento in dic_departamento.keys():
        dic_departamento.pop(nombre_departamento)

    else:
        print('El departamento no existe')
    pausa()

def opcion_5(dic_departamento):
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
        if dni_empleado in dic_departamento[nombre_departamento].empleados.keys():
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
        if dni_empleado in dic_departamento[nombre_departamento].empleados.keys():
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

def opcion_9(dic_supervisores):
    print('Opcion 9')
    objeto_supervisor = Supervisor('Suan',
                                    'Fan SOne',
                                    '16-Julio-87',
                                    '1234',
                                    'Amazonas 34',
                                    'suanfansone@cice.com',
                                    'suaaaaaaaaan',
                                    True,
                                    )

    if not objeto_supervisor.dni in dic_supervisores.keys():
        dic_supervisores [objeto_supervisor.dni] = objeto_supervisor
        print( objeto_supervisor)
    else:
        print('El supervisor esta registrado')

    pausa()

def opcion_10(dic_supervisores, dic_departametos):

    dni_super = input('Agregue DNI: ')
    departamento_super = input('Agregue departamento: ')

    if dni_super in dic_supervisores.keys():
        if departamento_super in dic_departametos.keys():
            obj_super = dic_supervisores[dni_super]
            obj_depar = dic_departametos[departamento_super]

            obj_super.departamento = obj_depar
            obj_depar.supervisor = obj_super

        else:
            print('Departamento no registrado')
    else:
        print('SUpervisor no existe')

    pausa()

def opcion_11(dic_supervisores):
    print('11. opcion - Supervisor - Acceder al departamento')
    dni_super = input('Agrege DNI: ')
    if dni_super in dic_supervisores.keys():
        print(dic_supervisores[dni_super])
        print(dic_supervisores[dni_super].departamento)
        

    pausa()

def menu_simple(objeto_gerencia):

    dic_supervisores = {}
    dic_departamentos = {}
    objeto_gerencia.dic_departametos = {}
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

        print('9. opcion - Supervisor - Create')
        print('10. opcion - Supervisor - Conectar instancias')
        print('11. opcion - Supervisor - Acceder al departamento')

        opcion = input('selecione una:')

        if   opcion == '1': opcion_1(objeto_gerencia.dic_departamentos) #Departamento - Create
        elif opcion == '2': opcion_2(objeto_gerencia.dic_departamentos) #Departamento - Read  
        elif opcion == '3': opcion_3(objeto_gerencia.dic_departamentos) #Departamento - Update
        elif opcion == '4': opcion_4(objeto_gerencia.dic_departamentos) #Departamento - Delete
        elif opcion == '5': opcion_5(objeto_gerencia.dic_departamentos) #Empleado - Create
        elif opcion == '6': opcion_6(objeto_gerencia.dic_departamentos) #Empleado - Read
        elif opcion == '7': opcion_7(objeto_gerencia.dic_departamentos) #Empleado - Update
        elif opcion == '8': opcion_8(objeto_gerencia.dic_departamentos) #Empleado - Delete
        elif opcion == '9': opcion_9(dic_supervisores) #Supervisor - Crear
        elif opcion == '10': opcion_10(dic_supervisores, objeto_gerencia.dic_departamentos) #Supervisor - Consultar
        elif opcion == '11': opcion_11(dic_supervisores) #Supervisor - Acceder
        elif opcion == '0': 
            print('Adios...')
            pausa()
            salida = False
        else: 
            print('la opcion seleccionada no se encuentra dispobible, intente nuevamente')
            pausa()


def main():

    objeto_gerencia = Gerencia('Dainese')

    #?Lectura de fichero para crear departamentos


    path = 'C:/Users/cice.AULA4POV14S/Documents/CICE-M-509'

    fichero = open(path + '/fichero_departamentos.csv', 'r')
    lectura = csv.reader(fichero) 
    for fila in lectura:
        print('FILA - :' ,fila[0], fila[1])
        nombre = fila[0]
        telefono = fila[1]
        objeto_departamento = Departamento(nombre,telefono)

        if objeto_departamento.nombre not in objeto_gerencia.dic_departamentos.keys():
            objeto_gerencia.dic_departamentos [objeto_departamento.nombre] = objeto_departamento
            print(objeto_departamento)
        else:
            print('El departamento está creado')

    fichero.close()


    
    #?===============================
    #*Lectura de fichero para crear empleados por departamento

    fichero = open(path + '/fichero_empleados.csv', 'r')
    lectura = csv.reader(fichero) 
    for fila in lectura:
        print('FILA - :' ,fila[0], fila[1], fila[2], fila[3], fila[4], fila[5],fila[6], fila[7], fila[8], fila[9], fila[10])
        # nombre = fila[0]
        # telefono = fila[1]
        # fecha_de_nacimiento = fila[2]
        # dni = fila[3]
        # direccion = fila[4]
        # email = fila[5]
        # clave = fila[6]
        # activo = fila[7]
        # salario = fila[8]
        # horario = fila[9]
        # nombre_departamento = fila[10]
        objeto_empleado = Empleado(
                                    fila[0],
                                    fila[1],
                                    fila[2],
                                    fila[3],
                                    fila[4],
                                    fila[5],
                                    fila[6],
                                    fila[7],
                                    fila[8],
                                    fila[9],)
        nombre_departamento = fila[10]

        if nombre_departamento in objeto_gerencia.dic_departamentos.keys():
            if not objeto_empleado.dni in objeto_gerencia.dic_departamentos[nombre_departamento].empleados.keys():
                objeto_gerencia.dic_departamentos[nombre_departamento].empleados[objeto_empleado.dni] = objeto_empleado
            else:
                print('El empleado esta registrado')
        else:
            print('El empleado no existe')

    fichero.close()

    input('pausa....')    

    menu_simple(objeto_gerencia)


    #*=====================================
    #! Escritura de fichero departamentos

    fichero = open( path+'/fichero_departamentos.csv', 'w')
    primera_linea = True
    for objetos_depar in objeto_gerencia.dic_departamentos.values():
        cadena = ''
        if primera_linea == True:
            cadena = f'{objetos_depar.nombre},{objetos_depar.telefono}'
        else:
            cadena = f'\n{objetos_depar.nombre},{objetos_depar.telefono}'
        fichero.write(cadena)
        primera_linea = False
    
    # cadena = f'\nCalidad, 91 637 40 79'
    # fichero.write(cadena)

    # cadena = f'\nRRHH, 91 637 40 80'
    # fichero.write(cadena)

    # cadena = f'\nLogistica, 91 637 40 81'
    # fichero.write(cadena)

    fichero.close()

    #! =====================================

    #^ Escritura de fichero empelado

    fichero = open( path+'/fichero_empleados.csv', 'w')
    primera_linea = True
    for objetos_empleado in objeto_gerencia.dic_departamentos.values():
        cadena = ''
        if primera_linea == True:
            cadena = f'{objetos_empleado.nombre},{objetos_empleado.apellido}, {objetos_empleado.fecha_de_nacimiento}, {objetos_empleado.dni}, {objetos_empleado.email},{objetos_empleado.clave},{objetos_empleado.activo}, {objetos_empleado.salario}, {objetos_empleado.horario}'
        else:
            cadena = f'\n{objetos_empleado.nombre},{objetos_empleado.apellido}, {objetos_empleado.fecha_de_nacimiento}, {objetos_empleado.dni}, {objetos_empleado.email},{objetos_empleado.clave},{objetos_empleado.activo}, {objetos_empleado.salario}, {objetos_empleado.horario}'
        fichero.write(cadena)
        primera_linea = False
    



main()