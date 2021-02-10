
# EJEMPLO DE MANEJO  DE REPOSITORIOS Y CLASES POR MEDIO DE PAQUETES
from package.empleado import Empleado
from package.departamento import Departamento
import csv
def main():

    empleado = Empleado(1200,'L-V 8H a 18H','guillermo@gmail.com','asafsfafsf','Guillermo', 'Ginestal','19/04/1989', '052054554-Z','calle avila 28')
    empleado1 = Empleado(1400,'L-V 10H a 20H','pablo@gmail.com','Djajsjasasd','Pablo', 'Barneto','28/04/1989', '053493944-Y','calle macarena 32')
    empleado2 = Empleado(1800,'L-V 14H a 18H','ciriaco@gmail.com','bhsdfh2234','Ciriaco', 'nose','10/08/2004', '08283737-E','calle alcantara 23')
    empleado3 = Empleado(2200,'L-V 16H a 18H','javi@gmail.com','bhsdfh2234','Javi', 'apellido','14/02/1985', '055664654-R','calle arcoiris 43')
    empleado4 = Empleado(1300,'L-V 9H a 19H','evander@gmail.com','1234jhjfjg','Evander', 'Holifield','07/11/1954', '052545544-C','calle de al lado 25')
    empleado5 = Empleado(2400,'L-J 13H a 17H','nicole@gmail.com','Nic23727','Nicole', 'Martínez','13/10/2001', '05354545-W','calle sol 54')
    empleado6 = Empleado(2100,'L-X 20H a 24H','benjamin@gmail.com','sdfuhsrhasf','Benjamin', 'Peñaloza','31/04/1953', '08554522-G','calle paraguas 12')
    empleado7 = Empleado(1500,'L-V 18H a 22H','roberto@gmail.com','asfahsdfjjkawd','Roberto', 'Cabeza','18/06/1988', '055664654-K','calle sin numero 10')
    empleado8 = Empleado(2500,'L-V 15H a 18H','jorge@gmail.com','bhsdfh2234','Jorge', 'Martin','24/07/1977', '0855545665-S','calle Elipa 89')
    empleado9 = Empleado(2800,'L-V 11H a 20H','gianni@gmail.com','b444678794','Gianni', 'Di Lorenzo','15/09/1983', '456545646-O','calle tres 23')
    
    lista_empleados = [empleado,empleado1,empleado2,empleado3,empleado4,empleado5,empleado6,empleado7,empleado8,empleado9]

    departamento_calidad = Departamento ('calidad', '98574321', lista_empleados)

    #departamento_calidad.lista_empleados.sort(key = lambda Empleado: Empleado.salario, reverse=False)

    print(departamento_calidad.media_salarial())
    print(departamento_calidad.reporte_empleados())

    #path = 'C:/Users/cice.AULA4POV14S/Pictures/Saved Pictures/CICE-M-509'
    #fichero = open (path+'/fichero.csv', 'w')
    #fichero.close





main()