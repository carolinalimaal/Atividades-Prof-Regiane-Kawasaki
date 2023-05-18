Algoritmo "semnome"
// Disciplina   : Algoritmos
// Professor    : Regiane Kawasaki
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Carolina de Lima Alves
// Data atual  : 16/05/2023
Var
// Seção de Declarações das variáveis
   vet : vetor[1..10] de inteiro
   x, a, maior, menor: inteiro
   soma: real

Inicio
// Seção de Comandos, procedimento, funções, operadores, etc...
   x <- 1
   enquanto x <> 11 faca
        escreva("Digite um valor: ")
        leia(a)
        se (a mod 2) = 0 entao
           se (1 < a) e (a <= 20) entao
              vet[x] <- a
              soma <- soma + vet[x]
              se x = 1 entao
                 maior <- vet[x]
                 menor <- vet[x]
              senao
                   se vet[x] > maior entao
                      maior <- vet[x]
                   fimse
                   se vet[x] < menor entao
                      menor <- vet[x]
                   fimse
              fimse
              x <- x + 1
           fimse
        fimse
   fimenquanto
   escreva("Todos os elementos do vetor são: ")
   para x de 1 ate 10 faca
        escreva(vet[x], ",")
   fimpara
   escreval()
   escreval("A média dos números digitados é: ", soma/10)
   escreval("O maior valor foi ", maior, " e o menor foi ", menor)
Fimalgoritmo
