matriz = [[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
matrizT = [[0,0,0,0],[0,0,0,0],[0,0,0,0]]
soma = 0
diagonal = []
for l in range(4):
    for c in range(3):
        matriz[l][c] = int(input(f'Insira o elemento da {l+1}ª linha x {c+1}ª coluna: '))

for l in range(4):
    for c in range(3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print()

for l in range(3):
    for c in range(4):
        matrizT[l][c] = matriz[c][l]
        print(f'[{matrizT[l][c]:^5}]', end='')
    print()

