from random import randint
vetor = [0]*10
soma = dp = 0
for i in range(0,10):
    vetor[i] = randint(1,10)
    soma += vetor[i]
    dp += (vetor[i] - (soma/10))**2

print(f'LISTA DAS ALTURAS: {vetor}')
print(f'A média das alturas é {soma/10}')
print(f'O desvio padrão das alturas é {(dp/10)**(1/2)}')