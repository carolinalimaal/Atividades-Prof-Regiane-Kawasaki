Algoritmo "semnome"
// Disciplina   : Algoritmos
// Professor    : Regiane Kawasaki
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Carolina de Lima Alves
// Data atual  : 16/05/2023
Var
// Seção de Declarações das variáveis
   vet1: vetor[1..10] de real
   vet2: vetor[1..10] de real
   vet3: vetor[1..10] de real
   x: inteiro
Inicio
// Seção de Comandos, procedimento, funções, operadores, etc...
   para x de 1 ate 10 faca
        escreva("VETOR 1 - Insira o ", x, "º valor: ")
        leia(vet1[x])
   fimpara
   
   limpatela
   
   para x de 1 ate 10 faca
        escreva("VETOR 2 - Insira o ", x, "º valor: ")
        leia(vet2[x])
   fimpara
   escreva("A soma do VETOR 1 + VETOR 2 é: [")
   para x de 1 ate 10 faca
        vet3[x] <- vet1[x] + vet2[x]
        escreva(vet3[x], ", " )
   fimpara
   escreva("]")
Fimalgoritmo
