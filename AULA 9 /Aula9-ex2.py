matriz = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
soma = 0
diagonal = []
for l in range(4):
    for c in range(4):
        matriz[l][c] += int(input(f'Insira o elemento da {l+1}ª linha x {c+1}ª coluna: '))
        soma += matriz[l][c]

for l in range(4):
    for c in range(4):
        print(f'[{matriz[l][c]:^5}]', end='')
        if l == c:
            diagonal += [matriz[l][c]]
    print()

print(f'A diagonal principal é {diagonal}')
