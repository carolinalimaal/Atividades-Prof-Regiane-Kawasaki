vetor1 = [0]*10
vetor2 = [0]*10
j = 0
for i in range(10):
    vetor1[i] = int(input(f'Insira o {i+1}º valor: '))
    if i % 2 == 0:
        vetor2[j] = vetor1[i]/2
        j += 1
    else:
        vetor2[j] = vetor1[i]*3
        j += 1

print(f'VETOR ORIGINAL: {vetor1}')
print(f'VETOR NOVO: {vetor2}')
