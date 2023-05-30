matriz = []
soma = media = 0
for l in range(3):
    linha = []
    for c in range(3):
        num = int(input(f'Insira o item da {l+1}ª linha x {c+1}ª coluna: '))
        soma += num
        linha.append(num)
    matriz.append(linha)

for i in range(3):
    print(f'{matriz[i]}')

print(f'A soma dos elementos da matriz é {soma} e a média é {soma/9}')
