//Quest�o 1 - Pe�a um n�mero e valide se este n�mero � divis�vel por 5.
programa {
  funcao inicio() {
    inteiro num, resto, int
    escreva("Digite um n�mero \n")
    leia(num)
    
    resto = num % 5
    se(resto == 0)
        escreva(num," � divis�vel por 5")
    senao 
        escreva(num," n�o � divis�vel por 5")
  }
}
