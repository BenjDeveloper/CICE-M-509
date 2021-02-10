


class Persona:
    
    def __init__(self , nombre:str,apellido:str,dni:str,fecha_de_nacimiento:str,direccion:list):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni 
        self.fecha_de_nacimiento = fecha_de_nacimiento
        self.direccion = direccion

    def getnombreapellido(self):
        return f"{self.nombre} {self.apellido}"

    def getDia(self):
        fecha = self.fecha_de_nacimiento.split('-')
        return fecha[0]

    def getMes(self):
        fecha = self.fecha_de_nacimiento.split('-')
        return fecha[1]

    def getAño(self):
        fecha = self.fecha_de_nacimiento.split('-')
        return fecha[2]

    def setDia(self, dia):
        fecha = self.fecha_de_nacimiento.split("-")
        fecha[0]= dia 
        self.fecha_de_nacimiento = fecha[0]+'-'+fecha[1]+'-'+fecha[2]

    def setMes(self, mes):
        fecha = self.fecha_de_nacimiento.split("-")
        fecha[1]= mes
        self.fecha_de_nacimiento = fecha[0] + "-" + fecha[1] + "-" +fecha[2]
        
    def  setAño(self, año):
        fecha = self.fecha_de_nacimiento.split("-")
        fecha[2]= año
        self.fecha_de_nacimiento = fecha[0] + "-" + fecha[1] + "-" + fecha[2]

    def __str__(self):
        return f"{self.nombre}:{self.apellido}:{self.dni}"







objeto = Persona( 'Evander', 'Lopez', "00055m", "19-7-1992","povedilla")
print(objeto)