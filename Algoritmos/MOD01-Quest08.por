//Questão 8 - Ordene uma lista de 10 palavras recebidas pela pessoa, as palavras serão digitadas uma por vez.
programa{
  funcao inicio() {
    
    cadeia listaDePalavras[10], listaOrdenada[10], aux
    inteiro pos
    
    escreva("\n Digite uma palavra \n")
        leia(listaDePalavras[0])
    listaOrdenada[0] = listaDePalavras[0]
    para(inteiro i = 1; i < 10; i++){
        escreva("\n Digite uma palavra \n")
        leia(listaDePalavras[i])
        pos = i/2
        se(listaDePalavras[i]<listaOrdenada[pos])

        senao
            se(listaDePalavras[i] < listaOrdenada[pos+1])
            senao
                se(listaDePalavras[i] < listaOrdenada[pos+2])

    }
}

listaDePalavras = {hoje, bola, amora, azul, corrida, marrom}
listaOrdenada = {amora, azul, corrida, hoje}