//Questão 1 - Peça um número e valide se este número é divisível por 5.
programa {
  funcao inicio() {
    inteiro num, resto, int
    escreva("Digite um número \n")
    leia(num)
    
    resto = num % 5
    se(resto == 0)
        escreva(num," é divisível por 5")
    senao 
        escreva(num," não é divisível por 5")
  }
}
