resp = 'Ss'
idade = menor = maior = 0
while resp in 'Ss':
    idade = int(input('Qual a sua idade? '))
    if idade < 18:
        menor += 1
    if idade > 60:
        maior += 1 
    resp = input('Deseja continuar? [S]/[N]: ')
print(f'{menor} pessoa(s) menor(es) de 18 anos e {maior} maior(es) de 60 anos.')