
# 7.- Cree una clase Empleado que herede de Persona y Usuario, adicionalmente posea el atributo:
# #     salario:float
# #     horario:str


class Empleado(Persona, Usuario):
    
    def __init__(self, salario:float, horario:str, email, contraseña ):
        Usuario.__init__(self,  email, contraseña)
        self.salario = salario
        self.horario = horario
    #def __float__(self):
    #    return f'\n Salario: {self.salario}

    def __str__(self):
        return f'\n Horario: {self.horario} {self.email } {self.contraseña } {self.salario }'

e1 = Empleado(1235,18, 'email', 'contraseña')

print('AQUI ES CHAMITO:',e1)