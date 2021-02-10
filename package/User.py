

class User (object):
    def __init__(self,email:str,clave:str,activo=True):
        self.email=email
        self.clave=clave
        self.activo=activo
    def __str__(self):
        activostr="online" if self.activo==True else "ofline"
        # return f"email: {self.email}, clave: {self.clave}, activo: {activostr}"
        return f"email: {self.email}, activo: {activostr}"

    def validacion(self, param_email, param_clave):
        if param_email==self.email and param_clave==self.clave and self.activo==True:
            return True
        return False

# user1=User("qwerty@asdf","123456",True)
# print(user1)
# print(user1.validacion("aaaaa","123456"))
# print(user1.validacion("qwerty@asdf","123456"))