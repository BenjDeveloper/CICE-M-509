
# EJEMPLO DE MANEJO  DE REPOSITORIOS Y CLASES POR MEDIO DE PAQUETES

import package.departamento as depa
import package.empleado as Empleado
# import package.persona
# import package.User


def main():
    # javi1=Persona("javi","menendez","19/06/1998","123456789F",["Narvaez","51","4º","Izq"])
    # print(javi1)
    # print(javi1.getNombreCompleto())
    # print(javi1.getDia())
    # print(javi1.getMes())
    # print(javi1.getAño())

    # print(javi1.setDia(1))
    # print(javi1.setMes(11))
    # print(javi1.setAño(2019))

    # print(javi1.getDia())
    # print(javi1.getMes())
    # print(javi1.getAño())

    # # print("19/06/1998")
    # # hola=datetime.strptime("19/06/1998", "%d/%m/%Y")
    # # print(hola)
    # # print(hola.strftime("%d/%m/%Y"))

    departamento1=depa.Departamento("informatica","91233456")
    empleado1=Empleado.Empleado("juan","perez","21/11/1995","1234567F",["sainz de baranda","44","4º","Izq"],"qwerty@asdf","9112345623456", 1200,"L-V 10H-14H")
    
    empleado2=Empleado.Empleado("pepe","perez","21/11/1995","1234567F",["sainz de baranda","44","4º","Izq"],"qwerty@asdf","9112345623456",1300,"L-V 10H-14H")
    
    empleado3=Empleado.Empleado("sara","sanchez","21/11/1995","1234567F",["sainz de baranda","44","4º","Izq"],"informatica","9123456", 1200,"L-V 10H-14H")
    
    empleado4=Empleado.Empleado("susana","jimenez","21/11/1995","1234567F",["sainz de baranda","44","4º","Izq"],"informatica","9123456", 1200,"L-V 10H-14H")
    
    empleado5=Empleado.Empleado("ana","ricotta","21/11/1995","1234567F",["sainz de baranda","44","4º","Izq"],"informatica","9123456", 1200,"L-V 10H-14H")

    empleado6=Empleado.Empleado("jorge","mascarpone","21/11/1995","1234567F",["sainz de baranda","44","4º","Izq"],"contabilidad","9123456", 1200,"L-V 10H-14H")

    empleado7=Empleado.Empleado("lisa","pecorinno","21/11/1995","1234567F",["sainz de baranda","44","4º","Izq"],"contabilidad","9123456", 1200,"L-V 10H-14H")

    empleado8=Empleado.Empleado("laura","parmigiano","21/11/1995","1234567F",["sainz de baranda","44","4º","Izq"],"contabilidad","9123456", 1200,"L-V 10H-14H")

    empleado9=Empleado.Empleado("cloe","yanez","21/11/1995","1234567F",["sainz de baranda","44","4º","Izq"],"contabilidad","9123456", 1200,"L-V 10H-14H")

    empleado10=Empleado.Empleado("javi","menendez","19/06/1998","1234567F",["sainz de baranda","44","4º","Izq"],"contabilidad","9123456", 1200,"L-V 10H-14H")

    departamento1.setEmpleados(empleado1,empleado2,empleado3,empleado4,empleado5,empleado6,empleado7,empleado8,empleado9,empleado10)

    departamento1.printEmp()
    print(departamento1.mediaSal())

    # departamento1.empleados.append(empleado1)
    # # print (departamento1.empleados)
    # # print (departamento1.empleados[0])
    # empleado1.pertenece_departamento=departamento1
    # # print(empleado1.pertenece_departamento)
    # # print(type(empleado1.pertenece_departamento))


    # print (departamento1.empleados[0].nombre)
    # print (departamento1.empleados)

    # print(empleado1.pertenece_departamento)
    # departamento1.printEmp()
    # print(departamento1.mediaSal())
    # 

    # # print(empleado5.pertenece_departamento.departYemplea)
    # # print(empleado1.pertenece_departamento.departYemplea)





main()
