from os import system


# 1.- Cree una clase Persona con los siguientes atributos: 
#     nombre:str 
#     apellido:str 
#     fecha de nacimiento:str -> 'dia-mes-año' 
#     dni:str
#     direccion:list

class Persona():

    def __init__(self, nombre:str, apellido:str, fecha_nacimiento:str, dni:str,direccion:list):
        self.nombre = nombre
        self.apellido = apellido
        self.fnacimiento = fecha_nacimiento
        self.dni = dni
        self.direccion = direccion

    def __str__(self):
        return f'\n Nombre: {self.nombre}\n Apellido: {self.apellido}\n Fecha de nacimiento: {self.fnacimiento} \n Dni: {self.dni} \n Direccion: {self.direccion}\n'

# 2.- Edite la clase Persona y agrege un metodo que permita concatenar 
#     el nombre completo (nombre y apellido):
#     def getNombreCompleto(self):
#         pass
    
    def getNombreCompleto(self):
        return self.nombre +' '+ self.apellido +' '+ 'nació el:'

# 3.- Edite la clase Persona y 3 metodos que permita adquirir(getter) el dia , el mes y el año
#     nota: el atributo fecha_nacimiento es un str ( String )
#     def getDia(self):
#         pass
#     def getMes(self):
#         pass
#     def getAño(self):
#         pass

    def getDia(self):
        dia = self.fnacimiento.split('/')
        return dia[0]
    def getMes(self):
        mes = self.fnacimiento.split('/')
        return mes[1]
    def getAño(self):
        año = self.fnacimiento.split('/')
        return año[2]

# 4.- Edite la clase Persona y 3 metodos que permita editar(setter) el dia , el mes y el año
#     nota: el atributo fecha_nacimiento es un str ( String )
#     def setDia(self, dia):
#         pass
#     def setMes(self, mes):
#         pass
#     def setAño(self, año):
#         pass

    def setDia(self, hdia=None):
        dia = self.fnacimiento.split('/')
        if hdia == None:
            return dia[0]
        else:
            return hdia

    def setMes(self, hmes=None):
        mes = self.fnacimiento.split('/')
        if hmes == None:
            return mes[1]
        else:
            return hmes
    
    def setAño(self, haño=None):
        año = self.fnacimiento.split('/')
        if haño == None:
            return año[2]
        else:
            return haño


"""def main():
    titulo ='---Bienvenido al respaso de la unidad 1 a la 5---'
    opciones = ['1. consulta de tipos de datos',
                '2. hacer operacion selecionada',
                '3. la wiki',
                '4. Operaciones especiales',
                '5. OPCION DE PRUEBA',
                '0. salida'
                ]
    nivel = 0
    salida = True
    while salida == True:
        system('cls') # system('clear') 

        opcion = menu(nivel, titulo, opciones)

        if   opcion == '1': opcion_1()
        elif opcion == '2': opcion_2()   
        elif opcion == '3': opcion_3()
        elif opcion == '4': opcion_4()
        elif opcion == '5': pass
        elif opcion == '0': salida = opcion_0()
        else: 
            print('la opcion seleccionada no se encuentra dispobible, intente nuevamente')
            pausa()

main()"""
