Algoritmo "Exerc�cio 1 Aula 11"
// Disciplina   : Algoritmos
// Professor    : Regiane Kawasaki
// Descri��o   : Exerc�cio 1 - Aula 11
// Autor(a)    : Carolina de Lima Alves
// Data atual  : 15/06/2023

tipo aluno = registro
                 nome: caracter
                 n1, n2, n3, media: real
        fimregistro
Var
// Se��o de Declara��es das vari�veis 
   aluno: vetor[1..4] de aluno
   x: inteiro

Inicio
// Se��o de Comandos, procedimento, fun��es, operadores, etc... 
   para x de 1 ate 4 faca
        escreval("Aluno ", x)
        escreva("Nome: ")
        leia(aluno[x].nome)
        escreva("Nota 1: ")
        leia(aluno[x].n1)
        escreva("Nota 2: ")
        leia(aluno[x].n2)
        escreva("Nota 3: ")
        leia(aluno[x].n3)
        aluno[x].media <- (aluno[x].n1 + aluno[x].n2 + aluno[x].n3)/3
        escreval("M�dia: ", aluno[x].media)
        escreval()
   fimpara

Fimalgoritmo