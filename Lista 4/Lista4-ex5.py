matriz1 = [[0 for l in range(5)] for c in range(5)]
diagonalSec = [0]*5
soma = i = 0

for l in range(5):
    for c in range(5):
        matriz1[l][c] = int(input(f'Insira o elemento da posição [{l+1} x {c+1}]: '))
    
for l in range(5):
    for c in range(5):
        if (l + c) == 4:
            diagonalSec[i] = matriz1[l][c]
            soma += diagonalSec[i]
            i += 1
        print(f'[{matriz1[l][c]:^5}]', end='')
    print()

print(f'A diagonal secundária contém os elementos {diagonalSec} e a soma desses elementos é {soma}')