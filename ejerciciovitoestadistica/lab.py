import math
from functools import reduce

# def bucle():
#     count = 0
#     while count < 5:
#         if count == 1:
#             count += 1
#             continue
#         print(count)
#         count += 1

# bucle()

# a = iter('RNadal')
# next(a)
# for element in a:
#     print(element)

def times(a,b):
    return a * b

calculadora = {'add': lambda a,b : a + b, 'times': times}
print(calculadora['times'](6,9))

a = 1
b = lambda a: a + 1
print(b(3))

def treatment(name, gender):
    result = lambda name, gender: f"Sr.{name}" if gender == 'm' else f"Sra. {name}"
    return result(name, gender)
    # def result(name, gender):

# pablo = treatment('Pablo', 'm')
# print(pablo)

# def treatment(name, gender):
#     validation = lambda  gender: True if gender == 'm' else False
#     if validation(gender):
#         return f"Sr. {name}"
#     return f"Sra. {name}"

a = [lambda a,b: a + b, lambda a,b: a * b]
b = 56
c = 28
contador = 0
for function in a:
    contador += function(b,c)
# print(contador)
print(a[0](b,c))

pablo = treatment('Pablo', 'm')
print(pablo)


'''
MAP
'''

values = [1,4,9,16,25]
values1 = [3,6,9]
# def pow(a):
#     return a**3
# print(list(map(pow,values)))

print(list(map(lambda a: a**0.5, values)))

print(sum(map(lambda a,b : a**b, values, values1)))

# map(function, values)

def pow(a):
    return a ** 2

def mapeo( function, given_list):
    result = []
    for value in given_list:
        result.append(pow(value))
    return result
    
print(mapeo(pow,values))
print(list(map(pow,values)))
print(list(map(lambda a: a **2, values)))

print(list(zip(values, values1)))
print(list(map(lambda par: par[0]*par[1], zip(values, values1))))




print(list(filter(lambda a : a%2 == 0,values)))
print(list(map(lambda a : a%2 == 0,values)))
print(reduce(lambda a, b: a+b,values))
print(reduce(lambda a,b: a**b, values))



