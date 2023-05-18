num = i = soma = 0
while num >= 0:
    num = int(input('Insira um valor: '))
    if num >= 0: #Para calcular somente a média entre os valores positivos
        i += 1
        soma += num
print(f'A média dos valores digitados é {soma/i}') 