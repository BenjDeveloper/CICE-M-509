
class Usuario():

    def __init__(self, email, clave, activo):
        self.email = email
        self.clave = clave
        self.activo = activo    # booleano

    def validacion(self, param_email, param_clave):
        return True if (param_email == self.email and param_clave == self.clave) else False
