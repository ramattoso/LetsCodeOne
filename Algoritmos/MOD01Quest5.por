// Quest�o 5 - De uma lista de dez n�meros desordenados, encontre e mostre o maior.
programa {
  funcao inicio() {
    
    real num[10], maior
    
    para(inteiro k=0; k<10; k++)
    {
        escreva("\n Digite um n�mero \n")
        leia(num[k])
    }
    maior = num[0]
    para(inteiro k=1; k<10; k++)
    {
        se(maior >=num[k])
            maior = maior
        senao
            maior = num[k]
    }
    escreva(maior)
  }
}
