from dataclasses import dataclass
total = int(input('Insira a quantidade de livros a serem registrados: '))

@dataclass
class Livro:
    titulo: str
    autor: str
    ano: int

registro = [None] * total
for i in range(total):
    registro[i] = Livro('', '', 0)
    print('='*30)
    print(f'            LIVRO {i+1}')
    print('='*30)
    registro[i].titulo = input('Título: ')
    registro[i].autor = input('Autor: ')
    registro[i].ano = int(input('Ano de lançamento: '))
print()

anoRef = int(input('Digite o ano de referência: '))
print(f'Livros lançados antes de {anoRef}')
for i in range(total):
    if registro[i].ano < anoRef:
        print(f' - {registro[i].titulo} - {registro[i].autor} - {registro[i].ano}')