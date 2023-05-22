num1 = int(input('Insira o 1º valor: '))
num2 = int(input('Insira o 2º valor: '))

if num1 > num2:
    maior = num1
else:
    maior = num2

mmc = maior

while (mmc % num1) != 0 or (mmc % num2) != 0:
    mmc += maior

print(f'O MMC entre {num1} e {num2} é {mmc}')
