soma = 0
cont = 0
num = 0
for i in range(0,20):
    num = int(input('Insira um valor inteiro: '))
    if num > 0:
        soma += num
    elif num < 0:
        cont += 1
print(f'A soma dos números positivos é {soma} e a quantidade de números negativos é {cont}')