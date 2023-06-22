capital = 1000
mes = 0 
capitalF = 15000
while capital < capitalF:
    capital += capital*0.03
    mes += 1

print(f'Após {mes//12} anos e {mes%12} meses Sr. Pantera conseguirá o valor de R$15000,00.')
