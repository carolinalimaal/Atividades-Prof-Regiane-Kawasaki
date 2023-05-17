Algoritmo "semnome"
// Disciplina   : Algoritmos
// Professor    : Regiane Kawasaki
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Carolina de Lima Alves
// Data atual  : 16/05/2023
Var
// Seção de Declarações das variáveis
   vet: vetor[1..20] de real
   x, y: inteiro
   
Inicio
// Seção de Comandos, procedimento, funções, operadores, etc...
   para x de 1 ate 20 faca
        escreva("Insira o", x, "º valor: ")
        leia(vet[x])
   fimpara
   
   escreva("VETOR: [")
   para x de 1 ate 20 faca
        escreva(vet[x])
   fimpara
   escreva("]")
   
   para y de 20 ate 1 passo -1 faca
        para x de 1 ate 20 faca
             vet[y] <- vet[x]
        fimpara
   fimpara
Fimalgoritmo
