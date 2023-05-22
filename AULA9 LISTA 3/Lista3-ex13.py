lista1 = [0]*12
lista2 = [0]*12
for i in range(0,12):
    num = int(input('Insira um número inteiro: '))
    lista1[i] = num
    if (i % 2) != 0:
        lista2[i] = num

print(f'LISTA INICIAL: {lista1}')
print(f'LISTA DAS POSIÇÕES ÍMPARES: {lista2}')
