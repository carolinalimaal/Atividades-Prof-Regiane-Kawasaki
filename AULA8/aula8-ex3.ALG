Algoritmo "semnome"
// Disciplina   : Algoritmos
// Professor    : Regiane Kawasaki
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Carolina de Lima Alves
// Data atual  : 16/05/2023
Var
// Seção de Declarações das variáveis 
   vet : vetor[1..10] de inteiro
   x, a: inteiro
   

Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 
   para x de 1 ate 10 faca
        escreva("Digite um valor: ")
        leia(a)
        se (a mod 2) = 0 entao
           vet[x] <- a
        fimse
   fimpara
Fimalgoritmo