
#?CSV

# path = './MPP - Máster Programación Python - Oficial Python Institute/Unidad 12/M-509'

#! APERTURA - ABRIR FICHERO / CERRADO DE FICHEROS

# fichero = open( path+'/fichero.csv', 'w')

# fichero.close()


#! LECTURA - READER

# import csv

# fichero = open( path+'/fichero.csv', 'r')

# lectura = csv.reader(fichero) 
# for fila in lectura:
#     print(fila)

# fichero.close()

#! LECTURA - READLINE

# fichero = open( path+'/fichero.csv', 'r')

# print( fichero.readline() )

# fichero.close()

#! LECTURA - READLINES

# fichero = open( path+'/fichero.csv', 'r')

# print( fichero.readlines() )

# fichero.close()

#! ESCRITURA - WRITE

# fichero = open( path+'/fichero.csv', 'a')

# fichero.write('\n')
# fichero.write('HOLA QUE TAL')

# fichero.close()

#! ESCRITURA - WRITELINES

# fichero = open( path+'/fichero.csv', 'w')

# lista = ['benjamin\n', 'evander\n', 'ciriaco\n']
# fichero.write('\n')
# fichero.writelines(lista)

# fichero.close()


#? EJERCICIO
#? escriba y lea un archivo CSV 
#? con el formato siguiente:

# import csv


# path = './MPP - Máster Programación Python - Oficial Python Institute/Unidad 12/M-509'

# ESCRITURA
# fichero = open( path+'/fichero.csv', 'a')
# fichero.write(f'Patricia,Herresanchez,15-09-71,223233444T,iglesia2,patricia@gmail.com,jfjfur123∑,True,40000,partido')
# fichero.close()


#* fichero.csv ( recuerde separado por comas ',' y sin espacios )
#* nombre,apellido,fecha_de_nacimiento,dni,direccion,email,clave,activo,salario,horario
#? Patricia,Herresanchez,15-09-71,223233444T,iglesia2,patricia@gmail.com,jfjfur123∑,True,40000,partido


# LECTURA
# fichero = open( path+'/fichero.csv', 'r')
# lectura = csv.reader(fichero) 
# for fila in lectura:
#     print(fila)
# fichero.close()

#* fichero.csv ( recuerde separado por comas ',' y sin espacios )
#* nombre,apellido,fecha_de_nacimiento,dni,direccion,email,clave,activo,salario,horario
#? ['Patricia', 'Herresanchez', '15-09-71', '223233444T', 'iglesia2', 'patricia@gmail.com', 'jfjfur123∑', 'True', '40000', 'partido']