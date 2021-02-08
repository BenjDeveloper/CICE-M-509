


#? UNIDAD 10: Cadenas, Textos, Números, Fechas y Horas

import re


#! RE.SEARCH
# cadena = 'la casa de papel'
# busqueda = 'casa'
# # * ejemplo 1
# if  re.search( busqueda, cadena ):
#     print( re.search( busqueda, cadena ) )
#     # <re.Match object; span=(3, 7), match='casa'>
# else:
#     print('que no, que no, que noooo')



#* ejemplo 2
# obj = re.search( busqueda, cadena )
# print( obj.start() )
# print( obj.end() )
# print( obj.span() )
# print( obj.string )


#! RE.MATCH

# texto = 'hola esta cadena es un texto de practica de python'
# busqueda = 'hola'

# obj = re.match( busqueda, texto )

# print(obj)
# # <re.Match object; span=(0, 4), match='hola'>

#! RE.SPLIT

# texto = 'hola esta cadena es un texto de practica de python'
# lista = re.split( ' ', texto )
# print( lista )

#! RE.SUB

# texto = 'hola esta cadena es un texto de practica de python'
# obj = re.sub( 'es un texto de', 'de caracteres es una', texto )
# print(obj)

#! RE.FINDALL

# texto = 'hola esta cadena es un texto de practica de python'
# obj = re.findall( 'de', texto )
# print(obj)

#! PATRONES CON METACARACTERES

#! METACARACTER | ( OR )

#* ejemplo 1
# texto = 'hola adios hello bye hola adios hello bye hola adios hello bye la casa de papel'
# obj = re.findall( 'hola|hello' , texto )
# print(obj)


#* ejemplo 2 - dinamico
# texto = 'hola adios hello bye hola adios hello bye hola adios hello bye la casa de papel'
# def buscar(patrones, texto):
#     expresion = ''
#     for patron in patrones:
#         expresion = expresion + patron + '|'
#     return re.findall(expresion[0:-1], texto)

# print (buscar(['hola','hello', 'papel'], texto) )

#! METACARACTER * (0-n)

# def buscar(patrones, texto):
#     for patron in patrones:
#         print( patron,':',re.findall(patron, texto) )

# texto = 'hlo hola hoola hooola hoooooola hoooooooolu'
# patrones = [ 'ho', 'ho*', 'ho*la', 'hu*la']
# buscar(patrones, texto)

# # buscar -> ho*
# # h, ho, hoo, hooo, hooooo, hoooooooooooo

#! METACARACTER + (1-n)

# def buscar(patrones, texto):
#     for patron in patrones:
#         print( patron,':',re.findall(patron, texto) )

# texto = 'hlo hola hoola hooola hoooooola hoooooooolu'
# patrones = [ 'ho+', 'ho*']
# buscar(patrones, texto)


#! METACARACTER ? (0-1)

# def buscar(patrones, texto):
#     for patron in patrones:
#         print( patron,':',re.findall(patron, texto) )

# texto = 'hlo hola hoola hooola hoooooola hoooooooolu'
# patrones = [ 'ho*', 'ho+', 'ho?']
# buscar(patrones, texto)

#! NUMERO DE REPETICIONES EXPLICITO

# def buscar(patrones, texto):
#     for patron in patrones:
#         print( patron,':',re.findall(patron, texto) )

# texto = 'hlo hola hoola hooola hoooooola hoooooooolu'
# patrones = [ 'ho{0}la', 'ho{1}la', 'ho{2}la', 'ho{6}la']
# buscar(patrones, texto)

#! NUMERO DE REPETICIONES POR RANGO

# def buscar(patrones, texto):
#     for patron in patrones:
#         print( patron,':',re.findall(patron, texto) )

# texto = 'hlo hola hoola hooola hoooooola hoooooooolu'
# patrones = [ 'ho{0,1}la', 'ho{1,2}la', 'ho{2,3}la', 'ho{0,6}la']
# buscar(patrones, texto)

#! CONJUNTO DE CARACTERES {}

# def buscar(patrones, texto):
#     for patron in patrones:
#         print( patron,':',re.findall(patron, texto) )

# texto = 'hlo hola hoola hooola hoooooola hula'
# patrones = [ 'h[ou]la', 'h[aio]la']
# buscar(patrones, texto)

#! EXCLUSION DE GRUPOS []

# def buscar(patrones, texto):
#     for patron in patrones:
#         print( patron,':',re.findall(patron, texto) )

# texto = 'hlo hola hoola hooola hoooooola hula hila'
# patrones = [ 'h[o]la', 'h[^o]la', 'h[^o^u]la']
# buscar(patrones, texto)



#! RANGOS -
# def buscar(patrones, texto):
#     for patron in patrones:
#         print( patron,':',re.findall(patron, texto) )

# texto = 'hola h0la Hoooola mola m0la M0la hxla h1la h2la'
# patrones = [ 'h[a-z]la', 'h[0-9]la', '[A-z]{4}', '[A-Z][A-z0-9]{3}', '[a-z][A-z0-9]{3}']
# buscar(patrones, texto)