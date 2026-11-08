numeros =[1,2,3,4,5,6,7,8,9,10]
impar = 0
par = 0
for n in numeros:
    if n % 2 == 0:
        par += 1
    else:
        impar += 1
print("O numero de pares e ", par, " e o numero de impares e ", impar)
