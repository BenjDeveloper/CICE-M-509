
#UNIDAD 10 CADENAS, TEXTOS, NUMEROS ,FECHAS

#RE.SEARCH

import re
'''cadena = 'la casa de papel'
busqueda = 'monica'
#ejemplo 1


if(re.search(busqueda,cadena)):
    print(re.search(busqueda,cadena))

#ejemplo 2

obj = re.search(busqueda,cadena)
#donde empieza
print (obj.start())
#donde termina
print (obj.end())
#rango
print (obj.span())
#imprime cadena
print (obj.string)'''

#RE.MATCH

'''texto = 'hola esta cadena es un texto'
busqueda = 'hola'
obj = re.match(busqueda,texto)
print(obj)
#<re.Match object; span=(0, 4), match='hola'>

#RE.SPLIT
texto = 'hola esta cadena es un texto'

re.split(' ',texto)'''

#PATRONES CON METACARACTERES

#OR (|)
texto = 'hola adios hello bye'

obj = re.findall('hola|hello',texto)
print(obj)


