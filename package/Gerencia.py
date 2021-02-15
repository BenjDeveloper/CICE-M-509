
import csv
from package.departamento import Departamento
from package.empleado import Empleado
class Gerencia(object):
    def __init__(self, empresa):
        self.empresa=empresa
        # self.departamento=[]
        self.departamento=dict()
        self.__allempleados=[]

    def __str__(self):
        return f'{self.empresa} \ndepartamentos: {", ".join([d.nombre for d in self.departamento])}'

    def setDepartamentos(self, *departamentos):
        # for i in departamentos:
        #     self.departamento.append(i)
        for i in departamentos:
            self.departamento[i.nombre]=i
    
    def setDepartamentosCSV(self, csvfile):
        filedepartamentos=open(csvfile,"r")
        readfile=csv.reader(filedepartamentos)
        rownumber=0
        for row in readfile:
            if rownumber==0:
                rownumber+=1
                continue
            # print(row[0],row[1])
            midepartamento=Departamento(row[0],row[1])
            # self.departamento.append(midepartamento)
            self.setDepartamentos(midepartamento)
            
            fileempleados=open(row[2],"r")
            readempleados=csv.reader(fileempleados)
            rownumberemp=0
            for empData in readempleados:
                if rownumberemp==0:
                    rownumberemp+=1
                    continue
                miempleado=Empleado(*empData)
                midepartamento.setEmpleados(miempleado)
            fileempleados.close()
        fileempleados.close()

    # def getDepartamento(self,nombredepartamento):
    #     for i,d in enumerate(self.departamento):
    #         # print(d.nombre,self.departamento[i])
    #         if nombredepartamento==d.nombre:
    #             return self.departamento[i]
    #     return None
    def getDepartamento(self,nombredepartamento):
        if nombredepartamento in self.departamento:
            return self.departamento[nombredepartamento]
        return None 
    
    def updateAllEmpleados(self):
        # print(empleadosObj,type(empleadosObj))
        for depart in self.departamento.values():
            for empleado in depart.empleados:
                # print(empleado,type(empleado))
                if empleado not in self.__allempleados:
                    self.__allempleados.append(empleado)
    
    # @property
    def getAllEmpleados(self):
        return self.__allempleados
            