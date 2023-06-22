from dataclasses import dataclass

@dataclass
class Aluno:
    nome: str
    nota: float

maiorNota = maiorNome = 0
num = int(input('Insira o número de alunos: '))
alunos = [None] * num
for i in range(num):
    alunos[i] = Aluno('', 0)
    print('='*30)
    print(f'            ALUNO {i+1}')
    print('='*30)
    alunos[i].nome = input('NOME: ')
    alunos[i].nota = float(input('NOTA: '))
    if i == 1:
        maiorNota = alunos[i].nota
        maiorNome = alunos[i].nome
    else:
        if alunos[i].nota > maiorNota:
            maiorNota = alunos[i].nota
            maiorNome = alunos[i].nome

print()
print('='*30)
print(f'    ALUNO COM A MAIOR NOTA')
print('='*30)
print(f'Nome: {maiorNome}')
print(f'Nota: {maiorNota}')