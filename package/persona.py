
class Persona():   
    def __init__(self, nombre:str, apellido:str, fecha_de_nacimiento:str, dni:str, direccion:list):
        self.nombre = nombre
        self.apellido = apellido
        self.fecha_de_nacimiento = fecha_de_nacimiento
        self.dni = dni
        self.direccion = direccion

    def __str__(self):
        return f'\n{self.nombre}\n{self.apellido}\n{self.fecha_de_nacimiento}\n{self.dni}\n{self.direccion}\n'

    def getNombreCompleto(self):
        return self.nombre + ' ' + self.apellido
        

    def getDia(self):
        dia = self.fecha_de_nacimiento.split('-')
        return dia[0]
    def getMes(self):
        mes = self.fecha_de_nacimiento.split('-')
        return mes[1]
    def getAño(self):
        año = self.fecha_de_nacimiento.split('-')
        return año[2]

    def setDia(self, hdia = None):
        dia = self.fecha_de_nacimiento.split('/')
        if hdia == None:
            return dia[0]
        else:
            return hdia

    def setMes(self, hmes=None):
        mes = self.fecha_de_nacimiento.split('/')
        if hmes == None:
            return mes[1]
        else:
            return hmes
    
    def setAño(self, haño=None):
        año = self.fecha_de_nacimiento.split('/')
        if haño == None:
            return año[2]
        else:
            return haño

individuo = Persona('Ramon', 'De Pitis', '21-2-1968', '53728994T', 'Calle caballo' )

print(individuo)
print(individuo.getNombreCompleto())
print(individuo.getDia())
print(individuo.getMes())
print(individuo.getAño())
print(individuo.setDia(25))
print(individuo.setMes(11))
print(individuo.setAño(1965))


class Usuario:
    email = 'pbarneto25@gmail.com'
    contraseña = '198919'
    activo = True
    
    def __init__(self, email, contraseña):
        self.email = email
        self.contraseña = contraseña

    def validation(self, param_email, param_contraseña):
        if (self.email == param_email) and (self.contraseña == param_contraseña):
            return True
        else:
            return False
    
anonimo = Usuario('pbarneto25@gmail.com', '198919')
print(anonimo.validation('pbarneto25@gmail.com', '198919'))


class Departamento():
    def __init__(self, departamento_nombre:str, departamento_telefono:str):

        self.departamento_nombre = departamento_nombre
        self.departamento_telefono = departamento_telefono
    def __str__(self):
        return f'\n Nombre del departamento: {self.departamento_nombre}\n Teléfono del departamento: {self.departamento_telefono}'

departamento = Departamento('Desarrollo','916301004')
print(departamento)