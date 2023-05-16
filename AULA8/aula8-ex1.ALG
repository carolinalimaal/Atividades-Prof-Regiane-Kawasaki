Algoritmo "semnome"
// Disciplina   : Algoritmos
// Professor    : Regiane Kawasaki
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Carolina de Lima Alves
// Data atual  : 16/05/2023
Var
   vetElem: vetor[1..5] de real
   x: inteiro
   soma: real

Inicio
      para x de 1 ate 5 faca:
           escreva("Digite o", x,"º valor: ")
           leia(vetElem[x])
           se (x % 2) <> 0 entao
              soma <- soma + vetElem[x]
           fimse
      fimpara
      escreva("A soma dos valores nas posições ímpares é", soma)
Fimalgoritmo