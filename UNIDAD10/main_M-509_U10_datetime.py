

#! DATETIME - LIBRERIAS DE FECHAS

def p(*args):
    print()
    print(*args)

#! NOW - AHORA - FECHA ACTUAL

# import datetime
# datetime.datetime.now()


# from datetime import datetime
# p(datetime.now())

# import datetime as date
# p(date.datetime.now())
# p(date.datetime.now())
# p(date.datetime.now())

# x = str(date.datetime.now())
# p(x)

#! FECHA ACTUAL

# import datetime

# p( datetime.date.today() ) 

#! FECHA TIME - CLASS

# import datetime

# class time():
#     def __init__(self,hour = 0, minute = 0, second = 0):
#         pass


# p(datetime.time())
# p(datetime.time(hour = 10, minute = 10, second = 10))
# p(datetime.time(hour = 21, minute = 41, second = 59))

# ---- T-508

#! FECHA TIME - CLASS - ATRIB. HORA, MINUTO, SEGUNDOS

# import datetime

# a = datetime.time(hour = 21, minute = 41, second = 59, microsecond = 24232 )

# p( 'hora = ', a.hour )
# p( 'minute = ', a.minute )
# p( 'second = ', a.second )
# p( 'microsecond = ', a.microsecond )

#! RANGO DE FECHAS DE UN MES

#! FECHA - CLASS DATETIME
# from datetime import datetime

# a = datetime(2021, 2, 8,10,5,30,2324)
# p( a )

# p( 'año = ', a.year )
# p( 'mes = ', a.month )
# p( 'dia = ', a.day )
# p( 'hora = ', a.hour )
# p( 'minute = ', a.minute )
# p( 'second = ', a.second )
# p( 'microsecond = ', a.microsecond )



#! CONVERSION DE CADENAS A DATETIME

#! STRPTIME

# from datetime import datetime

# fecha_nacimiento = '28/2/1990'

# a = datetime.strptime( fecha_nacimiento, '%d/%m/%Y' )

# # a = datetime(2012,2,12)

# p( 'año = ', a.year )
# p( 'mes = ', a.month )
# p( 'dia = ', a.day )
# p( 'hora = ', a.hour )
# p( 'minute = ', a.minute )
# p( 'second = ', a.second )
# p( 'microsecond = ', a.microsecond )


#! STRFTIME

from datetime import datetime

f = datetime.now()
p( f )

hora = f.strftime('%H:%M:%S')
p(hora)

fecha_formato = f.strftime( '%d de %m del %Y, a las %H:%M:%S' )
p(fecha_formato)