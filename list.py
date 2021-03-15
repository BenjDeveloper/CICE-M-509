
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

course = [
    {
        "name": "Viktor Navorski",
        "grade": 10
    },
    {
        "name": "Leo Di Caprio",
        "grade": 3
    },
    {
        "name": "John Williams",
        "grade": 10
    },
    {
        "name": "Meryl Streep" ,
        "grade": 4
    },
    {
        "name": "Jack Black",
        "grade": 1
    },
    {
        "name": "Jennifer Lopez",
        "grade": 7
    },
    {
        "name": "Nicole Kidman",
        "grade": 8
    },
    

]


aprobados = []
suspensos = []

for diccionario in course:
    if diccionario['grade'] >= 5:
        aprobados.append(diccionario)
    else:
        suspensos.append(diccionario)

print(aprobados)
print(suspensos)

# def nota_alumnos(valor_nota):
#     lista_aprobados = []
#     lista_suspensos = []






