
# EJEMPLO DE MANEJO  DE REPOSITORIOS Y CLASES POR MEDIO DE PAQUETES

from os import system
from package.empleado import Empleado
from package.direccion_administrativa import Direccion_administrativa
from package.supervisor import Supervisor
from package.departamento import Departamento

def pausa():
    input('presione enter para continuar...') 

def opcion_1(dic_departamento):
    print('opcion 1 - Departameno - Create')
    nombre = input('agrege un nombre del departamento:')
    telefono = input('agrege un teléfono  del departamento:')
    objeto_departamento = Departamento(nombre, telefono )

    #! DICCIONARIO
    if not objeto_departamento.nombre in dic_departamento.keys():
        dic_departamento [ objeto_departamento.nombre ]  =  objeto_departamento
        print(objeto_departamento)
    else:
        print("EL DEPARTAMENTO YA ESTA CREADO")

    #! LISTA
        # si_existe_departamento = False
        # for i in lista_departamento:
        #     if i.nombre == objeto_departamento.nombre:
        #         si_existe_departamento = True
        # if si_existe_departamento == False:
        #     lista_departamento.append(objeto_departamento)
        #     print(objeto_departamento)
        # else:
        #     print("El departamento ya esta creado")
    pausa()

def opcion_2(dic_departamento):
    print('opcion 2 - Departameno - Read')
    # nombre_departamento = input("Agrege el Nombre del departamento que desea ver:")
    # if nombre_departamento in dic_departamento.keys():
    #     print(dic_departamento[nombre_departamento])
    for valor_objeto_departamento in dic_departamento.values():
        print(valor_objeto_departamento)

    pausa()

def opcion_3(dic_departamento):
    print('opcion 3 - Departameno - Update')
    nombre_departamento = input("Agrege el Nombre del departamento que desea ver:")
    if nombre_departamento in dic_departamento.keys():
        print(dic_departamento[nombre_departamento])

        atributo = input("Agrege el nombre del atributo que desea editar: ") #nombre, telefono, empleados
        valor = input("Agrege el atributo anterior que desea editar: ")
        if atributo in ['nombre', 'telefono']:
            setattr(dic_departamento[nombre_departamento], atributo, valor)
        
        if atributo == 'nombre':
            objeto_departamento = dic_departamento.nombre(nombre_departamento)
            dic_departamento[objeto_departamento.nombre] = objeto_departamento
        
        print(dic_departamento[nombre_departamento])


    pausa()

def opcion_4(dic_departamento):
    print('opcion 4 - Departameno - Delete')
    nombre_departamento = input('Agrege el nombre del departameno que desea eliminar: ')
    if nombre_departamento in dic_departamento.keys():
        dic_departamento.pop(nombre_departamento)
    else:
        print('EL DEPARTAMENTO NO EXISTE')
    pausa()

def opcion_5(lista_departamento, dic_departamento):
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
    
    #! DICCIONARIO    
    if nombre_departamento in dic_departamento.keys():
        if not objeto_empleado.dni in dic_departamento[nombre_departamento].empleados.keys():
            dic_departamento[ nombre_departamento ] . empleados [ objeto_empleado.dni ] = objeto_empleado
        else:
            print('EL EMPLEADO INDICADO YA SE ENCUENTRA REGISTRADO EN EL DEPARTAMENTO')
    else:
        print('EL DEPARTAMENTO INDICADO NO EXISTE')

    #! LISTA
        # lista_empleados = []
        # si_existe_empleado = False
        # for departamento in lista_departamento:
        #     if departamento.nombre == nombre_departamento:
        #         print("Encontro el departamento")
        #         lista_empleados = departamento.empleados

        #         for empleado in lista_empleados:
        #             if objeto_empleado.dni == empleado.dni:
        #                 si_existe_empleado = True
                
        #         if si_existe_empleado == False:
        #             departamento.empleados.append(objeto_empleado)
        #             print(departamento)
    pausa()


def opcion_6(dic_departamento):
    print('opcion 6 - Empleado - Read')
    dni_empleado = input("Agrege el DNI del empleado que desea consultar:")
    # nombre_departamento = input("Agrege el Nombre del departamento donde desea buscar:")

    # if nombre_departamento in dic_departamento.keys():
    #     if dni_empleado in dic_departament[nombre_departamento].empleados.keys():
    #         print(dic_departamento[nombre_departamento].empleados[dni_empleado])

    for objeto_departamento in dic_departamento.values():
        if dni_empleado in objeto_departamento.empleados.keys():
            print(objeto_departamento.nombre, objeto_departamento.empleados[dni_empleado])

        


    pausa()

def opcion_7(dic_departamento):
    print('opcion 7 - Empleado - Update')
    nombre_departamento = input('Departamento que desea ver: ')
    dni_empleado = input('Agrega el DNI: ')
        
    if nombre_departamento in dic_departamento.keys():
        if dni_empleado in dic_departamento[nombre_departamento].empleados.keys():
            atributo = input("Introduce el atributo que deseas editar: ")
            valor = input("Agregue el valor del atributo anterior que desea editar:")
            if atributo in ["nombre", "apellido", "fecha_nacimiento", "direccion", "email", "clave", "activo", "salario", "horario"]:
                setattr(dic_departamento[nombre_departamento].empleados[dni_empleado],atributo,valor)
        else: 
            print('Dni no registrado')
    else: 
        print('El departamento no existe')

    pausa()

def opcion_8(dic_departamento):
    print('opcion 8 - Empleado - Delete')
    dni_empleado = input("Agrege el DNI del empleado que desea Eliminar:")
    nombre_departamento = input('Agrege el nombre del departameno que desea eliminar: ')
    if nombre_departamento in dic_departamento.keys():
        if dni_empleado in dic_departamento[nombre_departamento].empleados.keys():
            dic_departamento[nombre_departamento].empleados.pop(dni_empleado)
        else:
            print('EL DNI NO SE ENCUENTRA REGISTRADO EN ESTE DEPARTAMENTO')
    else:
        print('EL DEPARTAMENTO NO EXISTE')

    pausa()

def opcion_9(dic_supervisor):
    print('opcion - Supervisor - Create')

    objeto_supervisor = Supervisor("Pablo",
                                "Barneto",
                                "24-Septiembre-52",
                                "1234",
                                "povedilla 4",
                                "ciriacousman@cice.es",
                                "cuenta compraaaaaaaa",
                                True)
    print(objeto_supervisor)
    
    if not objeto_supervisor.dni in dic_supervisor.keys():
        dic_supervisor [ objeto_supervisor.dni ]  =  objeto_supervisor
        #print(objeto_supervisor)
    else:
        print("EL SUPERVISOR YA ESTA CREADO")


    pausa()

def opcion_10(dic_supervisor,dic_departamentos):

    dni_super = input('agrege el DNI del supervisor a asignar: ')
    nombre_depa = input('agrege el nombre del departamento: ')

    if dni_super in dic_supervisor.keys():
        if nombre_depa in dic_departamentos.keys():
            
            obj_super = dic_supervisores[dni_super]
            obj_depar = dic_departamentos[nombre_depa]

            obj_super.departamento = obj_depar
            obj_super.supervisor = obj_super
         
        
        else:
            print('EL DEPARTAMENTO NO ESTA REGISTRADO')

    else:
        print('EL SUPERVISOR NO EXISTE - NO ESTA REGISTRADO')

def opcion_11(dic_supervisor):
    print('11. opcion - Supervisor - Acceder al departamento')
    dni_super = input('Agrege DNI: ')
    if dni_super in dic_supervisor.keys():
        print(dic_supervisor[dni_super])

    pausa()


def menu_simple(objeto_DA):

    dic_supervisor = {}

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
        print('10. opcion - Supervisor - Conectar Instancias - Referencias de Objetos')
        print('11. opcion - Empleado - Acceder al departamento')

        opcion = input('selecione una:')

        if   opcion == '1': opcion_1(objeto_DA.dic_departametos) #Departamento - Create
        elif opcion == '2': opcion_2(objeto_DA.dic_departametos) #Departamento - Read  
        elif opcion == '3': opcion_3(objeto_DA.dic_departametos) #Departamento - Update
        elif opcion == '4': opcion_4(objeto_DA.dic_departametos) #Departamento - Delete

        elif opcion == '5': opcion_5(objeto_DA.dic_departametos) #Empleado - Create
        elif opcion == '6': opcion_6(objeto_DA.dic_departametos) #Empleado - Read
        elif opcion == '7': opcion_7(objeto_DA.dic_departametos) #Empleado - Update
        elif opcion == '8': opcion_8(objeto_DA.dic_departametos) #Empleado - Delete

        elif opcion == '9': opcion_9(dic_supervisor)            # Supervisor - Create
        elif opcion == '10': opcion_10(dic_supervisor,objeto_DA.dic_departametos)          # Supervisor - Read
        elif opcion == '11': opcion_11(dic_supervisor) 

        elif opcion == '0': 
            print('Adios...')
            pausa()
            salida = False
        else: 
            print('la opcion seleccionada no se encuentra dispobible, intente nuevamente')
            pausa()


def main():

    objeto_DA = Direccion_administrativa('Dainese')
    menu_simple(objeto_DA)

main()

#! Gerencia

#       Nombre
#?         dic_departamentos {
#             'nombre': objeto_departamento
#!             'RRHH': objeto_departamento_RRHH
#                                             nombre
#                                             telefono
#?                                             empleados{
#!                                                        'dni':objeto_empleado
#                                                                             nombre
#                                                                             apellido
#                                                                             fecha fecha_nacimiento
#                                                                             direccion
#                                                                             dni 
#                                                                             horario
#                                                                             email
#                                                                             clave
#                                                                             salario
#                                                                             activo
#                                             }

#         }


