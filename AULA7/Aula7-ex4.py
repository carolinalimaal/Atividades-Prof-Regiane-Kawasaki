print("""===========================
         CARDÁPIO
===========================
Cachorro quente 100 R$ 1.20
Bauru Simples   101 R$ 1.30
Bauru com ovo   102 R$ 1.50
Hambúrguer      103 R$ 1.20
Cheeseburguer   104 R$ 1.30
Refrigerante    105 R$ 1.00
Fechar pedido   000\n""")

cardapio = {'100':1.2, '101':1.3, '102':1.5, '103':1.2, '104':1.3, '105':1.0, '000':0.0}
precoUnid = ''
precoTot = 0
listaCodigo, listaPreco, listaQuant = [], [], []

while True:
    codigo = input('INSIRA O CÓDIGO DO PEDIDO: ')
    listaCodigo.append(codigo)
    for n in codigo:
        precoUnid = cardapio[codigo]
    listaPreco.append(precoUnid)
    if codigo == '000':
        print('========================')
        print('    RESUMO DO PEDIDO    ')
        print('========================')
        print(' ITEM    R$  QUANT')
        for item in zip(listaCodigo, listaPreco, listaQuant):
            print(item)
        print(f'TOTAL A PAGAR: R${precoTot :.2f}')
        break
    quant = int(input('QUANTIDADE: '))
    listaQuant.append(quant)
    precoTot += precoUnid * quant
    
