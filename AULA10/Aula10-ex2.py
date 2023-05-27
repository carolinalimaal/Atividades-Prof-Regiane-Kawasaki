matriz = [[0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0]]
diagonal = [0]*5
for l in range(5):
    for c in range(5):
        matriz[l][c] = int(input(f'Insira o valor da {c+1}ª coluna da {l+1}ª linha: '))
for l in range(5):
    for c in range(5):
        print(f'[{matriz[l][c]:^5}]', end='')
        if l == c:
            diagonal[l] = matriz[l][c]
    print()
print(f'Os elementos da diagonal principal são {diagonal}')