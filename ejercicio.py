class cuentaCorriente():

    def __init__(self,numero, titular, saldo):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo

    def getDatos(self):
        return "El numero de cuenta es: " + self.numero + " y el titular es: "+ self.titular + " y el saldo: " + str(self.saldo)

    def ingresar(self,cantidad):
        self.saldo = self.saldo + cantidad
    def retirar(self,cantidad):
        self.saldo = self.saldo - cantidad

cuenta1 = cuentaCorriente("0049-2100-7895-5555","evander",150000)
print(cuenta1.getDatos())
cuenta1.ingresar(50000)
print(cuenta1.getDatos())
cuenta1.retirar(4555)
print(cuenta1.getDatos())
