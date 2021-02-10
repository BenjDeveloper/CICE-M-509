
class Usuario:
    def __init__ (self, email, clave, activo):
        self.email = email
        self.clave = clave
        self.activo = activo


    def __str__ (self):
        return f''': Email = {self.email}'''

    def validacion(self, param_email, param_clave):
        
        if param_email == self.email and param_clave == self.clave:
            if self.activo ==True:
                return True
            return False

        else: return False