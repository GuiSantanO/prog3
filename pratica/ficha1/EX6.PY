
def pesquisa_binaria(lista, valor):
    inicio = 1
    fim = len(lista) - 1
    
    while inicio <= fim:
        meio = (inicio + fim) // 2
        pesquisa = lista[meio]
        if pesquisa == valor:
            return "existe"
        if pesquisa > valor:
            fim = meio - 1
        else:
            inicio = meio + 1
    return "não existe"


numeros = [10 , 9 , 8 , 7 , 6 , 5 , 4 , 3 , 2 , 1]

sorted_numeros = sorted(numeros)

input = int(input("Introduza um numero de 1 a 10: "))

print(pesquisa_binaria(sorted_numeros, input))
