palavras = ["casa", "carro", "bicicleta", "avião", "barco", "carro" ,"bicicleta"]
contadorrepetidos = 0
for p in palavras:
    
    for prep in palavras:
        if p == prep:
            contadorrepetidos += 1


    if contadorrepetidos > 1:
        palavras.remove(p)

    contadorrepetidos = 0
print(palavras)