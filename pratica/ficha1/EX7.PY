def max_Sep_Bin(N):
    num_binario = bin(N)[2:] #usei a funcao bin para calcular o binario do numero e depois usei o slice para remover os dois primeiros caracteres que sao sempre 0b
    cont_zeros = 0
    primeiro_1 = False #enquanto estiver false significa que nao aparareceu o primeiro 1
    maior_cont_0 = 0

    for numero in num_binario:

        if numero == '1':


            if primeiro_1 and cont_zeros > maior_cont_0:
                maior_cont_0 = cont_zeros
            primeiro_1 = True
            cont_zeros = 0


        else:
            cont_zeros = cont_zeros + 1



    return maior_cont_0


print(max_Sep_Bin(257))     



