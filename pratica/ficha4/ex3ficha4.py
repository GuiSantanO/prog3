class Turma:
    escola = "Escola ABC"
    def __init__(self, nome):
        self.nome = nome
        self.alunos = []
        self.contador = 0

    def adicionar(self,valor):
        self.alunos.append(valor)
        self.contador = self.contador +1

    def listar(self):
        if self.contador > 1 and self.contador < 1: #if para verificar se a turma tem mais de 1 aluno
            print(f"A turma tem {self.contador} alunos")

        else:
            print(f"A turma tem {self.contador} aluno")



turmaA = Turma("A")

turmaA.adicionar("Ana")
turmaA.listar()

turmaB= Turma("B")
turmaB.adicionar("Ana")
turmaB.listar()




    
        

        
        

        




    