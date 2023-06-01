matriz1 = [[0,0,0], [0,0,0]]
matriz2 = [[0,0,0], [0,0,0]]
soma = [[0,0,0], [0,0,0]]
for l in range(2):
    for c in range(3):
        matriz1[l][c] = int(input(f'MATRIZ 1 ({l+1}x{c+1}): '))
        
for l in range(2):
    for c in range(3):
        matriz2[l][c] = int(input(f'MATRIZ 2 ({l+1}x{c+1}): '))
        soma[l][c] = (matriz1[l][c] + matriz2[l][c]) 

print(f'SOMA')
for l in range(2):
    for c in range(3):
        print(f'[{soma[l][c]}]', end='')
    print()