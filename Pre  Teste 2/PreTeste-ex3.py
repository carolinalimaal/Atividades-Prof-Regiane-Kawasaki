tamanho = int(input('Insira o tamanho da matriz quadrada: '))
print()

matriz = [[0 for _ in range(tamanho)] for _ in range(tamanho)]
matrizID = [[0 for _ in range(tamanho)] for _ in range(tamanho)]

for l in range(tamanho):
    for c in range(tamanho):
        matriz[l][c] = int(input(f'ELEMENTO [{l+1} x {c+1}]: '))
        if l == c:
          matrizID[l][c] = 1
print()
  
print('MATRIZ: ')
for l in range(tamanho):
    for c in range(tamanho):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
    
if matriz == matrizID:
    print('A matriz acima é uma IDENTIDADE.')
else:
    print('A matriz acima NÃO é uma IDENTIDADE.')