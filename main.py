
# EJEMPLO DE MANEJO  DE REPOSITORIOS Y CLASES POR MEDIO DE PAQUETES

import csv
import package.departamento as depa
import package.empleado as Empleado
from package.Gerencia import Gerencia
# import package.persona
# import package.User

from os import system


def main():

    alphatechsl=Gerencia("Alphatech S.L.")
    alphatechsl.setDepartamentosCSV("importempCSV\departamentos.csv")
    print(alphatechsl)
    # print(alphatechsl.getDepartamento("informatica"))
    depart_informatica=alphatechsl.getDepartamento("informatica")
    print()
    print(depart_informatica)
    depart_informatica.printEmp()
    print(depart_informatica.mediaSal())



def pausa():
    input('presione enter para continuar...') 

def crear_Depa(empresaExistente):
    nombre=input("Introduzca el nombre del departamento: ")
    telefono=input("Introduzca el telefono del departamento: ")
    midepartamento=depa.Departamento(nombre,telefono)
    empresaExistente.setDepartamentos(midepartamento)
    print(f"Se ha creado el departamento {midepartamento}")

def crear_Emp(empresaExistente):
    nombredepartamento=input("Introduzca el nombre del departamento al que pertenece el Empleado: ")
    nombre=input("Introduzca el nombre del Empleado: ")
    apellido=input("Introduzca el apellido del Empleado: ")
    fecha=input("Introduzca el fecha del Empleado: ")
    dni=input("Introduzca el dni del Empleado: ")
    direccion=input("Introduzca el direccion del Empleado: ")
    email=input("Introduzca el email del Empleado: ")
    clave=input("Introduzca el clave del Empleado: ")
    salario=input("Introduzca el salario del Empleado: ")
    horario=input("Introduzca el horario del Empleado: ")
    miempleado=Empleado(nombre,apellido,fecha,dni,direccion,email,clave,salario,horario)                                        #!implementar errores
    empresaExistente.getDepartamento(nombredepartamento).setEmpleados(miempleado)                                               #!implementar errores
    print(f"Se ha creado el empleado {miempleado}, en el departamento {nombredepartamento}")

def leer_Depa(empresaExistente):
    nombre=input("Introduzca el nombre del departamento que quiere comprobar: ")
    if empresaExistente.getDepartamento(nombre)==None:
        print(f"El departamento {nombre} no existe")
    else:
        print(f"El departamento {nombre} si existe")


def leer_Emp(empresaExistente):
    alphatechsl.updateAllEmpleados()
    nombre=input("Introduzca el nombre del empleado que quiere comprobar: ")
    existe=False
    for empleado in alphatechsl.getAllEmpleados():
        if empleado.nombre==nombre:
            print(f"El empleado {nombre} si existe")
            existe=True
            break
    if existe==False:
        print(f"El empleado {nombre} no existe")


def update_Depa(empresaExistente):
    nombreold=input("Introduzca el nombre del departamento que quiere actualizar: ")
    departoUpdate=empresaExistente.getDepartamento(nombreold)
    if departoUpdate==None:
        print(f"El departamento {nombreold} no existe")
    # print(departoUpdate)
    else:
        print("Los campos que no quiera actualizar dejelos en blanco")
        nombrenew=input("Introduzca el nuevo nombre del departamento: ")
        if nombrenew!="":
            departoUpdate.nombre=nombrenew
            empresaExistente.departamento[nombrenew]=empresaExistente.departamento.pop(nombreold)
        telefono=input("Introduzca el nuevo telefono del departamento: ")
        departoUpdate.telefono=departoUpdate.telefono if telefono=="" else telefono
        print(f"Se ha actualizado el departamento {nombreold}")
        


    # print(departoUpdate)

def update_Emp(empresaExistente):
    alphatechsl.updateAllEmpleados()
    nombre=input("Introduzca el nombre del Empleado que quiere actualizar: ")
    existe=False
    for empleado in alphatechsl.getAllEmpleados():
        if empleado.nombre==nombre:
            print(f"El empleado {nombre} si existe")
            existe=True
            break
    if existe==False:
        print(f"El empleado {nombre} no existe")
        return
    # print(empleado)
    nombre=input("Introduzca el nuevo nombre del Empleado: ")
    empleado.nombre=empleado.nombre if nombre=="" else nombre
    apellido=input("Introduzca el nuevo apellido del Empleado: ")
    empleado.apellido=empleado.apellido if apellido=="" else apellido                   #condicional ternario
    fecha=input("Introduzca el nuevo fecha del Empleado: ")
    empleado.fecha=empleado.fecha if fecha=="" else fecha
    dni=input("Introduzca el nuevo dni del Empleado: ")
    empleado.dni=empleado.dni if dni=="" else dni
    direccion=input("Introduzca la nueva direccion del Empleado: ")
    empleado.direccion=empleado.direccion if direccion=="" else direccion
    email=input("Introduzca el nuevo email del Empleado: ")
    empleado.email=empleado.email if email=="" else email
    clave=input("Introduzca la nueva clave del Empleado: ")
    empleado.clave=empleado.clave if clave=="" else clave
    salario=input("Introduzca la nueva salario del Empleado: ")
    empleado.salario=empleado.salario if salario=="" else salario
    horario=input("Introduzca el nuevo horario del Empleado: ")
    empleado.horario=empleado.horario if horario=="" else horario
    print(f"Se ha actualizado el Empleado {nombre}")
    # print(empleado)
    alphatechsl.updateAllEmpleados()
    return

def eliminar_Depa(empresaExistente):
    print("Tambien se va a elimnar todos los empleados del departamento que quiere Eliminar: ")
    nombre=input("Introduzca el nombre del departamento que quiere Eliminar: ")
    empresaExistente.departamento.remove(empresaExistente.getDepartamento(nombre))
    print(empresaExistente)
    print(f"El departamento {nombre} se ha eliminado")                                                              #!implementar errores

def eliminar_Emp(empresaExistente):
    nombre=input("Introduzca el nombre del empleado que quiere Eliminar: ")
    nombredepartamento=input("Introduzca el nombre del departamento al que pertenece el Empleado: ")
    existe=False
    for index,empleado in enumerate(empresaExistente.getDepartamento(nombredepartamento).empleados):
        if empleado.nombre==nombre:
            empresaExistente.getDepartamento(nombredepartamento).empleados.pop(index)
            print(f"El empleado {nombre} se ha eliminado")
            existe=True
            break
    if existe==False:
        print(f"El empleado {nombre}, o el departamento no existe")                                                 #!implementar errores



def menu(empresaExistente):

    salida = False
    while salida == False:
        # system('clear') 
        # system('cls') 
        print(empresaExistente.departamento)

        print('--- TITULO MENU ---')
        print('0. opcion - Salir ')
        print('1. opcion - Departamento - Create ')
        print('2. opcion - Departamento - Read ')
        print('3. opcion - Departamento - Update ')
        print('4. opcion - Departamento - Delete ')
        print('5. opcion - Empleado - Create')
        print('6. opcion - Empleado - Read')
        print('7. opcion - Empleado - Update')
        print('8. opcion - Empleado - Delete')

        opcion = input('selecione una:')

        if   opcion == '1': 
            crear_Depa(empresaExistente)    #Departamento - Create
            pausa()
        elif opcion == '2': 
            leer_Depa(empresaExistente)     #Departamento - Read  
            pausa()
        elif opcion == '3': 
            update_Depa(empresaExistente)   #Departamento - Update
            pausa()
        elif opcion == '4': 
            eliminar_Depa(empresaExistente) #Departamento - Delete
            pausa()
        elif opcion == '5': 
            crear_Emp(empresaExistente)     #Empleado - Create
            pausa()
        elif opcion == '6': 
            leer_Emp(empresaExistente)      #Empleado - Read
            pausa()
        elif opcion == '7': 
            update_Emp(empresaExistente)    #Empleado - Update
            pausa()
        elif opcion == '8': 
            eliminar_Emp(empresaExistente)  #Empleado - Delete
            pausa()
        elif opcion == '0': 
            print('Adios...')
            pausa()
            salida = True
        else: 
            print('la opcion seleccionada no se encuentra dispobible, intente nuevamente')
            pausa()


# main()

alphatechsl=Gerencia("Alphatech S.L.")
alphatechsl.setDepartamentosCSV("importempCSV\departamentos.csv")
alphatechsl.updateAllEmpleados()
print(alphatechsl.departamento)


menu(alphatechsl)