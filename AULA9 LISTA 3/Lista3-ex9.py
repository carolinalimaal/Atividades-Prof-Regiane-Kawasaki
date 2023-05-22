num1 = int(input('Insira o 1º valor: '))
num2 = int(input('Insira o 2º valor: '))
save1= num1
save2 = num2

if num2 > num1:
    num1, num2 = num2, num1 

while num2 != 0:
    num1, num2 = num2 , (num1 % num2) 

mdc = num1 

print(f'O MDC entre {save1} e {save2} é {mdc}')