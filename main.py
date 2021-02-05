
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

    
    empleado1=Empleado.Empleado("juan","perez","21/11/1995","1234567F",["sainz de baranda","44","4º","Izq"],"qwert@asdf","9112345623456", 1200,"L-V 10H-14H")
    # print(empleado1)
    departamento1=depa.Departamento("informatica","91233456")
    departamento1.empleados.append(empleado1)
    # print (departamento1.empleados)
    # print (departamento1.empleados[0])
    empleado1.pertenece_departamento=departamento1
    # print(empleado1.pertenece_departamento)
    # print(type(empleado1.pertenece_departamento))

    print (departamento1.empleados[0].nombre)

    # empleado2=Empleado("pepe","perez","21/11/1995","1234567F",["sainz de baranda","44","4º","Izq"],"contabilidad","9123456", 1200,"L-V 10H-14H")
    # # print(empleado2)

    # empleado3=Empleado("sara","perez","21/11/1995","1234567F",["sainz de baranda","44","4º","Izq"],"informatica","9123456", 1200,"L-V 10H-14H")
    # # print(empleado3)

    # empleado4=Empleado("susana","perez","21/11/1995","1234567F",["sainz de baranda","44","4º","Izq"],"informatica","9123456", 1200,"L-V 10H-14H")
    # # print(empleado4)

    # empleado5=Empleado("ana","perez","21/11/1995","1234567F",["sainz de baranda","44","4º","Izq"],"informatica","9123456", 1200,"L-V 10H-14H")
    # # print(empleado5)

    # # print(empleado5.pertenece_departamento.departYemplea)
    # # print(empleado1.pertenece_departamento.departYemplea)





main()
