numeros = []

num = int(input('Insira um valor inteiro: '))
while num != -1:
    numeros.append(num)
    num = int(input('Insira um valor inteiro: '))
print(f'O maior número digitado foi {max(numeros)} e o menor foi {min(numeros)}.')
