n = int(input('Insira um número para calcular seu fatorial: '))
fatorial = 1
print(f'{n}!', end=' = ')
while n > 0:
    if n == 1:
        print(f'{n}', end='')
    else:
        print(f'{n}', end='x')
    fatorial *= n
    n -= 1
print(f' = {fatorial}')