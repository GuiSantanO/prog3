class Lampada:
    def __init__(self, divisao, ligada=False):
        self.divisao = divisao
        self.ligada = ligada
        self.descricao = f"Lâmpada na divisão {self.divisao}, ligada: {self.ligada}"

    def ligar(self):
        self.ligada = True
        self.descricao = f"Lâmpada na divisão {self.divisao}, ligada: {self.ligada}"

    def desligar(self):
        self.ligada = False
        self.descricao = f"Lâmpada na divisão {self.divisao}, ligada: {self.ligada}"


lampadaCozinha = Lampada("Cozinha")
lampadaBathroom = Lampada("Casa de banho")

lampadaCozinha.ligar()
lampadaBathroom.ligar()

print(lampadaBathroom.descricao)
print(lampadaCozinha.descricao)
