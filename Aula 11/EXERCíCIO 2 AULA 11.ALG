Algoritmo "Exerc�cio 2 Aula 11"
// Disciplina   : Algoritmos
// Professor    : Regiane Kawasaki
// Descri��o   : Exerc�cio 2 - Aula 11
// Autor(a)    : Carolina de Lima Alves
// Data atual  : 15/06/2023
tipo RegAluno = registro
              nome, curso, disciplina: caracter
              mat, n1, n2, media: real
fimregistro

Var
// Se��o de Declara��es das vari�veis 
aluno: vetor[1..10] de RegAluno
x: inteiro

Inicio
// Se��o de Comandos, procedimento, fun��es, operadores, etc... 
   para x de 1 ate 10 faca
        escreval("CADASTRO ALUNO ", x)
        escreva("Nome: ")
        leia(aluno[x].nome)
        escreva("Matr�cula: ")
        leia(aluno[x].mat)
        escreva("Curso: ")
        leia(aluno[x].curso)
        escreva("Disciplina: ")
        leia(aluno[x].disciplina)
        escreva("Nota 1: ")
        leia(aluno[x].n1)
        escreva("Nota 2: ")
        leia(aluno[x].n2)
        limpatela
   fimpara

   para x de 1 ate 10 faca
        aluno[x].media <- (aluno[x].n1 + aluno[x].n2)/2
        escreval("RESUMO ALUNO ", x)
        escreval("Nome: ", aluno[x].nome)
        escreval("Matr�cula: ", aluno[x].mat)
        escreval("Curso: ", aluno[x].curso)
        escreval("Disciplina: ", aluno[x].disciplina)
        escreval("M�dia: ", aluno[x].media)
        escreval()
   fimpara

Fimalgoritmo