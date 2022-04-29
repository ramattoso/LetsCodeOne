// Questão 4 - Calcule a idade de uma pessoa de acordo com a data de nascimento dela. Você deve solicitar dia, mês e ano.
programa {
  funcao inicio() {
    inteiro idade, dia, mes, ano, diah, mesh, anoh
    escreva("Digite o ano de seu nascimento \n")
    leia(ano)
    escreva("\n Digite o mês de seu nascimento \n ")
    leia(mes)
    escreva("\n Digite o dia de seu nascimento \n ")
    leia(dia)
    escreva("Digite o ano atual \n")
    leia(anoh)
    escreva("\n Digite o mês atual \n ")
    leia(mesh)
    escreva("\n Digite o dia atual \n ")
    leia(diah)
    
    se(mesh>=mes e diah>=dia)
        idade = anoh-ano;
    se(mesh>=mes e diah<dia)
        idade = anoh-ano-1;
    se(mesh<mes)
        idade = anoh-ano-1

    escreva("Sua idade é ", idade, " anos.")
  }
}
