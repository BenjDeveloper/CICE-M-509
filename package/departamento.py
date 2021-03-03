

class Departamento():
    # departYemplea=dict()
    def __init__(self, nombredepartamento, telefonodepartamento):
        self.telefono=telefonodepartamento
        self.nombre=nombredepartamento
        # self.departYemplea[self.nombre]=[]
        # self.empleados=[]
        self.empleados=dict()
        self.supervisor = None

        
    def __str__(self):
        return f"nombre del departamento: {self.nombre}, telefono del departamento: {self.telefono}"
    
    def setEmpleados (self,*listempl):
        # self.empleados.extend(listempl)
        # for emp in listempl:
        #     self.empleados.append(emp)
        #     emp.pertenece_departamento=self
        for empl in listempl:
            self.empleados[empl.dni]=empl
    
    def getEmpleados (self,nombreempleado):
        if nombreempleado in self.departamento:
            return self.departamento[nombredepartamento]
        return None
    
    def getSalario(self,emp):
        return emp.salario

    def printEmp(self):
        empsorted=self.empleados.copy()
        empsorted.sort(reverse=True,key=self.getSalario)
        for emp in empsorted:
            print(f"Nombre: {emp.nombre:<15} Apellido: {emp.apellido:<15} Salario: {emp.salario}")

    def mediaSal(self):
        listaSal=list(map(lambda emp: emp.salario, self.empleados))
        return sum(listaSal)/len(listaSal)