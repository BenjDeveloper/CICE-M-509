
from os import system

def ver_infomacion(dic_departametos):
    print()
    for key, departamento in dic_departametos.items():
        print()
        print(key.upper())
        for ele in departamento.empleados:
            print(key,ele)
    print()




# MENU GENERICO - PARAMETRIZADO

def opcion_0(nivel = 0):
    tab = '\t' * nivel
    print(tab+'Adios...')
    pausa(nivel)
    return False

def pausa(nivel = 0):
    tab = '\t' * nivel
    input(tab+'presione enter para continuar...') 

def menu_levels_aux(nivel = 0, titulo = 'Asignar Titulo', opciones = ['x. opcion','deber agregar una opcion']):
    tab = '\t' * nivel
    print(tab,titulo)
    for opt in opciones: print(tab,opt)

def menu_levels(nivel = 0, titulo = 'Asignar Titulo', opciones = ['x. opcion','deber agregar una opcion']):
    tab = '\t' * nivel
    print(tab,titulo)
    for opt in opciones: print(tab,opt)
    ope = input(tab + 'selecione una:')
    return ope


def menu(titulo, opciones, raiz):

    CRUD = [] # Funciones

    def opcion_1(nivel = 1): #CARGA DE CRUD
        sub_menu(titulo, opciones,'opcion 1 - Departamenos',raiz,CRUD)

    def opcion_2(nivel = 1):
        sub_menu(titulo, opciones,'opcion 2 - Empleado',raiz,CRUD)

    salida = True
    while salida == True:
        system('clear') # system('cls') 
        opcion = menu_levels(0, titulo, opciones)
        if   opcion == '1': opcion_1() #Departamentos
        elif opcion == '2': opcion_2() #Empleados
        elif opcion == '0': salida = opcion_0()
        else: 
            print('la opcion seleccionada no se encuentra dispobible, intente nuevamente')
            pausa()



def sub_menu(titulo, opciones, sub_titulo, raiz, CRUD):
    sub_opciones = ['1. Create',
                    '2. Read',
                    '3. Update',
                    '4. Delete',
                    '0. salida'
                    ]
    salida = True
    while salida == True:
        system('clear') # system('cls') 
        menu_levels_aux(0,titulo, opciones)
        opcion = menu_levels( 1, sub_titulo, sub_opciones)
        if opcion in ['1','2','3','4'] : pass #CRUD[opcion](raiz) # REVISAR
        elif opcion == '0': salida = opcion_0(1)
        else: 
            print('\t la opcion seleccionada no se encuentra dispobible, intente nuevamente')
            pausa(1)
