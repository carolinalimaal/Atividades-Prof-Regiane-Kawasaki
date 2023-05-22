n = int(input('Insira o número de linhas do triângulo de pascal: '))
triangulo = [[1]]


for i in range(1, n):
    linha = [1]
    for j in range (1, i):
        linha.append(triangulo[i-1][j-1] + triangulo[i-1][j])
    linha.append(1)
    triangulo.append(linha)

for linha in triangulo:
    print(linha)