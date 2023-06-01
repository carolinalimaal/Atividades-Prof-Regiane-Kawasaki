vetor = [0]*20
vetorP = []
vetorI = []
maior = menor = 0
for j in range(10):
    vetor[j] = int(input(f'Insira o {j+1}º valor: '))
    if vetor[j] % 2 == 0:
        if j == 0:
            maior = vetor[j]
            menor = vetor[j]
            vetorP.append(maior)
        else:
            if vetor[j] > maior:
                maior = vetor[j]
                vetorP.append(maior)
            elif vetor[j] < menor:
                menor = vetor[j]
                vetorP.insert(0,menor)
    else:
        if j == 0:
            maior = vetor[j]
            menor = vetor[j]
            vetorI.append(menor)
        else:
            if vetor[j] > maior:
                maior = vetor[j]
                vetorI.insert(0, maior)
            elif vetor[j] < menor:
                menor = vetor[j]
                vetorI.append(menor) #rever
print(vetor)
print(vetorI)
print(vetorP)