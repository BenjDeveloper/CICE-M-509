
import pandas as pd

class Departamento():

    def __init__(self, nombre, telefono, lista_empleados=[]):
        self.nombre = nombre
        self.telefono = telefono
        self.empleados = lista_empleados 

    def __str__(self):
        return f'Departamento: {self.nombre}, Teléfono: {self.telefono}'

    def __crea_dataframe_empleado(self):
        '''
        Funcion auxiliar para los metodos media_salarial() y reporte_salarial(). Crea un tipo de dato llamado DataFrame
        que podemos entender como una tabla. El diccionario_de_datos se guarda de manera que cada key es el nombre de una columna
        y el value es una lista de valores para dicha columna. Despues simplemente le pasamos este diccionario al metodo DataFrame 
        de Pandas. Devolvemos los valores en este formato "tabla" --> DataFrame
        '''
        nombres_emp = []
        salario_emp = []
        for empleado in self.empleados:
            nombres_emp.append(empleado.nombre) 
            salario_emp.append(float(empleado.salario))
        diccionario_de_datos = {'Nombre': nombres_emp, 'Salario': salario_emp}
        return pd.DataFrame(diccionario_de_datos)

    def media_salarial(self):
        '''
        Método que devuelve la media salarial de todos los empleados de un departamento. Con self.crea_dataframe_empleado() obtenemos 
        el dataframe con los nombres y salarios de todos los empleados del departamento. Con ['Salario'] le indicamos la columna con la
        que queremos trabajar. Y por ultimo con .mean() calcula la media se todos los valores de dicha columna.
        '''
        return self.__crea_dataframe_empleado()['Salario'].mean()

    def reporte_salarios(self):
        '''
        Método que devuelve un dataframe con todos los valores ordenados por salario de mayor a menor de todos los empleados
        de un departamento. Con self.crea_dataframe_empleado() obtenemos el dataframe con los nombres y salarios de todos los empleados
        del departamento sin ordenar. Con sort_values('Salario', ascending=False) le pedimos que ordene el dataframe segun el salario
        y de manera descendente (ascending = False)
        '''
        return self.__crea_dataframe_empleado().sort_values('Salario', ascending=False)

    def muestra_empleados(self):
        '''
        Funcion para mostrar los empleados que pertenecen a un departamento
        '''
        if self.empleados != []:
            for emp in self.empleados:
                print(emp)
        else:
            print('\nEste departamento aun no tiene empleados.')