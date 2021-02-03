
# 6.- Cree una clase Departamento con los siguientes atributos:
#     nombre:str
#     telefono:str

# 8.- Edite la clase Departamento y agrege una lista de Empleados para poder manejar los empleados 
#     de cada Departamento

# 9.- Edite la clase Departamento y agregele metodos para el calculo de la media salarial 
#     del Departamento, tambien un metodo que imprima un reporte de los empleados y sus salarios,
#     ordenados de mayor a menor en funcion de sus salarios

from empleado import Empleado
class Departamento:
    e1 = Empleado(1400,'L-V 8H a 18H','raulito@gmail.com','asafsfafsf','Raúl','González','González', '04358213-Z', 'Calle Piedra 28')
    e2 = Empleado(1800,'L-S 9H a 19H','jose@gmail.com','afhsdjfsdf','Jose','Galardo','G', '04358213-Z', 'Calle Piedra 28')
    lista_empleados = [e1, e2]

    def __init__(self, departamento_nombre:str, departamento_telefono:str):
        self.departamento_nombre = departamento_nombre
        self.departamento_telefono = departamento_telefono

    def media_salarial(self):
        lista_salario = []
        for salario in self.lista_empleados:
            lista_salario.append(salario.__dict__['salario'])
        suma_salarial = sum(lista_salario) / len(lista_salario)
        return f"La media salarial es: {suma_salarial} euros"

    def reporte_empleados(self):
        dic_nombre_salario = {}
        for nombre in self.lista_empleados:
            dic_nombre_salario[nombre.__dict__['nombre']] = nombre.__dict__['salario']
        lista_salario = list(dic_nombre_salario.values())
        lista_salario.sort()
        lista_salario.reverse()

        for x in lista_salario:
            name = list(dic_nombre_salario.keys())[list(dic_nombre_salario.values()).index(x)]
            print(f"{name}:{x}")
        return 'esto es un reporte de los empleados'
        

    def __str__(self):
        return f'\n Nombre del departamento: {self.departamento_nombre}\n Teléfono del departamento: {self.departamento_telefono}'

departamento = Departamento('Desarrollo','916374567')
print(departamento.media_salarial())
print(departamento.reporte_empleados())