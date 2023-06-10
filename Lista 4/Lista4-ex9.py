matriz1 = [[0 for l in range(3)] for c in range(3)]
matriz2 = [[0 for l in range(3)] for c in range(3)]
produto = [[0 for l in range(3)] for c in range(3)]

print('MATRIZ 1:')
for l in range(3):
    for c in range(3):
        matriz1[l][c] = int(input(f'Elemento [{l+1} x {c+1}]: '))

print('MATRIZ 2:')
for l in range(3):
    for c in range(3):
        matriz2[l][c] = int(input(f'Elemento [{l+1} x {c+1}]: '))
    
for l in range(3):
    for c in range(3):
        for a in range(3):
            produto[l][c] += matriz1[l][a] * matriz2[a][c]

print('PRODUTO:')
for l in range(3):
    for c in range(3):
        print(f'[{produto[l][c]:^5}]', end='')
    print()