# 5.- Cree una clase Usuario con los siguientes atributos:
#     email:str
#     clave:str
#     activo:bool

# 6.- Edite la clase Usuario y agregele un metodo:
#     def validacion(self, param_email, param_clave):
#         pass
#     la funcion validacion recibe 2 parametros externos -> param_email y param_clave  
#     y revisa si son iguales con los de la clase -> self.email y self.clave
#     tambien debera verificar si ese encuentra activo o no self.activo -> ( True o False )
#     y por ultimo devuelve True en caso de que sean iguales y False en caso de que no


class Usuario():
    email = 'willyg.ginestal@gmail.com'
    contraseña = '101010'
    #print('\nEl email del usuario es:',email)
    #print('La contraseña del usuario es:',contraseña,'\n')
    activo = True

    #print('Vamos a validar este email y esta contraseña...\n')
    
    def __init__(self, email, contraseña):
        self.email = email
        self.contraseña = contraseña

    def validation(self, param_email, param_contraseña):
        if (self.email == param_email) and (self.contraseña == param_contraseña):
            return True 
        else:
            return False
            
"""    
anonimo = Usuario('willyg.ginestal@gmail.com', '101010')
print('El email introducido es willyg.ginestal@gmail.com''\n''La contraseña introducida es 101010\n')
print('Comprobamos....',anonimo.validation('willyg.ginestal@gmail.com', '101010'))
print('El email y contraseña son correctos!!!\tContinuemos...\n')
"""
