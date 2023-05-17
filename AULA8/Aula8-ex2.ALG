Algoritmo "semnome"
// Disciplina   : Algoritmos
// Professor    : Regiane Kawasaki
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Carolina de Lima Alves
// Data atual  : 16/05/2023
Var
// Seção de Declarações das variáveis
   vet: vetor[1..50] de real
   num, x: inteiro

Inicio
// Seção de Comandos, procedimento, funções, operadores, etc...
   vet[1] <- 1

   num <- 1
   para x de 2 ate 50 faca
        vet[x] <- num/(2*x)
   fimpara
Fimalgoritmo