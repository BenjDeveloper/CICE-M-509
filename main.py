
# EJEMPLO DE MANEJO  DE REPOSITORIOS Y CLASES POR MEDIO DE PAQUETES

from os import system
from package.empleado import Empleado
from package.departamento import Departamento

def pausa():
    input('presione enter para continuar...') 

def opcion_1( lista_departamento):
    print('opcion 1 - Departameno - Create')
    objeto_departamento = Departamento("RRHH", " 5555-5555-55" )
    si_existe_departamento = False
    for i in lista_departamento:
        if i.nombre == objeto_departamento.nombre:
            si_existe_departamento = True
    if si_existe_departamento == False:
        lista_departamento.append(objeto_departamento)
        print(objeto_departamento)
    else:
        print("El departamento ya esta creado")
    pausa()

def opcion_2():
    print('opcion 2 - Departameno - Read')
    pausa()

def opcion_3():
    print('opcion 3 - Departameno - Update')
    pausa()

def opcion_4():
    print('opcion 4 - Departameno - Delete')
    pausa()

def opcion_5(lista_departamento):
    print('opcion 5-Empleado - Create')
    
    objeto_empleado = Empleado("ricardo",
                                "lamas",
                                "16-julio-87",
                                "0157226q",
                                "povedilla 4",
                                "lamas@cice.es",
                                "1,2,3,4",
                                True,
                                1500.00,
                                "jornada completa")
    print(objeto_empleado)
    nombre_departamento = input("Nombre del departamento que desea agregar el empleado:")
    lista_empleados = []
    si_existe_empleado = False
    for departamento in lista_departamento:
        if departamento.nombre == nombre_departamento:
            print("Encontro el departamento")
            lista_empleados = departamento.empleados

            for empleado in lista_empleados:
                if objeto_empleado.dni == empleado.dni:
                    si_existe_empleado = True
            
            if si_existe_empleado == False:
                departamento.empleados.append(objeto_empleado)
                print(departamento)
    pausa()


def opcion_6():
    print('opcion 6')
    pausa()

def opcion_7():
    print('opcion 7')
    pausa()

def opcion_8():
    print('opcion 8')
    pausa()



def main():

    lista_departamento = []


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

        if   opcion == '1': opcion_1( lista_departamento) #Departamento - Create
        elif opcion == '2': opcion_2() #Departamento - Read  
        elif opcion == '3': opcion_3() #Departamento - Update
        elif opcion == '4': opcion_4() #Departamento - Delete
        elif opcion == '5': opcion_5(lista_departamento) #Empleado - Create
        elif opcion == '6': opcion_6() #Empleado - Read
        elif opcion == '7': opcion_7() #Empleado - Update
        elif opcion == '8': opcion_8() #Empleado - Delete
        elif opcion == '0': 
            print('Adios...')
            pausa()
            salida = False
        else: 
            print('la opcion seleccionada no se encuentra dispobible, intente nuevamente')
            pausa()


main()


