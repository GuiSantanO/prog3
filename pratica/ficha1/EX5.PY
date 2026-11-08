numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
k = 0

while k < 1 or k > len(numeros):
    print("Introduza um numero de 1 a 10")
    k = int(input())


resultado = numeros[-k:] + numeros[:-k]

print("O resultado da rotação é: ", resultado)
