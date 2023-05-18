n = int(input('Insira a quantidade de elementos: '))
soma = 1
a = 0
for i in range(1,n):
    a = 1/(1+i)
    soma += a
print(f'A soma de 1 + 1/2 + 1/3 + ... + 1/n é igual a, sendo n={n}: {soma:.2f}')