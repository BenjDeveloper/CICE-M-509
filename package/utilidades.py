
import os



def menu_crud(opt):
    os.system('cls')
    print('C - Crear un','empleado' if opt == '1' else 'departamento','\nR - Consultar existencias \nU - Editar datos \nD - Eliminar un','empleado' if opt == '1' else 'departamento')
    seleccion = input('\n¿Qué acción desea realizar? (C,R,U ó D): ').upper()
    while not seleccion in ('C','R','U','D'):
        seleccion = input('Opción incorrecta. ¿Qué acción desea realizar? (C,R,U ó D): ')
    
    if seleccion == 'C':
        if opt == '1':
            #*Crear empleado
        else:
            #*Crear departamento
    if seleccion == 'R':
        if opt == '1':
            #*Ver empleados
        else:
            #*Ver departamentos
    if seleccion == 'U':
        if opt == '1':
            #*Editar empleado
        else:
            #*Editar departamento
    if seleccion == 'D':
        if opt == '1':
            #*Eliminar empleado
        else:
            #*Eliminar departamento


def menu_principal():
    os.system('cls')
    print('''\t *MENÚ PRINCIPAL*
    1- Empleados
    2- Departamentos''')
    seleccion = input('\n¿Qué campo desea editar o consultar? (1 ó 2): ')
    while not seleccion in ('1','2'):
        seleccion = input('Opción incorrecta. ¿Qué campo desea editar o consultar? (1 ó 2): ')
    return menu_crud(seleccion)