from dataclasses import dataclass

@dataclass
class PesquisaShopping:
    idade: int
    frequencia: int
    pracaAlimentacao: int
    sugestao: str

pesquisa = [None] * 3
cont = menor18 = entre1865 = maior65 = exc = bom = precisaMelhorar = 0

for i in range(3):
    cont += 1
    print('='*25)
    print(f'      ENTREVISTADO {i+1}')
    print('='*25)
    pesquisa[i] = PesquisaShopping(0, 0, 0, '')

    pesquisa[i].idade = int(input(' Qual a sua idade? ')) #Bloco para verificar a idade
    if pesquisa[i].idade < 18:
        menor18 += 1
    elif 18 <= pesquisa[i].idade < 65:
        entre1865 += 1
    else:
        maior65 +=1
    print()

    pesquisa[i].frequencia = int(input(' [1]Diário\n [2]Semanal\n [3]Quase nunca\n Qual a sua frequência no shopping? ')) #Bloco para verificar a frequência
    print()

    pesquisa[i].pracaAlimentacao = int(input(' [1]Execente\n [2]Boa\n [3]Precisa melhorar\n Qual a sua nota para a Praça de Alimentação do shoppng? ')) #Bloco para verificar a nota da P.A.
    print()
    if pesquisa[i].pracaAlimentacao == 1:
        exc += 1
    elif pesquisa[i].pracaAlimentacao == 2:
        bom += 1
    else:
        precisaMelhorar += 1

    if pesquisa[i].pracaAlimentacao == 3: #Bloco para coletar as sugestões, se preciso
        pesquisa[i].sugestao = input(' Sugestão de melhoria para a PRAÇA DE ALIMENTAÇÃO: ')
        print()

print('='*60)
print(f'Porcentagem de entrevistados de acordo com a idade:\n - MENOR QUE 18 ANOS: {menor18*100/cont:.2f}%\n - ENTRE 18 E 65 ANOS: {entre1865*100/cont:.2f}%\n - MAIOR QUE 65 ANOS{maior65*100/cont:.2f}%\n')
print(f'Porcentagem de avalições da Praça de Alimentação:\n - EXCELENTE: {exc*100/cont:.2f}%\n - BOM: {bom*100/cont:.2f}%\n - PRECISA MELHORAR: {precisaMelhorar*100/cont:.2f}%\n')
print('LISTA DE SUGESTÕES')
for i in range(cont):
    print(f' - ENTREVISTADO {i+1}: {(pesquisa[i].sugestao).capitalize()}')
