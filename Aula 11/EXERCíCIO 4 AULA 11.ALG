Algoritmo "Exerc�cio 4 Aula 11"
// Disciplina   : Algoritmos
// Professor    : Regiane Kawasaki
// Descri��o   : Exerc�cio 4 - Aula 11
// Autor(a)    : Carolina de Lima Alves
// Data atual  : 15/06/2023

tipo contracheque = registro
                 nome, func: caracter
                 sal, novosal: real
        fimregistro
Var
// Se��o de Declara��es das vari�veis 
funcionario: vetor[1..3] de contracheque
x: inteiro

Inicio
// Se��o de Comandos, procedimento, fun��es, operadores, etc... 
   para x de 1 ate 3 faca
        escreval("CADASTRO FUNCION�RIO ", x)
        escreva("Nome: ")
        leia(funcionario[x].nome)
        escreva("Fun��o: ")
        leia(funcionario[x].func)
        escreva("Sal�rio: R$")
        leia(funcionario[x].sal)
        funcionario[x].novosal <- funcionario[x].sal * 1.3
        escreval()
   fimpara
   limpatela
   
        escreval("CONTRACHEQUE")
   para x de 1 ate 3 faca
        escreval("FUNCION�RIO ", x)
        escreval("Nome: ", funcionario[x].nome)
        escreval("Fun��o: ", funcionario[x].func)
        escreval("Sal�rio: R$", funcionario[x].sal)
        escreval("Sal�rio com aumento: ", funcionario[x].novosal)
        escreval()
   fimpara
Fimalgoritmo