matriz = [[0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0]]
soma = 0
for l in range(5):
    for c in range(5):
        matriz[l][c] = int(input(f'Insira o valor da {c+1}ª coluna da {l+1}ª linha: '))
        soma += matriz[l][c]
for l in range(5):
    for c in range(5):
        print(f'[{matriz[l][c]}]', end='')
    print()
print(f'A soma dos elementos da matriz é {soma}.')
