n = 50
nota = soma = acima = abaixo = 0
notas = [0]*50
for i in range(0,n):
    nota = float(input(f'Insira a {i+1}ª nota: '))
    notas[i] = nota
    soma += nota

for i in range(0,n):
    if notas[i] > (soma/n) + (0.1*(soma/n)):
        acima += 1
    if notas[i] < (soma/n) - (0.1*(soma/n)):
        abaixo += 1

print(f'A média das notas é {soma/n} pts.')
print(f'{acima} notas estão 10% acima da média e {abaixo} estão 10% abaixo da média.')    