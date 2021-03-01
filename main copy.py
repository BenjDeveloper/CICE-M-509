
# EJEMPLO DE MANEJO  DE REPOSITORIOS Y CLASES POR MEDIO DE PAQUETES

import csv
import package.departamento as depa
import package.empleado as Empleado
from package.Gerencia import Gerencia
# import package.persona
# import package.User

from os import system


def main():

    # departamento1=depa.Departamento("informatica","91233456")
    # # empleado1=Empleado.Empleado("juan","perez","21/11/1995","712187548067K",["sainz de baranda","44","4º","Izq"],"qwerty@asdf.com","tzrtl", 1200,"L-V 10H-14H")
    
    # # empleado2=Empleado.Empleado("pepe","perez","25/1/1983","313256588501E",["sainz de baranda","44","4º","Izq"],"tudul@asdf.com","ufwgk",1866,"L-V 10H-14H")
    
    # # empleado3=Empleado.Empleado("sara","sanchez","16/4/1995","489725656749S",["sainz de baranda","44","4º","Izq"],"trnuf@asdf.com","kmnja", 1744,"L-V 10H-14H")
    
    # # empleado4=Empleado.Empleado("susana","jimenez","13/8/1989","307966939383Q",["sainz de baranda","44","4º","Izq"],"nodeu@asdf.com","hvlks", 1399,"L-V 10H-14H")
    
    # # empleado5=Empleado.Empleado("ana","ricotta","25/6/1983","963250232483J",["sainz de baranda","44","4º","Izq"],"jyfvd@asdf.com","dqfms", 1626,"L-V 10H-14H")

    # # empleado6=Empleado.Empleado("jorge","mascarpone","19/8/1976","668835597115M",["sainz de baranda","44","4º","Izq"],"xcgiu@asdf.com","zqcwl", 1337,"L-V 10H-14H")

    # # empleado7=Empleado.Empleado("lisa","pecorinno","14/12/1986","703830803697G",["sainz de baranda","44","4º","Izq"],"oivyn@asdf.com","ucxsv", 1701,"L-V 10H-14H")

    # # empleado8=Empleado.Empleado("laura","parmigiano","17/6/1975","815092174248Q",["sainz de baranda","44","4º","Izq"],"zhryd@asdf.com","ibksf", 2153,"L-V 10H-14H")

    # # empleado9=Empleado.Empleado("cloe","yanez","23/3/2001","275793331598F",["sainz de baranda","44","4º","Izq"],"kfsqf@asdf.com","bijei", 1978,"L-V 10H-14H")

    # # empleado10=Empleado.Empleado("javi","menendez","19/06/1998","871965078151T",["sainz de baranda","44","4º","Izq"],"yicyn@asdf.com","gskbx", 1527,"L-V 10H-14H")

    # departamento1.setEmpleados(empleado1,empleado2,empleado3,empleado4,empleado5,empleado6,empleado7,empleado8,empleado9,empleado10)

    # departamento1.printEmp()
    # print(departamento1.mediaSal())



    # path = 'I:\AAAmasterpython\codigo\repoMaster\CICE-M-509-4\main.py'
    # fichero = open( path+'/fichero.csv', 'r')


    # listaañadir=[["Patricia","Herresanchez","5/5/1995","223233444T","iglesia2","patricia@gmail.com","jfjfur123","40000","L-V 10H-14H"],
    # ["pepe","perez","18/3/1970","12345678K","real30","pepe@gmail.com","12345","50000","L-V 10H-14H"],
    # ["maria","lopez","7/5/1992","176894045K","cordillera39","maria@gmail.com","67584","45000","L-V 10H-14H"],
    # ["jose","martin","5/5/2002","123458765H","blanco30","jose@gmail.com","9875766","30000","L-V 10H-14H"],
    # ["ana","sanchez","9/11/1976","123484567P","Sepulveda80","ana@gmail.com","12678","420000","L-V 10H-14H"],
    # ["eva","fernandez","8/10/1988","12398778L","corredera10","eva@gmail.com","129889","55000","L-V 10H-14H"],
    # ["Antonio","ruiz","28/8/1991","22765894T","lanuza11","antonio@gmail.com","123423","40000","L-V 10H-14H"],
    # ["elena","rincon","23/7/1985","12345678K","arroyo30","elena@gmail.com","98745","50000","L-V 10H-14H"],
    # ["mariano","rojo","10/8/1975","98756045K","lapaz99","mariano@gmail.com","98764","45000","L-V 10H-14H"],
    # ["luis","sanz","14/10/1985","123498675H","pinar30","luis@gmail.com","7658476","30000","L-V 10H-14H"]]

    # fichero = open('empleados2.csv', 'a')

    # escritura= csv.writer(fichero)
    # for row in listaañadir:
    #     escritura.writerow(row)

    # fichero.close()



    # fichero = open('empleados.csv', 'r')

    # departamento_informatica = depa.Departamento("informatica","91233456")

    # lectura = csv.reader(fichero) 
    # lista = [] 
    # for fila in lectura:
    #     empleado = Empleado.Empleado( fila[0], fila[1], fila[2], fila[3], fila[4], fila[5], fila[6], fila[7], fila[8])
    #     departamento_informatica.setEmpleados(empleado)


    
    # departamento_informatica.printEmp()
    # print (departamento_informatica)
    # print (departamento_informatica.mediaSal())

    # fichero.close()

    # departamento_contabilidad = depa.Departamento("contabilidad","91233456")
    # alphatechsl=Gerencia("Alphatech S.L.")
    # alphatechsl.setDepartamentos(departamento_informatica,departamento_contabilidad)
    # print(alphatechsl)
    
    
    alphatechsl=Gerencia("Alphatech S.L.")
    alphatechsl.setDepartamentosCSV("importempCSV\departamentos.csv")
    print(alphatechsl)
    # print(alphatechsl.getDepartamento("informatica"))
    depart_informatica=alphatechsl.getDepartamento("informatica")
    print()
    print(depart_informatica)
    depart_informatica.printEmp()
    print(depart_informatica.mediaSal())

def menu(empresaExistente):
    # import os

    def depOemp():
        seleccion=input("seleccione el elemento sobre el que realizar la accion: \n\tD - Departamento \n\tE - Empleado \nOpcion seleccionada: ")
        if seleccion!="D" and seleccion!="E":
            print("ERROR: opcion no valida")                                                                                        #!implementar errores
            # continue
            return None
            
        return seleccion
    
    opciones=["C","R","U","D","S"]
    salir=False
    while salir==False:
        # os.system("cls")
        print("Editar empleados y/o departamentos")
        opcion=input("""seleccione la accion que desea realizar:
    C - Create - Crear un Objeto
    R - Read   - Consultar Exitencia 
    U - Update - Editar Datos
    D - Delete - Eliminar Objeto
    S - Salir  - Cerrar el programa
Opcion seleccionada: """)
        if opcion not in opciones:
            print("ERROR: opcion no valida")                                                                                                #!implementar errores
            continue
        if opcion=="S":
            salir=True

        if opcion=="C":
            sel=depOemp()
            if sel==None:
                continue
            elif sel=="D":
                nombre=input("Introduzca el nombre del departamento: ")
                telefono=input("Introduzca el telefono del departamento: ")
                midepartamento=depa.Departamento(nombre,telefono)
                empresaExistente.setDepartamentos(midepartamento)
                print(f"Se ha creado el departamento {midepartamento}")
                continue
            # if depOemp()=="E":
            else:
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
                continue

        if opcion=="R":
            sel=depOemp()
            if sel==None:
                continue
            elif sel=="D":
                nombre=input("Introduzca el nombre del departamento que quiere comprobar: ")
                if empresaExistente.getDepartamento(nombre)==None:
                    print(f"El departamento {nombre} no existe")
                else:
                    print(f"El departamento {nombre} si existe")
                continue
            else:
                # nombre=input("Introduzca el nombre del empleado que quiere comprobar: ")
                # existe=False
                # for departamento in empresaExistente.departamento:
                #     for empleado in departamento.empleados:
                #         if empleado.nombre==nombre:
                #             print(f"El empleado {nombre} si existe")
                #             existe=True
                #             break
                # if existe==False:
                #     print(f"El empleado {nombre} no existe")
                # continue

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
                continue


        if opcion=="U":
            sel=depOemp()
            if sel==None:
                continue
            elif sel=="D":
                nombre=input("Introduzca el nombre del departamento que quiere actualizar: ")
                departoUpdate=empresaExistente.getDepartamento(nombre)
                if departoUpdate==None:
                    print(f"El departamento {nombre} no existe")
                    continue
                # print(departoUpdate)
                print("Los campos que no quiera actualizar dejelos en blanco")
                nombre=input("Introduzca el nuevo nombre del departamento: ")
                departoUpdate.nombre=departoUpdate.nombre if nombre=="" else nombre
                telefono=input("Introduzca el nuevo telefono del departamento: ")
                departoUpdate.telefono=departoUpdate.telefono if telefono=="" else telefono
                print(f"Se ha actualizado el departamento {nombre}")
                # print(departoUpdate)
                continue
            else:
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
                    continue
                # print(empleado)
                nombre=input("Introduzca el nuevo nombre del Empleado: ")
                empleado.nombre=empleado.nombre if nombre=="" else nombre                   #condicional ternario
                apellido=input("Introduzca el nuevo apellido del Empleado: ")
                empleado.apellido=empleado.apellido if apellido=="" else apellido
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
                continue



        if opcion=="D":
            sel=depOemp()
            if sel==None:
                continue
            elif sel=="D":
                print("Tambien se va a elimnar todos los empleados del departamento que quiere Eliminar: ")
                nombre=input("Introduzca el nombre del departamento que quiere Eliminar: ")
                empresaExistente.departamento.remove(empresaExistente.getDepartamento(nombre))
                print(empresaExistente)
                print(f"El departamento {nombre} se ha eliminado")                                               #!implementar errores
                continue
            else:
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
                    print(f"El empleado {nombre}, o el departamento no existe")                                               #!implementar errores
                continue        


# main()

alphatechsl=Gerencia("Alphatech S.L.")
alphatechsl.setDepartamentosCSV("importempCSV\departamentos.csv")
alphatechsl.updateAllEmpleados()
print(alphatechsl.departamento)
# print(alphatechsl.departamento['informatica'].empleados)
# print(alphatechsl.getDepartamento('informatica'))
# print(alphatechsl.getDepartamento('infor'))
# print('hey')

# print(alphatechsl.setAllEmpleados(*alphatechsl.departamento['informatica'].empleados))
# print(alphatechsl.setAllEmpleados(*alphatechsl.departamento['contabilidad'].empleados))
# print(alphatechsl.getAllEmpleados())
# # print(alphatechsl.__allempleados)

# # print(type(alphatechsl.getAllEmpleados))

# # for e in alphatechsl.departamento['informatica'].empleados:
# #     # print(e.nombre)
# #     # print(e)
# #     print(type(e))

# for e in alphatechsl.getAllEmpleados():
#     print(e.nombre)
#     # print(e)
#     print(type(e))

# menu(alphatechsl)

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
    nombre=input("Introduzca el nombre del departamento que quiere actualizar: ")
    departoUpdate=empresaExistente.getDepartamento(nombre)
    if departoUpdate==None:
        print(f"El departamento {nombre} no existe")
    # print(departoUpdate)
    else:
        print("Los campos que no quiera actualizar dejelos en blanco")
        nombre=input("Introduzca el nuevo nombre del departamento: ")
        departoUpdate.nombre=departoUpdate.nombre if nombre=="" else nombre
        telefono=input("Introduzca el nuevo telefono del departamento: ")
        departoUpdate.telefono=departoUpdate.telefono if telefono=="" else telefono
        print(f"Se ha actualizado el departamento {nombre}")
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
    empleado.nombre=empleado.nombre if nombre=="" else nombre                   #condicional ternario
    apellido=input("Introduzca el nuevo apellido del Empleado: ")
    empleado.apellido=empleado.apellido if apellido=="" else apellido
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
    return

def eliminar_Depa(empresaExistente):
    print("Tambien se va a elimnar todos los empleados del departamento que quiere Eliminar: ")
    nombre=input("Introduzca el nombre del departamento que quiere Eliminar: ")
    empresaExistente.departamento.remove(empresaExistente.getDepartamento(nombre))
    print(empresaExistente)
    print(f"El departamento {nombre} se ha eliminado")                                               #!implementar errores

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
        print(f"El empleado {nombre}, o el departamento no existe")                                               #!implementar errores

def update_Emp3(empresaExistente):
    pass
def update_Emp4(empresaExistente):
    pass

def menu2(empresaExistente):
    # import os
    salida = False
    while salida == False:
        # system('clear') 
        system('cls') 

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



#     def depOemp():
#         seleccion=input("seleccione el elemento sobre el que realizar la accion: \n\tD - Departamento \n\tE - Empleado \nOpcion seleccionada: ")
#         if seleccion!="D" and seleccion!="E":
#             print("ERROR: opcion no valida")                                                                                        #!implementar errores
#             # continue
#             return None
            
#         return seleccion
    
#     opciones=["C","R","U","D","S"]
#     salir=False
#     while salir==False:
#         # os.system("cls")
#         print("Editar empleados y/o departamentos")
#         opcion=input("""seleccione la accion que desea realizar:
#     C - Create - Crear un Objeto
#     R - Read   - Consultar Exitencia 
#     U - Update - Editar Datos
#     D - Delete - Eliminar Objeto
#     S - Salir  - Cerrar el programa
# Opcion seleccionada: """)
#         if opcion not in opciones:
#             print("ERROR: opcion no valida")                                                                                                #!implementar errores
#             continue
#         if opcion=="S":
#             salir=True

#         if opcion=="C":
#             sel=depOemp()
#             if sel==None:
#                 continue
#             elif sel=="D":
#                 crear_Depa(empresaExistente)
#             # if depOemp()=="E":
#             else:
#                 crear_Emp(empresaExistente)

#         if opcion=="R":
#             sel=depOemp()
#             if sel==None:
#                 continue
#             elif sel=="D":
#                 leer_Depa(empresaExistente)

#             else:
#                 leer_Emp(empresaExistente)
                


#         if opcion=="U":
#             sel=depOemp()
#             if sel==None:
#                 continue
#             elif sel=="D":
#                 update_Depa(empresaExistente)

#             else:
#                 update_Emp(empresaExistente)

#         if opcion=="D":
#             sel=depOemp()
#             if sel==None:
#                 continue
#             elif sel=="D":
#                 eliminar_Depa(empresaExistente)

#             else:
#                 eliminar_Emp(empresaExistente)
                    

menu2(alphatechsl)