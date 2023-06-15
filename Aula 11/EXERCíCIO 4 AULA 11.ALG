Algoritmo "Exercício 4 Aula 11"
// Disciplina   : Algoritmos
// Professor    : Regiane Kawasaki
// Descrição   : Exercício 4 - Aula 11
// Autor(a)    : Carolina de Lima Alves
// Data atual  : 15/06/2023

tipo contracheque = registro
                 nome, func: caracter
                 sal, novosal: real
        fimregistro
Var
// Seção de Declarações das variáveis 
funcionario: vetor[1..3] de contracheque
x: inteiro

Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 
   para x de 1 ate 3 faca
        escreval("CADASTRO FUNCIONÁRIO ", x)
        escreva("Nome: ")
        leia(funcionario[x].nome)
        escreva("Função: ")
        leia(funcionario[x].func)
        escreva("Salário: R$")
        leia(funcionario[x].sal)
        funcionario[x].novosal <- funcionario[x].sal * 1.3
        escreval()
   fimpara
   limpatela
   
        escreval("CONTRACHEQUE")
   para x de 1 ate 3 faca
        escreval("FUNCIONÁRIO ", x)
        escreval("Nome: ", funcionario[x].nome)
        escreval("Função: ", funcionario[x].func)
        escreval("Salário: R$", funcionario[x].sal)
        escreval("Salário com aumento: ", funcionario[x].novosal)
        escreval()
   fimpara
Fimalgoritmo