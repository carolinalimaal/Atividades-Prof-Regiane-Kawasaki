from random import randint
vetor1 = []
vetor2 = []
dif = []
soma = []
prod = []
for i in range(10):
    vetor1.append(randint(0,11))
    vetor2.append(randint(0,11))
    dif.append(vetor1[i]-vetor2[i])
    soma.append(vetor1[i]+vetor2[i])
    prod.append(vetor1[i]*vetor2[i])

print(f'VETOR 1: {vetor1}')
print(f'VETOR 2: {vetor2}')
print(f'VETOR DIFERENÇA: {dif}')
print(f'VETOR SOMA: {soma}')
print(f'VETOR PRODUTO: {prod}')