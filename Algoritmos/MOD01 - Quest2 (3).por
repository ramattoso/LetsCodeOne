// Questão 5 - De uma lista de dez números desordenados, encontre e mostre o maior.
programa {
  funcao inicio() {
    
    cadeia lista, 
    caracter resp
    inteiro tamanho
    tamanho = 0

    resp = 's'
    enquanto(resp !='n'){
        escreva("Entre com um item da lista \n")
        leia(lista)
        escreva("Adicionar itens na lista, s ou n?\n")
        leia(resp)
        tamanho = tamanho + 1
    }
    escreva("O tamanho da lista é ", tamanho)
}
