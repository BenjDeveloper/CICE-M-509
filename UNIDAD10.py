
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

'''#PATRONES CON METACARACTERES

#OR (|)
texto = 'hola adios hello bye'

obj = re.findall('hola|hello',texto)
print(obj)'''

#ejemplo 1
#email

'''nombreusu == '[A-z0-9]'{6,30}
arroba == '[@]'
gmail == '[A-z]'{2,10}
. == '[.]'
com == ['A-z0-9']{2,4}'''

'''texto = 'vsalgueroherrera@gmail.com'
patron = '[A-z0-9]{6,30}[@][A-z]{2,10}[.][A-z0-9]{2,4}'
if re.match(patron,texto):
    print('correo valido')
else:
    print('correo no valido ')'''

'''#CHOICE

import random

nombres = ['benja','isa','evander','vero','patri','javi','nicole']

for i in range(3):
    print(random.choice(nombres))

#SHUFFLE

baraja = [1,2,3,4,5,6,7,8,9]
random.shuffle (baraja)
print(baraja)

 #SAMPLE 

baraja = [1,2,3,4,5,6,7,8,9]
x = random.sample (baraja,5)
print(x)'''

#DATE TIME

'''import datetime

#fecha actual con hora 
objeto_tiempo = datetime.datetime.now()
print(objeto_tiempo)

#fecha actual sin hora 
objeto_tiempo = datetime.date.today()
print(objeto_tiempo)'''

from datetime import time 

#tiempo (hora,min,seg  )
a = time()
print ( 'a =',a)

b = time(11,54,56)
print(b)




