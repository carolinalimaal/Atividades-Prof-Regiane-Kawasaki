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
   soma: real

Inicio
// Seção de Comandos, procedimento, funções, operadores, etc...
   num <- 1
   soma <- 1
   para x de 1 ate 50 faca
        vet[x] <- num/(2*x)
        soma <- soma + vet[x]
   fimpara
   escreva("A soma de 1+1/2+1/4+1/6+...+1/100 é igual a: ", soma)
Fimalgoritmo
