Algoritmo "semnome"
// Disciplina   : Algoritmos
// Professor    : Regiane Kawasaki
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Carolina de Lima Alves
// Data atual  : 16/05/2023
Var
// Seção de Declarações das variáveis
   vet1: vetor[1..20] de real
   vet2: vetor[1..20] de real
   x, y: inteiro

Inicio
// Seção de Comandos, procedimento, funções, operadores, etc...
   para x de 1 ate 20 faca
        escreva("Insira o", x, "º valor: ")
        leia(vet1[x])
   fimpara

   escreva("VETOR ORIGINAL : [")
   para x de 1 ate 20 faca
        escreva(vet1[x], ", ")
   fimpara
   escreva("]")
   
   y <- 20
   x <- 1
   enquanto y >= 1 faca
            enquanto x <= 20 faca
                    vet2[y] <- vet1[x]
                    y <- y - 1
                    x <- x + 1
            fimenquanto
   fimenquanto

   escreval()
   escreva("VETOR INVERTIDO: [")
   para y de 1 ate 20 faca
        escreva(vet2[y], ", ")
   fimpara
   escreva("]")
Fimalgoritmo
