matriz = [[0 for l in range(10)] for c in range(10)]
diagonalP = [0]*10
i = 0 
for l in range(10):
    for c in range(10):
        matriz[l][c] = int(input(f'Insira o elemento da posição [{l+1} x {c+1}]: '))

for l in range(10):
    for c in range(10):
        if l == c:
            diagonalP[i] = matriz[l][c]
            i += 1
        print(f'[{matriz[l][c]:^8}]', end='')
    print()

print(f'A diagonal principal dessa matriz acima contém os elemntos: {diagonalP}')