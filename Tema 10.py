
import re

def p(*args):
    print()
    print(list(args))
    print()

# texto = 'Serbia ganara la ATP cup sin problemas'

# print(re.search('cup', texto))

#2
# cadena = 'vinicius tanque es un figura'
# busqueda = 'tanque'

# obj = re.search( busqueda, cadena)
# print( obj.start())
# print( obj.end())
# print( obj.span())
# print( obj.string)

#! Re.Match

# texto = 'vinicius tanque pichichi de la liga'
# busqueda = 'tanque'

# obj = re.match (busqueda, texto)

# print(obj)

#! RE.SPLIT

# texto = 'vinicius tanque pichichi de la liga'

# lista = re.split( ' ', texto)

# print( lista)

#! RE.Sub

# texto = 'vinicius tanque pichichi de la liga'

# obj = re.sub( 'pichichi de', 'puto amo de', texto)

# print(obj)

#! PATRONES CON METACARACTERES

# texto = 'holas adios hello bye holas adios hello bye holas adios hello bye la casa de papel'
# obj = re.findall( 'hola|hello', texto)
# print(obj)

# def buscar(patrones, texto):
#     expresion = ''
#     for patron in patrones:
#         expresion = expresion + patron + '|'
#     return re.findall(expresion[0:-1], texto)

# print(buscar(['hola','hello', 'papel'], texto))

# texto = 'hlo hola hoola hooola hoooooooola '

# def buscar (patrones, texto):
#     for patron in patrones:
#         print(re.findall(patron, texto))

# patrones = ['ho+', 'ho*', 'ho?']
# buscar(patrones , texto)

#! Numero de repeticiones explicito

# texto = 'hlo hola hoola hooola hoooooooola '

# def buscar (patrones, texto):
#     for patron in patrones:
#         print(re.findall(patron, texto))

# patrones = ['ho{0}la', 'ho{1}la', 'ho{2}la']
# buscar(patrones , texto)

#! Numero de repeticiones por rango

# texto = 'hlo hola hoola hooola hoooooooola '

# def buscar (patrones, texto):
#     for patron in patrones:
#         print(re.findall(patron, texto))

# patrones = ['ho{0,1}la', 'ho{1,2}la', 'ho{2,3}la']
# buscar(patrones , texto)

#!Conjunto de caracteres 

# texto = 'hlo hola hoola hooola hoooooooola '

# def buscar (patrones, texto):
#     for patron in patrones:
#         print(re.findall(patron, texto))

# patrones = ['h[ou]la', 'ho[aio]la']
# buscar(patrones , texto)

#!EXCLUSION DE GRUPOS

texto = 'hlo hola hoola hooola hoooooooola hula hila'

def buscar (patrones, texto):
    for patron in patrones:
        print(re.findall(patron, texto))

patrones = ['h[o]la', 'h[^o]la']
buscar(patrones , texto)