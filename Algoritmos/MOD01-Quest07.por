//Quest�o 7 - De uma lista de dez n�meros inteiros desordenados, encontre e mostre o maior e o menor.programa 
programa{
  funcao inicio() {
    
    real num[] = {2,34,65,78,91,23,45,76,10,0}, maior, menor
    maior = num[0]
    menor = num[0]

    para(inteiro k=1; k<10; k++)
    {
        se(maior >=num[k])
            maior = maior
        se(maior < num[k])
            maior = num[k]
        se(menor <=num[k])
            menor = menor
        se(menor > num[k])
            menor = num[k]
    }
    escreva("O maior n�mero da lista � ",maior," e o menor n�mero da lista � ", menor)
}
}
