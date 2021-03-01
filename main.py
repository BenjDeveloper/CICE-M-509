
# EJEMPLO DE MANEJO  DE REPOSITORIOS Y CLASES POR MEDIO DE PAQUETES
# from package.empleado import Empleado
# from package.departamento import Departamento
# import csv
# def main():

#     empleado = Empleado(1200,'L-V 8H a 18H','guillermo@gmail.com','asafsfafsf','Guillermo', 'Ginestal','19/04/1989', '052054554-Z','calle avila 28')
#     empleado1 = Empleado(1400,'L-V 10H a 20H','pablo@gmail.com','Djajsjasasd','Pablo', 'Barneto','28/04/1989', '053493944-Y','calle macarena 32')
#     empleado2 = Empleado(1800,'L-V 14H a 18H','ciriaco@gmail.com','bhsdfh2234','Ciriaco', 'nose','10/08/2004', '08283737-E','calle alcantara 23')
#     empleado3 = Empleado(2200,'L-V 16H a 18H','javi@gmail.com','bhsdfh2234','Javi', 'apellido','14/02/1985', '055664654-R','calle arcoiris 43')
#     empleado4 = Empleado(1300,'L-V 9H a 19H','evander@gmail.com','1234jhjfjg','Evander', 'Holifield','07/11/1954', '052545544-C','calle de al lado 25')
#     empleado5 = Empleado(2400,'L-J 13H a 17H','nicole@gmail.com','Nic23727','Nicole', 'Martínez','13/10/2001', '05354545-W','calle sol 54')
#     empleado6 = Empleado(2100,'L-X 20H a 24H','benjamin@gmail.com','sdfuhsrhasf','Benjamin', 'Peñaloza','31/04/1953', '08554522-G','calle paraguas 12')
#     empleado7 = Empleado(1500,'L-V 18H a 22H','roberto@gmail.com','asfahsdfjjkawd','Roberto', 'Cabeza','18/06/1988', '055664654-K','calle sin numero 10')
#     empleado8 = Empleado(2500,'L-V 15H a 18H','jorge@gmail.com','bhsdfh2234','Jorge', 'Martin','24/07/1977', '0855545665-S','calle Elipa 89')
#     empleado9 = Empleado(2800,'L-V 11H a 20H','gianni@gmail.com','b444678794','Gianni', 'Di Lorenzo','15/09/1983', '456545646-O','calle tres 23')
    
#     lista_empleados = [empleado,empleado1,empleado2,empleado3,empleado4,empleado5,empleado6,empleado7,empleado8,empleado9]

#     departamento_calidad = Departamento ('calidad', '98574321', lista_empleados)

    #departamento_calidad.lista_empleados.sort(key = lambda Empleado: Empleado.salario, reverse=False)

    # print(departamento_calidad.media_salarial())
    # print(departamento_calidad.reporte_empleados())

    #path = 'C:/Users/cice.AULA4POV14S/Pictures/Saved Pictures/CICE-M-509'
    #fichero = open (path+'/fichero.csv', 'w')
    #fichero.close





# EJEMPLO DE MANEJO  DE REPOSITORIOS Y CLASES POR MEDIO DE PAQUETES

from os import system
from package.empleado import Empleado
from package.departamento import Departamento


def pausa():
    input('presione enter para continuar...') 

def opcion_1(lista_departamento):
    print('opcion 1 - Departamento - Create')
    objeto_departamento = Departamento('Contabilidad','555-55-55-55' )
    print(objeto_departamento)
    lista_departamento.append(objeto_departamento)                               
    pausa()
    
def opcion_2():
    print('opcion 2 - Departamento - Read')
    pausa()

def opcion_3():
    print('opcion 3 - Departamento - Update')
    pausa()

def opcion_4():
    print('opcion 4 - Departamento - Delete')
    pausa()

def opcion_5(lista_departamento):
    print('opcion 5 - Empleado - Create')
    
    objeto_empleado = Empleado(1500.00,
                                'jornada completa',
                                'guillermo.cice@gmail.com',
                                'manuela 10',
                                'Guillermo',
                                'Ginestal',
                                '7/03/1989',
                                '05315444Y',
                                'Calle Avila 12'
                                )
    print(objeto_empleado) 
    nombre_departamento = input('nombre del departamento que desea agregar el empleado: ')     

    lista_empleados = []
    si_existe_empleado = False
    for departamento in lista_departamento:
        if departamento.departamento_nombre == nombre_departamento:
            print('encontro el departamento')
            lista_empleados = departamento.lista_emp

            for empleado in lista_empleados:
                if objeto_empleado.dni == empleado.dni:
                    si_existe_empleado = True

            if si_existe_empleado == False:
                departamento.lista_emp.append(objeto_empleado)
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

        if   opcion == '1': opcion_1(lista_departamento) #Departamento - Create
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