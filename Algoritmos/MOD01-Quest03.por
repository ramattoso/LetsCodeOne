// Questão 3. Coloque, num algoritmo, um processo de chamada em sala de aula.
programa {
  funcao inicio() {
    
    cadeia nomes[] = {"Arthur Aguiar","Eslovênia","Fernando","Laura Moura","Marisa Souza"}
    inteiro cont = 0
    cadeia chamada[5], aux[]

    enquanto(cont < 5){
        escreva(nomes[cont], "\n")
        leia(aux)

        chamada[cont] = nomes[cont] +" "+ aux
        cont = cont+1
    }
    para(inteiro k =0; k<5; k++){
        escreva(chamada[k])
        escreva("\n")
    }
}
