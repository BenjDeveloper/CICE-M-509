

class Gerencia(object):
    def __init__(self, empresa):
        self.empresa=empresa
        self.departamento=[]

    def __str__(self):
        return f'{self.empresa} \ndepartamentos: {", ".join([d.nombre for d in self.departamento])}'

    def setDepartamentos(self, *departamentos):
        for i in departamentos:
            self.departamento.append(i)
