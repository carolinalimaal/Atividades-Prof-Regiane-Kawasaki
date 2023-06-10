MAT = [[0 for l in range(5)] for c in range(5)]
somaL = [0]*5
somaC = [0]*5
i = j = 0

for l in range(5):
    for c in range(5):
        MAT[l][c]= int(input(f'Posição [{l+1} x {c+1}]: '))
        somaL[i] += MAT[l][c]
    i += 1

for l in range(5):
    for c in range(5):
        somaC[j] += MAT[c][l]
        print(f'[{MAT[l][c]:^5}]', end='')
    j += 1
    print()

print('SOMA DAS LINHAS:')
print(f'1: {somaL[0]}')
print(f'2: {somaL[1]}')
print(f'3: {somaL[2]}')
print(f'4: {somaL[3]}')
print(f'5: {somaL[4]}\n')

print('SOMA DAS COLUNAS:')
print(f'1: {somaC[0]}')
print(f'2: {somaC[1]}')
print(f'3: {somaC[2]}')
print(f'4: {somaC[3]}')
print(f'5: {somaC[4]}')