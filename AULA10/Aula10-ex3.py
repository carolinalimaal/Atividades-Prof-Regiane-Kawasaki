matriz1 = [[0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0]]
matriz2 = [[0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0]]
a = int(input('Digite um valor para multiplicar uma matriz: '))
for l in range(2):
    for c in range(2):
        matriz1[l][c] = int(input(f'Insira o valor da {c+1}ª coluna da {l+1}ª linha: '))
        matriz2[l][c] = matriz1[l][c]*a
print('MATRIZ ORIGINAL')
for l in range(2):
    for c in range(2):
        print(f'[{matriz1[l][c]:^5}]', end='')
    print()
print('MATRIZ APÓS O PRODUTO')
for l in range(2):
    for c in range(2):
        print(f'[{matriz2[l][c]:^5}]', end='')
    print()