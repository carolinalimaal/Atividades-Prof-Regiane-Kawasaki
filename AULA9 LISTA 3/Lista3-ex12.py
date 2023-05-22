from random import randint
vetor = [0]*50
soma = dp = 0
for i in range(0,50):
    vetor[i] = randint(1,10)
    soma += vetor[i]
for i in range(0,5):
    dp += (vetor[i]-(soma/50))**2  / 50
print(f'LISTA DAS ALTURAS: {vetor}')
print(f'A média das alturas é {soma/50}')
print(f'O desvio padrão das alturas é {(dp)**(1/2)}')
