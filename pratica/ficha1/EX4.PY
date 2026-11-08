numero = 0
while numero < 1 or numero > 10:
    print("Introduza um numero de 1 a 10")
    numero = int(input())

for i in range(1, 11):
    print(numero, "x", i, "=", numero * i)

