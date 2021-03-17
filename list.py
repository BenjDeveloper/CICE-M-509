
import random

# numbers = [3,2,1,6,8,9,5,3]
# numbers1 = [1,2,3,4,7,2]

# def iteration(givenList):
#     result = []
#     count = 0
#     lenght = len(givenList)
#     while count < lenght:
#         result.append(min(givenList))
#         print(result[count])
#         givenList.remove(min(givenList))
#         count += 1
#     print(result)

# iteration(numbers1)

# course = [
#     {
#         "name": "Viktor Navorski",
#         "grade": 10
#     },
#     {
#         "name": "Leo Di Caprio",
#         "grade": 3
#     },
#     {
#         "name": "John Williams",
#         "grade": 10
#     },
#     {
#         "name": "Meryl Streep" ,
#         "grade": 4
#     },
#     {
#         "name": "Jack Black",
#         "grade": 1
#     },
#     {
#         "name": "Jennifer Lopez",
#         "grade": 7
#     },
#     {
#         "name": "Nicole Kidman",
#         "grade": 8
#     },
    

# ]


# aprobados = []
# suspensos = []

# for diccionario in course:
#     if diccionario['grade'] >= 5:
#         aprobados.append(diccionario)
#     else:
#         suspensos.append(diccionario)

# print(aprobados)
# print(suspensos)

# def nota_alumnos(valor_nota):
#     lista_aprobados = []
#     lista_suspensos = []




# Ejercicio 1: Agregar al curso de la tarde los siguiente lista de alumnos, recordad que no pueden tener los mismos id's:
# 	new_students = ["Miguel", "Pedro", "Sandra"]
# 	* Debe trabajarse con una lista dada
	
# Ejercicio 2: Crear una función que permita verificar que ningún id sea igual a otro


# Ejercicio 4: Agregar a los id de los alumnos por la mañana la letra "M" y a los alumnos por la tarde la letra "T"

# Ejercicio 5: Crear una nueva lista con todos los estudiantes de Python

# Ejercicio 6: De la última lista creada dividir por género

# Ejercicio 7: Crear una función que además de agregar la clave courses a cada uno de los estudiantes, se le pueda indicar uno de los 		cursos matriculados

# Siendo estas las siguientes listas, cree una función que permita crear una nueva lista que empiece por los alumnos del turno mañana

# Python por las mañanas: ["Patricia", "Nicole", "Verónica", "Javier", "Guillermo", "Javier", "Pablo"]
# Python por las tardes: ["Germán", "Sara", "José", "Claudio", "Rubén", "Sandra"]

mañana =[{
	"name": "Patricia",
	"id" :  "1",
    "gender": "F"
},
{
	"name": "Nicole",
	"id" :  "2",
    "gender": "F"
},
{
	"name": "Javier",
	"id" :  "3",
    "gender": "M"
},
{
	"name": "Verónica",
	"id" :  "4",
    "gender": "F"
},
{
	"name": "Guillermo",
	"id" :  "5",
    "gender": "M"
},
{
	"name": "Pablo",
	"id" :  "6",
    "gender": "M"
},
{
	"name": "Patricia",
	"id" :  "7",
    "gender": "F"
},
{
	"name": "Patricia",
	"id" :  "8",
    "gender": "F"
},

]

tarde =[
{
	"name": "Germán",
	"id" :  "1",
    "gender": "M"
},
{
	"name": "Sara",
	"id" :  "2",
    "gender": "F"
},
{
	"name": "Jorge",
	"id" :  "3",
    "gender": "M"
},
{
	"name": "María",
	"id" :  "4",
    "gender": "F"
},
{
	"name": "Alicia",
	"id" :  "5",
    "gender": "F"
},
{
	"name": "Hernesto",
	"id" :  "6",
    "gender": "M"
},]

# Ejercicio 1: Agregar al curso de la tarde los siguiente lista de alumnos, recordad que no pueden tener los mismos id's:
# 	new_students = ["Miguel", "Pedro", "Sandra"]

new_students = ["Miguel", "Pedro", "Sandra"]

def nuevo_alumno(donde, agregar_esto):
    lenght = len(donde)
    count = 1
    for student in agregar_esto:
        new_student = {
            'name' : student,
            'id' : '00' + str(lenght + count)
        }
        count += 1
        donde.append(new_student)

#nuevo_alumno(tarde, new_students)   
#print(tarde)


# Ejercicio 2: Crear una función que permita verificar que ningún id sea igual a otro


def verificacion_id(estudiantes):

    lista_id = []

    for estudiante in estudiantes:

        if estudiante['id'] in lista_id:
            print(estudiante)
        else:
            lista_id.append(estudiante['id'])

    if len(lista_id) == len(estudiantes):
        print('Ningun ID repetido')   

#verificacion_id(tarde)
#verificacion_id(mañana)

# Ejercicio 4: Agregar a los id de los alumnos por la mañana la letra "M" y a los alumnos por la tarde la letra "T"

def modificar_parametro(estudiantes, horario):
    
    for estudiante in estudiantes:
        estudiante['id'] += horario
        
        

#modificar_parametro(mañana, 'M')
#modificar_parametro(tarde, 'T')
#print(mañana)
#print(tarde)

# Ejercicio 5: Crear una nueva lista con todos los estudiantes de Python
total_student = mañana + tarde
# print(total_student)

# Ejercicio 6: De la última lista creada dividir por género

def dividir_genero(estudiantes):

    hombre = []
    mujer = []

    for estudiante in estudiantes:
        if estudiante['gender'] == 'M':
            hombre.append(estudiante)
        else:
            mujer.append(estudiante)
    return hombre, mujer

# print(dividir_genero(total_student))

# Ejercicio 7: Crear una función que además de agregar la clave courses a cada uno de los estudiantes, se le pueda indicar uno de los	cursos matriculados



def añadir_curso(total_students):
    cursos = [ 'Excel', 'SPSS','Natacion']
    for estudiantes in total_students:
        ciriaco = random.choice(cursos)
        estudiantes['cursos'] = ciriaco

print(añadir_curso(total_student))

def get_student(total_student):
    id_student = input('ID: ')
    for student in total_student:
        if student['id'] == id_student:
            return student

print(get_student(total_student))
# element loop
# element loop [condition]
# element condition1 condition2 loop

# element for element in list_of_elements if condition
# element if condition else condition for element in list_of_elements
lista = [1,2,3,4]
# print([element * 4 if element >= 2 else element for element in lista])


# callback function
def add(x,y):
    return x + y
# print(lambda x: x + 5)
# add_5 = lambda x, y: x + y
# print(add_5(5, 3))

# filter(add, lista)

# listaC = []
# for element in lista:
#     if element > 2:
#         listaC.append(element * 2)
#     else:
#         listaC.append(element)
# print(listaC)
# print([element * 3 for element in lista if element > 2])
# print([element * 2 if element % 2 == 0 else element for element in lista])
# print([elemento*2 for elemento in lista if elemento % 2 == 0])
# lista2 = [elemento*2 for elemento in lista]
# print(lista2)

# for elemento in lista:
#     elemento * 2


'''
funciones anonimas(lambda)
'''
# filter(lambda word: word + 's', 'sara')



# print(list(filter(lambda x: x > 2,lista)))