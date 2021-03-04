
import csv
from package.departamento import Departamento
from package.empleado import Empleado
class Gerencia(object):
    def __init__(self, empresa):
        self.empresa=empresa
        # self.departamentos=[]
        self.departamentos=dict()
        self.__allempleados=[]

    def __str__(self):
        return f'{self.empresa} \ndepartamentos: {", ".join([d for d in self.departamentos])}'

    def setDepartamentos(self, *departamentos):
        # for i in departamentos:
        #     self.departamentos.append(i)
        for i in departamentos:
            self.departamentos[i.nombre]=i
    
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
            # self.departamentos.append(midepartamento)
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

    def export_to_CSV(self):
        filecreate=open("exportCSV\departamentos.csv","w", newline='')
        depcsv=csv.writer(filecreate)
        depheader=["departamento","telefono","ruta csv empleados"]
        empheader=["nombre","apellido","fecha","dni","direccion","email","clave","salario","horario"]
        depcsv.writerow(depheader)
        cont=1
        for depart in self.departamentos.values():
            filename=f"exportCSV\empleados{str(cont)}.csv"
            fileemp=open(filename,"w", newline='')
            empcsv=csv.writer(fileemp)
            empcsv.writerow(empheader)
            for emp in depart.empleados.values():
                # print([emp.nombre,emp.apellido,emp.fechastr,emp.dni,emp.direccion,emp.email,emp.clave,emp.salario,emp.horario])
                empcsv.writerow([emp.nombre,emp.apellido,emp.fechastr,emp.dni,emp.direccion,emp.email,emp.clave,emp.salario,emp.horario])
            depcsv.writerow([depart.nombre,depart.telefono,filename])
            cont+=1

    def getDepartamento(self,nombredepartamento):
        if nombredepartamento in self.departamentos:
            return self.departamentos[nombredepartamento]
        return None 
    
    def updateAllEmpleados(self):
        # print(empleadosObj,type(empleadosObj))
        for depart in self.departamentos.values():
            for empleado in depart.empleados.values():
                # print(empleado,type(empleado))
                if empleado not in self.__allempleados:
                    self.__allempleados.append(empleado)
    
    # @property
    def getAllEmpleados(self):
        return self.__allempleados
            