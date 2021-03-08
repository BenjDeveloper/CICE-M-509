from os import system

class Persona(object):
    def __init__ (self, nombre, apellido, direccion, telefono, dni):
        self.nombre = nombre
        self.apellido = apellido
        self.direccion = direccion
        self.telefono = telefono
        self.dni = dni
        self.mascotas = {}

    def __str__ (self):
        return f'\nNUEVA PERSONA\n\n- Nombre: {self.nombre}\n- Apellido: {self.apellido}\n- Dirección:{self.direccion}\n- Teléfono: {self.telefono}\n- Dni: {self.dni}'

    
class Mascotas(object):
    def __init__(self, nombre_mascota, tipo, raza, edad, color):
        
        self.nombre_mascota = nombre_mascota
        self.tipo = tipo
        self.raza = raza
        self.edad = edad
        self.color = color

    def __str__ (self):
        
        return f'\nNUEVA MASCOTA\n\n- Nombre: {self.nombre_mascota}\n- Tipo: {self.tipo}\n- Raza:{self.raza}\n- Edad: {self.edad}\n- Color: {self.color}'

class Veterinaria(object):

    def __init__(self, nombre_veterinario, direccion_veterinario):

        self.nombre_veterinario = nombre_veterinario
        self.direccion_veterinario = direccion_veterinario
        self.persona = {}


def pausa():
    input('presione enter para continuar...') 

def opcion_1(dic_personas):
        print('opcion 1- Persona - Create')
        
        # objeto_persona = Persona("Guillermo",
        #                             "Ginestal",
        #                             "povedilla 4",
        #                             "666555888",
        #                             "54547898Y")

        nombre = input('Agrege nombre de la persona: ')
        apellido = input('Agrege apellido de la persona: ')
        direccion = input('Agrege la dirección de la persona: ')
        telefono = input('Agrege el teléfono de la persona: ')
        dni = input('Agrege el dni de la persona: ')

        objeto_persona = Persona(nombre,apellido,direccion,telefono,dni)


        if not objeto_persona.dni in dic_personas.keys():
            dic_personas [objeto_persona.dni] = objeto_persona
            print(objeto_persona)
        else:
            print("LA PERSONA YA ESTA CREADA")
        pausa()

def opcion_2(dic_personas):
    print('opcion 2 - Persona - Read')
  
    for valor_objeto_persona in dic_personas.values():
        print(valor_objeto_persona)

    pausa()

def opcion_3(dic_personas):
    print('opcion 3 - Persona - Update')
    
    dni_persona = input("Agrege el DNI que desea editar:")
    if dni_persona in dic_personas.keys():
        print(dic_personas[dni_persona])

        atributo = input("Agrege el nombre del atributo que desea editar: ") #nombre, telefono, empleados
        valor = input("Agrege el atributo anterior que desea editar: ")

        if atributo in ['nombre', 'apellido', 'direccion', 'telefono', 'dni']:
            setattr(dic_personas[dni_persona], atributo, valor)
        
        if atributo == 'dni':
            objeto_persona = dic_personas.pop(dni_persona)
            dic_personas[objeto_persona.dni] = objeto_persona
        
            print(dic_personas[objeto_persona.dni])
    else:
        print('El dni ya se encuentra registrado')


    pausa()

def opcion_4(dic_personas):
    print('opcion 4 - Persona - Delete')
    dni_persona = input('Agrege el nombre de la persona que desea eliminar: ')
    if dni_persona in dic_personas.keys():                                                      
        dic_personas.pop(dni_persona)
    else:
        print('LA PERSONA NO EXISTE')
    pausa()

def opcion_5(dic_mascotas):
        print('opcion 5- Mascota - Create')
        
        # objeto_mascota = Mascotas("Thor",
        #                             "Gato",
        #                             "Aristogato",
        #                             "6 años",
        #                             "Negro")

        nombre = input('Agrege nombre de la mascota: ')
        tipo = input('Agrege el tipo de mascota: ')
        raza = input('Agrege la raza de la mascota: ')
        edad = input('Agrege la edad de la mascota: ')
        color = input('Agrege el color de la mascota: ')

        objeto_mascota = Mascotas(nombre,tipo,raza,edad,color)

        if objeto_mascota.nombre_mascota not in dic_mascotas.keys():
            dic_mascotas [objeto_mascota.nombre_mascota] = objeto_mascota
            print(objeto_mascota)
        else:
            print("LA MASCOTA YA ESTA CREADA")
        pausa()

def opcion_6(dic_mascotas):
    print('opcion 2 - Mascota - Read')
  
    for valor_objeto_mascota in dic_mascotas.values():
        print(valor_objeto_mascota)

    pausa()

def opcion_7(dic_mascotas):
    print('opcion 3 - Mascota - Update')
    
    nombre_mascota = input("Agrege el NOMBRE de la mascota que desea editar:")
    if nombre_mascota in dic_mascotas.keys():
        print(dic_mascotas[nombre_mascota])

        atributo = input("Agrege el nombre del atributo que desea editar: ") 
        valor = input("Agrege el atributo anterior que desea editar: ")

        if atributo in ['nombre', 'tipo', 'raza', 'edad', 'color']:
            setattr(dic_mascotas[nombre_mascota], atributo, valor)
        
        if atributo == 'nombre':
            objeto_mascota = dic_mascotas.pop(nombre_mascota)
            dic_mascotas[objeto_mascota.nombre_mascota] = objeto_mascota
        
            print(dic_mascotas[objeto_mascota.nombre])
    else:
        print('El nombre de la mascota ya se encuentra registrado')

def opcion_8(dic_mascotas):
    print('opcion 4 - Mascota - Delete')
    nombre_mascota = input('Agrege el nombre de la mascota que desea eliminar: ')
    if nombre_mascota in dic_mascotas.keys():                                                      
        dic_mascotas.pop(nombre_mascota)
    else:
        print('LA MASCOTA NO EXISTE')
    pausa()


def menu_simple():
    
    objeto_persona =  Persona('Guillermo','Ginestal','povedilla 4', '666555888', '54547898Y')
                            
    objeto_Veterinario = Veterinaria('Veterinaria Las rozas', 'Avenida de españa 9')
    
    dic_mascotas = {}
    

    salida = True
    while salida == True:
        system('cls') # system('cls') 

        print('--- TITULO MENU ---')
        print('1. opcion - Persona - Create ')
        print('2. opcion - Persona - Read ')
        print('3. opcion - Persona - Update ')
        print('4. opcion - Persona - Delete ')
        print('5. opcion - Mascota - Create')
        print('6. opcion - Mascota - Read')
        print('7. opcion - Mascota - Update')
        print('8. opcion - Mascota - Delete')
        print('9. opcion - Mascota - Create')
        

        opcion = input('selecione una:')

        if   opcion == '1': opcion_1(objeto_Veterinario.persona) 
        elif opcion == '2': opcion_2(objeto_Veterinario.persona)  
        elif opcion == '3': opcion_3(objeto_Veterinario.persona) 
        elif opcion == '4': opcion_4(objeto_Veterinario.persona) 
        elif opcion == '5': opcion_5(objeto_persona.mascotas) 
        elif opcion == '6': opcion_6(objeto_persona.mascotas) 
        elif opcion == '7': opcion_7(objeto_persona.mascotas) 
        elif opcion == '8': opcion_8(objeto_persona.mascotas) 

        # elif opcion == '9': opcion_9(dic_supervisor)            
        
        elif opcion == '0': 
            print('Adios...')
            pausa()
            salida = False
        else: 
            print('la opcion seleccionada no se encuentra dispobible, intente nuevamente')
            pausa()



    
menu_simple()