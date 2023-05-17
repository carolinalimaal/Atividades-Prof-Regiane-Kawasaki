Algoritmo "semnome"
// Disciplina   : Algoritmos
// Professor    : Regiane Kawasaki
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Carolina de Lima Alves
// Data atual  : 16/05/2023
Var
// Seção de Declarações das variáveis
   vet: vetor[1..20] de inteiro
   p, p1, menor: inteiro

Inicio
// Seção de Comandos, procedimento, funções, operadores, etc...
   para p de 1 ate 20 faca
        escreva("Digite um valor: ")
        leia(vet[p])
        se p = 1 entao
           menor <- vet[p]
        senao
             se vet[p] < menor entao
                menor <- vet[p]
                p1<- p
             fimse
        fimse
   fimpara
   escreva("O menor elemento é ", menor, " que está na posição ", p1)
Fimalgoritmo
