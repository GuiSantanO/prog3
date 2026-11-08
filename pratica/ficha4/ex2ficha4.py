class CarteiraDigital:
    def __init__(self,titular,saldo):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        if valor < 0:
            print("Value Error")
        else:
            self.saldo += valor

    def pagar(self, valor):
        if valor < 0:
            print("Value Error")
        elif valor <= self.saldo:
            self.saldo -= valor
        else:
            print("Value Error")

    def mostrar_saldo(self):
        print(f"Titular: {self.titular}, Saldo: {self.saldo}")

minha_carteira = CarteiraDigital("JGuilherme", 100)

minha_carteira.depositar(-50)
minha_carteira.mostrar_saldo()

        
        

 