matriz = [[0 for l in range(4)] for c in range(4)]
i = 0
numMaior10 = [0] * 16

for l in range(4):
    for c in range(4):
        matriz[l][c] = int(input(f'Insira o elemento da posição [{l+1} x {c+1}]: '))
        if matriz[l][c] > 10:
            numMaior10[i] = matriz[l][c]
            i += 1

for l in range(4):
    for c in range(4):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print(f'Essa matriz tem {i} elementos maiores que 10, sendo eles {numMaior10[:i]} ')