matriz1 = [[0 for l in range(3)] for c in range(3)]

for l in range(3):
    for c in range(3):
        matriz1 = int(input(f'Elemento [{l+1} x {c+1}]: '))
   
matriz2 = matriz1 
matriz3 = [[0 for l in range(3)] for c in range(3)]

print('MATRIZ 1')
for l in range(3):
    for c in range(3):
        print(f'[{matriz1[l][c]:^5}]', end='')
    print()

print('MATRIZ 1 AO QUADRADO')
for l in range(3):
    for c in range(3):
        for a in range(3):
            matriz3[l][c] += matriz1[l][a] * matriz2[a][c]
        print(f'[{matriz3[l][c]:^5}]', end='')
    print()
