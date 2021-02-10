
# EJEMPLO DE MANEJO  DE REPOSITORIOS Y CLASES POR MEDIO DE PAQUETES

import csv
import package.departamento as depa
import package.empleado as Empleado
# import package.persona
# import package.User


def main():

    # departamento1=depa.Departamento("informatica","91233456")
    # # empleado1=Empleado.Empleado("juan","perez","21/11/1995","712187548067K",["sainz de baranda","44","4º","Izq"],"qwerty@asdf.com","tzrtl", 1200,"L-V 10H-14H")
    
    # # empleado2=Empleado.Empleado("pepe","perez","25/1/1983","313256588501E",["sainz de baranda","44","4º","Izq"],"tudul@asdf.com","ufwgk",1866,"L-V 10H-14H")
    
    # # empleado3=Empleado.Empleado("sara","sanchez","16/4/1995","489725656749S",["sainz de baranda","44","4º","Izq"],"trnuf@asdf.com","kmnja", 1744,"L-V 10H-14H")
    
    # # empleado4=Empleado.Empleado("susana","jimenez","13/8/1989","307966939383Q",["sainz de baranda","44","4º","Izq"],"nodeu@asdf.com","hvlks", 1399,"L-V 10H-14H")
    
    # # empleado5=Empleado.Empleado("ana","ricotta","25/6/1983","963250232483J",["sainz de baranda","44","4º","Izq"],"jyfvd@asdf.com","dqfms", 1626,"L-V 10H-14H")

    # # empleado6=Empleado.Empleado("jorge","mascarpone","19/8/1976","668835597115M",["sainz de baranda","44","4º","Izq"],"xcgiu@asdf.com","zqcwl", 1337,"L-V 10H-14H")

    # # empleado7=Empleado.Empleado("lisa","pecorinno","14/12/1986","703830803697G",["sainz de baranda","44","4º","Izq"],"oivyn@asdf.com","ucxsv", 1701,"L-V 10H-14H")

    # # empleado8=Empleado.Empleado("laura","parmigiano","17/6/1975","815092174248Q",["sainz de baranda","44","4º","Izq"],"zhryd@asdf.com","ibksf", 2153,"L-V 10H-14H")

    # # empleado9=Empleado.Empleado("cloe","yanez","23/3/2001","275793331598F",["sainz de baranda","44","4º","Izq"],"kfsqf@asdf.com","bijei", 1978,"L-V 10H-14H")

    # # empleado10=Empleado.Empleado("javi","menendez","19/06/1998","871965078151T",["sainz de baranda","44","4º","Izq"],"yicyn@asdf.com","gskbx", 1527,"L-V 10H-14H")

    # departamento1.setEmpleados(empleado1,empleado2,empleado3,empleado4,empleado5,empleado6,empleado7,empleado8,empleado9,empleado10)

    # departamento1.printEmp()
    # print(departamento1.mediaSal())



    # path = 'I:\AAAmasterpython\codigo\repoMaster\CICE-M-509-4\main.py'
    # fichero = open( path+'/fichero.csv', 'r')


    listaañadir=[["Patricia","Herresanchez","5/5/1995","223233444T","iglesia2","patricia@gmail.com","jfjfur123","40000","L-V 10H-14H"],
    ["pepe","perez","18/3/1970","12345678K","real30","pepe@gmail.com","12345","50000","L-V 10H-14H"],
    ["maria","lopez","7/5/1992","176894045K","cordillera39","maria@gmail.com","67584","45000","L-V 10H-14H"],
    ["jose","martin","5/5/2002","123458765H","blanco30","jose@gmail.com","9875766","30000","L-V 10H-14H"],
    ["ana","sanchez","9/11/1976","123484567P","Sepulveda80","ana@gmail.com","12678","420000","L-V 10H-14H"],
    ["eva","fernandez","8/10/1988","12398778L","corredera10","eva@gmail.com","129889","55000","L-V 10H-14H"],
    ["Antonio","ruiz","28/8/1991","22765894T","lanuza11","antonio@gmail.com","123423","40000","L-V 10H-14H"],
    ["elena","rincon","23/7/1985","12345678K","arroyo30","elena@gmail.com","98745","50000","L-V 10H-14H"],
    ["mariano","rojo","10/8/1975","98756045K","lapaz99","mariano@gmail.com","98764","45000","L-V 10H-14H"],
    ["luis","sanz","14/10/1985","123498675H","pinar30","luis@gmail.com","7658476","30000","L-V 10H-14H"]]

    fichero = open('empleados2.csv', 'a')

    escritura= csv.writer(fichero)
    for row in listaañadir:
        escritura.writerow(row)





    fichero = open('empleados.csv', 'r')

    departamento_informatica = depa.Departamento("informatica","91233456")

    lectura = csv.reader(fichero) 
    lista = [] 
    for fila in lectura:
        empleado = Empleado.Empleado( fila[0], fila[1], fila[2], fila[3], fila[4], fila[5], fila[6], fila[7], fila[8])
        departamento_informatica.setEmpleados(empleado)


    
    departamento_informatica.printEmp()
    print (departamento_informatica)
    print (departamento_informatica.mediaSal())

    fichero.close()






main()
