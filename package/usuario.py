class Usuario(object):
    #CONSTRUCTOR
    def __init__(self, email:str,clave:str,activo:bool):
        self.email = email 
        self.clave = clave 
        self.activo = activo

    def __str__(self):
        return f'Usuario (email): {self.email}, Activo: {self.activo}'

    def validacion(self, param_email, param_clave):
        return True if (param_email == self.email and param_clave == self.clave) else False
