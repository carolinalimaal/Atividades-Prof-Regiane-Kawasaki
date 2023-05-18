n = int(input('Insira o tamanho do vetor: '))
vetor = [0]*n
vetorDif = [0]*n
i = soma = media = 0
while n > 0:
    vetor[i]= int(input(f'Insira o {i+1}º valor: '))
    soma += vetor[i]
    n -= 1
    i += 1 
media = soma/i

while i > 0:
    vetorDif[n] = vetor[n] - media
    n += 1
    i -= 1

print(f'A média dos valores do vetor é igual a {media}')
print(f'O vetor diferença é igual a {vetorDif}')
