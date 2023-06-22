from random import randint

vetor = [0]*10
acima = [0]*10
soma = 0 

for i in range(10):
    vetor[i] = randint(0,10)
    soma += vetor[i]

print(vetor)
print(f'A média dos números do vetor é {soma/10}')
print(f'Os valores acima da média são:')
for i in range(10):
    if vetor[i] > (soma/10):
        print(f'{vetor[i]} -> INDEX {i}')