







import re



def buscar(patrones, texto):
    #for patron in patrones:
    if re.match(patrones, texto):
        print(True)
    else:
        print(False)

        #print( patron,':',*(re.findall(patron, texto)) )

# texto = 'hola h0la Hoooola mola m0la M0la hxla h10la h9la'
# patrones = [ 'h[a-z]la', 'h[0-9]la', '[A-z]{4}', '[A-Z][A-z0-9]{3}', '[a-z][A-z0-9]{3}']
# buscar(patrones, texto)

texto = 'ggouf@gmail.com'
#texto = 'bvpenaloza11@gmail.com'
patrones = '[A-z0-9]{5,22}[@][a-z]+[.][a-z]{2,3}'
buscar(patrones, texto)

print(dir(re))

"""
while True:
    texto = input('agrege su correo para validar:')
    if re.match( patrones[0], texto ):
        print('correo agregado exitosamente')
    else:
        print('ingrese nuevamente su correo')

"""





