
# EJEMPLO DE MANEJO  DE REPOSITORIOS Y CLASES POR MEDIO DE PAQUETES

import csv
import package.departamento as depa
from package.empleado import Empleado
from package.Gerencia import Gerencia
# import package.persona
# import package.User
from package.supervisor import Supervisor

from os import system


def main():

    alphatechsl=Gerencia("Alphatech S.L.")
    # alphatechsl.setDepartamentosCSV("importempCSV\departamentos.csv")
    menu(alphatechsl)
    # print(alphatechsl)
    # # print(alphatechsl.getDepartamento("informatica"))
    # depart_informatica=alphatechsl.getDepartamento("informatica")
    # print()
    # print(depart_informatica)
    # depart_informatica.printEmp()
    # print(depart_informatica.mediaSal())



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
    if empresaExistente.getDepartamento(nombredepartamento)==None:
        print(f"El departamento {nombredepartamento} no existe")
        return
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


def leer_Emp(empresaExistente,txt):
    # alphatechsl.updateAllEmpleados()
    # nombre=input("Introduzca el nombre del empleado que quiere comprobar: ")
    # existe=False
    # for empleado in alphatechsl.getAllEmpleados():
    #     if empleado.nombre==nombre:
    #         print(f"El empleado {nombre} si existe")
    #         existe=True
    #         break
    # if existe==False:
    #     print(f"El empleado {nombre} no existe")

    dni=input(f"Introduzca el dni del empleado que quiere {txt}: ")
    for dict_depart in empresaExistente.departamentos.values():
        dict_depart=dict_depart.empleados
        if dni in dict_depart:
            print(f"El empleado {dict_depart[dni].nombre}, con dni {dni} si existe")
            print(dict_depart[dni])
            return dict_depart,dni
    print(f"El empleado con {dni} no existe")
    return None,None


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
            empresaExistente.departamentos[nombrenew]=empresaExistente.departamentos.pop(nombreold)
        telefono=input("Introduzca el nuevo telefono del departamento: ")
        departoUpdate.telefono=departoUpdate.telefono if telefono=="" else telefono
        print(f"Se ha actualizado el departamento {nombreold}")
        


    # print(departoUpdate)

def update_Emp(empresaExistente):
    dict_depart,dni=leer_Emp(empresaExistente,"actualizar")
    if dict_depart==None:
        return
    empleado=dict_depart[dni]

    nombre=input("Introduzca el nuevo nombre del Empleado: ")
    empleado.nombre=empleado.nombre if nombre=="" else nombre
    apellido=input("Introduzca el nuevo apellido del Empleado: ")
    empleado.apellido=empleado.apellido if apellido=="" else apellido                   #condicional ternario
    fecha=input("Introduzca el nuevo fecha del Empleado: ")
    empleado.fecha=empleado.fecha if fecha=="" else fecha
    dninew=input("Introduzca el nuevo dni del Empleado: ")
    if dninew!="":
        empleado.dni=dninew
        dict_depart[dninew]=dict_depart.pop(dni)
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
    empresaExistente.updateAllEmpleados()
    return

def eliminar_Depa(empresaExistente):
    print("Tambien se va a elimnar todos los empleados del departamento que quiere Eliminar: ")
    nombre=input("Introduzca el nombre del departamento que quiere Eliminar: ")
    empresaExistente.departamentos.remove(empresaExistente.getDepartamento(nombre))
    print(empresaExistente)
    print(f"El departamento {nombre} se ha eliminado")                                                              #!implementar errores

def eliminar_Emp(empresaExistente):
    dict_depart,dni=leer_Emp(empresaExistente,"Eliminar")
    if dict_depart==None:
        return
    dict_depart.pop(dni)
    print(f"El empleado con {dni} se ha eliminado")
    # nombre=input("Introduzca el nombre del empleado que quiere Eliminar: ")
    # nombredepartamento=input("Introduzca el nombre del departamento al que pertenece el Empleado: ")
    # existe=False
    # for index,empleado in enumerate(empresaExistente.getDepartamento(nombredepartamento).empleados):
    #     if empleado.nombre==nombre:
    #         empresaExistente.getDepartamento(nombredepartamento).empleados.pop(index)
    #         print(f"El empleado {nombre} se ha eliminado")
    #         existe=True
    #         break
    # if existe==False:
    #     print(f"El empleado {nombre}, o el departamento no existe")                                                 #!implementar errores

def opcion_9(dic_supervisores):
    print('opcion 9 - Supervisor - Create')
    
    # objeto_supervisor = Supervisor("ricardo",
    #                                 "lamas",
    #                                 "16-07-87",
    #                                 "123",
    #                                 "povedilla 4",
    #                                 "lamas@cice.es",
    #                                 "1,2,3,4")
    objeto_supervisor = Supervisor("ricardo",
                                    "lamas",
                                    "16/07/1987",
                                    "123",
                                    "povedilla 4",
                                    "lamas@cice.es",
                                    "1,2,3,4")
    #! DICCIONARIO    
    if not objeto_supervisor.dni in dic_supervisores.keys():
        dic_supervisores [ objeto_supervisor.dni ] = objeto_supervisor
        print(objeto_supervisor)
    else:
        print('EL Supervisor INDICADO YA SE ENCUENTRA REGISTRADO')
    pausa()

def opcion_10(dic_supervisores, dic_departamentos):
    print('10. opcion - Supervisor - Conectar Instansias - Referencias de Objetos')
    dni_super = input('agrege el DNI del supersor a asignar: ')
    nombre_depa = input('agrege el NOMBRE del departamendo a ser asingado: ')

    if dni_super in dic_supervisores.keys():
        if nombre_depa in dic_departamentos.keys():

            dic_supervisores[dni_super].departamento = dic_departamentos[nombre_depa]
            dic_departamentos[nombre_depa].supervisor = dic_supervisores[dni_super]

        else:
            print('EL DEPARTAMENTO NO ESTA REGISTRADO')
    else:
        print('EL SUPERVISOR NO EXISTE - NO ESTA REGISTRADO')
    pausa()

def opcion_11(dic_supervisores):
    print('11. opcion - Supervisor - acceder al departamento')
    dni_super = input('agrege el DNI del supersor a consultar: ')
    if dni_super in dic_supervisores.keys():
        print(dic_supervisores[dni_super])
        print(dic_supervisores[dni_super].departamento)
    pausa()

def cargar_csv(empresaExistente):
    print(
        """los departamentos y empleados se cargarán de un archivo csv ubicado en la carpeta importempCSV. 
la estructura sera la sigueinte:
    archivo departamentos.csv:
        tiene 3 columnas: departamento, telefono, "ruta csv empleados" 
        la ultima hace referencia a la ubicacion del csv de los empleados que pertenecen a ese departamento
    archivo empleados:
        su nombre puede ser cualquiera mientras este referenciado en los departamentos
        las columnas son: nombre,apellido,fecha,dni,direccion,email,clave,salario,horario""")
    pausa()
    op=""
    while (op!="y") and (op!="n"):
        op=input("¿Desa cargar los archivos? [Y/N]").lower()
        if op=="y":
            empresaExistente.setDepartamentosCSV("importempCSV\departamentos.csv")
            print("Los archivos se han cargado.")
            return
        elif op=="n":
            print("Operacion cancelada. Slaiendo.")
            return
        else:
            print("El comando no se reconoce. Elija una opcion valida.")

def printAll(empresaExistente):
    empresa=empresaExistente.empresa
    maxlen1=max(len(empresa),len("empresa"))
    maxlendepNombre=len('departamento')
    maxlendepTelef=len('telefono')
    maxlenempNombre=len('nombre')
    maxlenempApellido=len('apellido')
    maxlenempfecha=len('fecha')
    maxlenempdni=len('dni')
    maxlenempemail=len('email')
    maxlenempsalario=len('salario')
    maxlenemphorario=len('horario')
    for depart in empresaExistente.departamentos.values():
        maxlendepNombre=max(maxlendepNombre,len(depart.nombre))
        maxlendepTelef=max(maxlendepTelef,len(depart.telefono))
        for emp in depart.empleados.values():
            maxlenempNombre=max(maxlenempNombre,len(emp.nombre))
            maxlenempApellido=max(maxlenempApellido,len(emp.apellido))
            maxlenempfecha=max(maxlenempfecha,len(emp.fechastr))
            maxlenempdni=max(maxlenempdni,len(emp.dni))
            maxlenempemail=max(maxlenempemail,len(emp.email))
            maxlenempsalario=max(maxlenempsalario,len(str(emp.salario)))
            maxlenemphorario=max(maxlenemphorario,len(emp.horario))
    indented=maxlen1+2
    indented2=maxlendepNombre+2+maxlendepTelef+2+1
    separatorTitels=f"+{'-':-^{maxlen1+2}}+{'-':-^{maxlendepNombre+2}}+{'-':-^{maxlendepTelef+2}}+{'-':-^{maxlenempNombre+2}}+{'-':-^{maxlenempApellido+2}}+{'-':-^{maxlenempfecha+2}}+{'-':-^{maxlenempdni+2}}+{'-':-^{maxlenempemail+2}}+{'-':-^{maxlenempsalario+2}}+{'-':-^{maxlenemphorario+2}}+"
    maxlentotal=len(separatorTitels)
    print(separatorTitels)
    print(f"|{'empresa':^{maxlen1+2}}|{'departamento':^{maxlendepNombre+2}}|{'telefono':^{maxlendepTelef+2}}|{'nombre':^{maxlenempNombre+2}}|{'apellido':^{maxlenempApellido+2}}|{'fecha':^{maxlenempfecha+2}}|{'dni':^{maxlenempdni+2}}|{'email':^{maxlenempemail+2}}|{'salario':^{maxlenempsalario+2}}|{'horario':^{maxlenemphorario+2}}|")
    print(separatorTitels)
    print(f"|{empresa:^{maxlen1+2}}|{' ':^{maxlentotal-(maxlen1+5)}}|")
    for depart in empresaExistente.departamentos.values():
        print(f"+{'-':-^{indented}}+{'-':-^{maxlendepNombre+2}}+{'-':-^{maxlendepTelef+2}}+{'-':-^{maxlentotal-(maxlendepNombre+maxlendepTelef+maxlen1+11)}}+")
        print(f"|{' ':^{indented}}|{depart.nombre:^{maxlendepNombre+2}}|{depart.telefono:^{maxlendepTelef+2}}|{' ':^{maxlentotal-(maxlendepNombre+maxlendepTelef+maxlen1+11)}}|")
        print(f"|{' ':^{indented}}+{'-':-^{maxlendepNombre+2}}+{'-':-^{maxlendepTelef+2}}+{'-':-^{maxlenempNombre+2}}+{'-':-^{maxlenempApellido+2}}+{'-':-^{maxlenempfecha+2}}+{'-':-^{maxlenempdni+2}}+{'-':-^{maxlenempemail+2}}+{'-':-^{maxlenempsalario+2}}+{'-':-^{maxlenemphorario+2}}+")
        for num, emp in enumerate(depart.empleados.values()):
            print("|"+" "*indented+"|"+" "*indented2+f"|{emp.nombre:^{maxlenempNombre+2}}|{emp.apellido:^{maxlenempApellido+2}}|{emp.fechastr:^{maxlenempfecha+2}}|{emp.dni:^{maxlenempdni+2}}|{emp.email:^{maxlenempemail+2}}|{str(emp.salario):^{maxlenempsalario+2}}|{emp.horario:^{maxlenemphorario+2}}|")
            if num!=len(depart.empleados.values())-1:
                print("|"+" "*indented+"|"+" "*indented2+f"+{'-':-^{maxlenempNombre+2}}+{'-':-^{maxlenempApellido+2}}+{'-':-^{maxlenempfecha+2}}+{'-':-^{maxlenempdni+2}}+{'-':-^{maxlenempemail+2}}+{'-':-^{maxlenempsalario+2}}+{'-':-^{maxlenemphorario+2}}+")
    print(f"+{'-':-^{indented}}+{'-':-^{indented2}}+{'-':-^{maxlentotal-(maxlendepNombre+maxlendepTelef+maxlen1+11)}}+")

def export_CSV(empresaExistente):
    print("los departamentos y empleados se exportaran a un archivo csv ubicado en la carpeta exportCSV.\nSe sobreescribirán los archivos en esa carpeta")
    pausa()
    op=""
    while (op!="y") and (op!="n"):
        op=input("¿Desa exportar los datos? [Y/N]").lower()
        if op=="y":
            empresaExistente.export_to_CSV()
            print("Los datos se han exportado.")
            return
        elif op=="n":
            print("Operacion cancelada. Slaiendo.")
            return
        else:
            print("El comando no se reconoce. Elija una opcion valida.")

alphatechsl=Gerencia("Alphatech S.L.")
alphatechsl.setDepartamentosCSV("importempCSV\departamentos.csv")
export_CSV(alphatechsl)
def menu(empresaExistente):

    dic_supervisores = {}

    salida = False
    while salida == False:
        # system('clear') 
        system('cls') 
        # print(empresaExistente.departamentos)

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
        print('9. opcion - Supervisor - Crear')
        print('10. opcion - Supervisor - Conectar Instansias - Referencias de Objetos')
        print('11. opcion - Supervisor - acceder al departamento')
        print('12. opcion - cargar csv Departamentos y Empleados')
        print('13. opcion - ALL - Read')
        print('14. opcion - exportar csv Departamentos y Empleados')

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
            leer_Emp(empresaExistente,"comprobar")      #Empleado - Read
            pausa()
        elif opcion == '7': 
            update_Emp(empresaExistente)    #Empleado - Update
            pausa()
        elif opcion == '8': 
            eliminar_Emp(empresaExistente)  #Empleado - Delete
            pausa()

        elif opcion == '9': opcion_9(dic_supervisores) #Supervisor - Crear
        elif opcion == '10': opcion_10(dic_supervisores, empresaExistente.departamentos) #Supervisor - Conectar
        elif opcion == '11': opcion_11(dic_supervisores) #Supervisor - Conectar

        elif opcion == '12':
            cargar_csv(empresaExistente)
        
        elif opcion == '13': 
            printAll(empresaExistente) #ALL - Read
            pausa()

        elif opcion == '14': 
            export_CSV(empresaExistente)

        elif opcion == '0': 
            print('Adios...')
            pausa()
            salida = True
        else: 
            print('la opcion seleccionada no se encuentra dispobible, intente nuevamente')
            pausa()


# main()

# alphatechsl=Gerencia("Alphatech S.L.")
# alphatechsl.setDepartamentosCSV("importempCSV\departamentos.csv")
# alphatechsl.updateAllEmpleados()
# print(alphatechsl.departamentos)



# opcion editar gerencia --- cambia el nombre solo e imprime la gerencia
# dep=depa.Departamento("aaaaaaaaaaaaaaa","1234567")
# alphatechsl.setDepartamentos(dep)




















