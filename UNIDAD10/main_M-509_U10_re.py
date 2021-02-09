
#? UNIDAD 10: Cadenas, Textos, Números, Fechas y Horas

import re

# NOTA
    # class MyClass():
    #     x = 'hola'
    #     def foo(self):
    #         print(self.x)

    #     def estaticas(x):
    #         return x

    # mensaje = 'Metodo Estatico'
    # print( MyClass.estaticas(mensaje) )
    # obj = MyClass()
    # print(obj.x)
    # obj.foo()
    # obj.estaticas(mensaje)


def p(*args):
    print()
    print(*args)


#! RE.SEARCH

#* ejemplo 1
# cadena = 'la casa de papel'
# busqueda = 'casa'
# if  re.search( busqueda, cadena ):
#     print( re.search( busqueda, cadena ) )
#     # <re.Match object; span=(3, 7), match='casa'>
# else:
#     print('que no, que no, que noooo')


# * ejemplo 2
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
# lista_2 = texto.split(' ')
# lista = re.split( ' ', texto )
# print( lista )
# print(lista_2)

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
# p(obj)


# #* ejemplo 2 - dinamico
# texto = 'hola adios heo bye hola adios helo bye hola adios hello bye la casa de papel'
# def buscar(patrones, texto):
#     expresion = ''
#     for patron in patrones:
#         expresion = expresion + patron + '|'
#     return re.findall(expresion[0:-1], texto)

# p(buscar(['hola','hello', 'papel'], texto) )

#! METACARACTER * (0-n)

# def buscar(patrones, texto):
#     for patron in patrones:
#         p( patron,':',re.findall(patron, texto) )

# texto = 'hlo hola hoola hooola hoooooola hoooooooolu'
# patrones = ['ho*lu']
# buscar(patrones, texto)


# patrones = [ 'ho', 'ho*', 'ho*la', 'hu*la']
# # buscar -> ho*
# # h, ho, hoo, hooo, hooooo, hoooooooooooo

#! METACARACTER + (1-n)

# def buscar(patrones, texto):
#     for patron in patrones:
#         p( patron,':',re.findall(patron, texto) )

# texto = 'hlo hola hoola hooola hoooooola hoooooooolu'
# patrones = [ 'ho+', 'ho*']
# buscar(patrones, texto)


#! METACARACTER ? (0-1)

# def buscar(patrones, texto):
#     for patron in patrones:
#         p( patron,':',re.findall(patron, texto) )

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

# texto = 'hlo hola hoola hooola hoooooola hoooooooolu hla'
# patrones = [ 'ho{0,1}la', 'ho{1,2}la', 'ho{2,3}la', 'ho{0,6}la']
# buscar(patrones, texto)



#! CONJUNTO DE CARACTERES {}

# def buscar(patrones, texto):
#     for patron in patrones:
#         p( patron,':',re.findall(patron, texto) )

# texto = 'hlo hola hoola hooola hoooooola hula hxla huuuuuuuuuuuuuuula'
# patrones = [ 'h[ou]la', 'h[aio]la']
# buscar(patrones, texto)


#! EXCLUSION DE GRUPOS []

# def buscar(patrones, texto):
#     for patron in patrones:
#         p( patron,':',re.findall(patron, texto) )

# texto = 'hlo hola hoola hooola hoooooola hula hila'
# patrones = [ 'h[o]la', 'h[^o]la', 'h[^o^u]la']
# buscar(patrones, texto)


#! RANGOS -

# def buscar(patrones, texto):
#     for patron in patrones:
#         p( patron,':',*(re.findall(patron, texto)) )

# texto = 'hola h0la Hoooola mola m0la M0la hxla h10la h9la'
# patrones = [ 'h[a-z]la', 'h[0-9]la', '[A-z]{4}', '[A-Z][A-z0-9]{3}', '[a-z][A-z0-9]{3}']
# buscar(patrones, texto)

# texto = 'bvpenaloza11@gmail.com'
# patrones = [ '[A-z0-9]{5,22}[@][a-z]+[.][a-z]{2,3}']
# buscar(patrones, texto)


# while True:
#     texto = input('agrege su correo para validar:')
#     if re.match( patrones[0], texto ):
#         p('correo agregado exitosamente')
#         break # redirecion de url a inicio, con mensage de que todo esta mega mal
#     else:
#         p('ingrese nuevamente su correo')

# bvpenaloza11@gmail.com



