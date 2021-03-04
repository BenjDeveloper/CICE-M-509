
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
    nombre =input("Agregue nombre del departamento: ")
    telefono =input("Agregue telefono del departamento: ")
    objeto_departamento = Departamento(nombre,telefono )
    #Diccionario
    if not objeto_departamento.nombre in dic_departamento.keys():
        dic_departamento[objeto_departamento.nombre]= objeto_departamento
    else:
        print("El departamento ya esta creado")
    pausa()
    #Lista
    # si_existe_departamento = False
    # for i in lista_departamento:
    #     if i.nombre == objeto_departamento.nombre:
    #         si_existe_departamento = True
    # if si_existe_departamento == False:
    #     lista_departamento.append(objeto_departamento)
    #     print(objeto_departamento)
    # else:
    #     print("El departamento ya esta creado")
    # pausa()

def opcion_2(dic_departamento):
    print('opcion 2 - Departameno - Read')
    # nombre_departamento = input("Nombre del departamento que desea ver:")
    # if nombre_departamento in dic_departamento.keys():
    #     print(dic_departamento[nombre_departamento])#Esto imprime solo un departamento

    for valor_objeto_departamento in dic_departamento.values():
        print(valor_objeto_departamento)



    pausa()

def opcion_3(dic_departamento,):
    print('opcion 3 - Departameno - Update')
    nombre_departamento = input("Nombre del departamento que desea ver:")
    if nombre_departamento in dic_departamento.keys():
        print(dic_departamento[nombre_departamento])
        atributo = input("Agregue el nombre del atributo que desea editar:")#Nombre,telefono,empleados
        valor = input("Agregue el valor del atributo anterior que desea editar:")
        if  atributo in ["nombre","telefono"]:
            setattr(dic_departamento[nombre_departamento],atributo,valor)

        if atributo == "nombre":
            objeto_departamento = dic_departamento.pop(nombre_departamento)
            dic_departamento[objeto_departamento.nombre]=objeto_departamento
            print(dic_departamento[objeto_departamento.nombre])
    pausa()

def opcion_4(dic_departamento):
    print('opcion 4 - Departameno - Delete')
    nombre_departamento = input("Nombre del departamento donde desea eliminar:")
    if nombre_departamento in dic_departamento.keys():
        dic_departamento.pop(nombre_departamento)
    else:
        print("El departamento no existe")
        
    pausa()

def opcion_5(dic_departamento):
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
    nombre_departamento = input("Nombre del departamento que desea agregar el empleado:")
    #Diccionario
    if nombre_departamento in dic_departamento.keys():
        if not objeto_empleado.dni in  dic_departamento[nombre_departamento].empleados.keys():
            dic_departamento[nombre_departamento].empleados[objeto_empleado.dni]= objeto_empleado
        else:
            print("El empleado ya se encuentra registrado")
    else:
        print("El empleado no existe")
    print(objeto_empleado)
    #Lista
    # nombre_departamento = input("Nombre del departamento que desea agregar el empleado:")
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
    dni_empleado = input("Ingresa el dni  del empleado que quieres buscar:")
    nombre_departamento = input("Nombre del departamento donde desea buscar:")

    if nombre_departamento in dic_departamento.keys():
        if dni_empleado in dic_departamento[nombre_departamento].empleados.keys():
            print(dic_departamento[nombre_departamento].empleados[dni_empleado])
    



    pausa()

def opcion_7(dic_departamento):
    dni_empleado = input("Introduce el dni del empleado que quieres actualizar:")
    nombre_departamento = input("Introduce el nombre del departamento  donde esta empleado:")
    if nombre_departamento in dic_departamento.keys():
        if dni_empleado in dic_departamento[nombre_departamento].empleados.keys():

            atributo=  input("Introduce el atributo que deseas editar:")
            valor = input("Agregue el valor del atributo anterior que desea editar:")
            if atributo in ["nombre","apellido", "fecha_de_nacimiento","direccion", "email", "clave", "activo", "salario", "horario"]:
                setattr(dic_departamento[nombre_departamento].empleados[dni_empleado],atributo,valor)

    print('opcion 7')
    pausa()

def opcion_8(dic_departamento):
    print('opcion 8- Empleado -Delete')
    dni_empleado = input("Ingresa el dni  del empleado que quieres buscar:")
    nombre_departamento = input("Agrega el nombre del departamento que desea eliminar:")
    if nombre_departamento in dic_departamento.keys():
        if dni_empleado in dic_departamento[nombre_departamento].empleados.keys():
            dic_departamento[nombre_departamento].empleados.pop(dni_empleado)
        else:
            print("El dni no se encuentra registrado en este departamento")
    else:
        print("El departamento no existe")

    pausa()


def opcion_9(dic_supervisor):
    print('opcion 9- Supervisor -Crear')
    objeto_supervisor = Supervisor("ricardito",
                                "lamas",
                                "16-julio-87",
                                "0157226q",
                                "povedilla 4",
                                "lamas@cice.es",
                                "1,2,3,4",
                                True)

    if not objeto_supervisor.dni in dic_supervisor.keys():
        dic_supervisor[objeto_supervisor.dni] = objeto_supervisor
        print(dic_supervisor)
        print(dic_supervisor[objeto_supervisor.dni])
    else:
        print("El supervisor ya se encuentra registrado")
    pausa()


def opcion_10(dic_supervisor,dic_departamentos):
    print("opcion 10")
    dni_super=input("Introduzca el dni del supervisor: ")
    nombre_depa=input("Introduzca el nombre del departamento: ")

    if dni_super in dic_supervisor.keys():
        if nombre_depa in dic_departamentos.keys():
            objeto_supervisor=dic_supervisor[dni_super]
            objeto_departamento=dic_departamentos[nombre_depa]

            objeto_supervisor.departamento = objeto_departamento
            objeto_departamento.supervisor = objeto_supervisor
        else:
            print("El departamento no esta registrado")
    else:
        print("El supervisor no existe - No esta registrado")
    pausa()
    
def opcion_11(dic_supervisor):
    print("Opcion 11 - supervisor - acceder al departamento")
    dni_super=input("Introduzca el dni del supervisor: ")
    if dni_super in dic_supervisor.keys():
        print(dic_supervisor[dni_super])

    pausa()

def menu_simple(objeto_gerencia):
    
    dic_supervisor= {}

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
        print('10. opcion - Supervisor - Conectar Instancias')
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
        elif opcion == '9': opcion_9(dic_supervisor) #Supervisor - Crear
        elif opcion == '10':opcion_10(dic_supervisor,objeto_gerencia.dic_departamentos)#Empleado- Consultar
        elif opcion == '11':opcion_11(dic_supervisor)#Empleado- Consultar
        elif opcion == '0': 
            print('Adios...')
            pausa()
            salida = False
        else: 
            print('la opcion seleccionada no se encuentra dispobible, intente nuevamente')
            pausa()

def main():

    objeto_gerencia = Gerencia("Dainese")
    

    #?Lectura de fichero para crear departamento
    
    path="C:/Users/cice/Pictures/Screenshots/CICE-M-509/CICE-M-509-4"

    fichero = open( path+'/fichero_departamentos.csv', 'r')
    lectura = csv.reader(fichero) 
    for fila in lectura:
        print("Fila  -:",fila[0],fila[1])
        nombre= fila[0]
        telefono=fila[1]
        objeto_departamento=Departamento(nombre,telefono)
        if not objeto_departamento.nombre in objeto_gerencia.dic_departamentos.keys():
            objeto_gerencia.dic_departamentos[objeto_departamento.nombre]= objeto_departamento
        else:
            print("El departamento ya esta creado")
    fichero.close()
    #----------------------------------------------------------
    #?Lectura empleado

    fichero = open( path+'/fichero_empleados.csv', 'r')
    lectura = csv.reader(fichero) 
    for fila in lectura:
        print(len(fila),"Fila  -:",fila[0],fila[1],fila[2],fila[3],fila[4],fila[5],fila[6],fila[7],fila[8],fila[9],fila[10])
        objeto_empleado = Empleado(fila[0],
                                fila[1],
                                fila[2],
                                fila[3],
                                fila[4],
                                fila[5],
                                fila[6],
                                fila[7],
                                fila[8],
                                fila[9])
        nombre_departamento=fila[10]
        if nombre_departamento in objeto_gerencia.dic_departamentos.keys():
            if not objeto_empleado.dni in  objeto_gerencia.dic_departamentos[nombre_departamento].empleados.keys():
                objeto_gerencia.dic_departamentos[nombre_departamento].empleados[objeto_empleado.dni]= objeto_empleado
            else:
                print("El empleado ya se encuentra registrado")
        else:
            print("El empleado no existe")
        print(objeto_empleado)
    
    fichero.close()

    
    menu_simple(objeto_gerencia)

    #----------------------------------------------------------
    #!Escritura de fichero departamentos

    fichero = open( path+'/fichero_departamentos_AUX.csv', 'w')
    contador = 0
    for objeto_departamento in objeto_gerencia.dic_departamentos.values():
        cadena = ""
        if contador == 0:
            cadena = f"{objeto_departamento.nombre},{objeto_departamento.telefono}"
        else:
            cadena = f"\n{objeto_departamento.nombre},{objeto_departamento.telefono}"
        fichero.write(cadena) 

        contador = 1


    fichero.close()


main()

