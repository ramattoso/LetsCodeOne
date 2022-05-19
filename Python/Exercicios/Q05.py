'''
Vamos fazer um programa para verificar quem é o assassino de um crime. Para descobrir o
assassino, a polícia faz um pequeno questionário com 5 perguntas onde a resposta só pode ser
sim ou não:
1. Mora perto da vítima?
2. Já trabalhou com a vítima?
3. Telefonou para a vítima?
4. Esteve no local do crime?
5. Devia para a vítima?
Cada resposta sim dá um ponto para o suspeito. A polícia considera que os suspeitos com 5
pontos são os assassinos, com 4 a 3 pontos são cúmplices e 2 pontos são apenas suspeitos,
necessitando de outras investigações. Valores abaixo de 2 são liberados.
No seu programa, você deve fazer essas perguntas e, de acordo com as respostas do usuário,
você vai informar como a polícia o considera.

'''

print('Será que você é o assassino?')
print('Rubens foi assassinado ontem, responda com sim ou não as perguntas e saiba como a polícia o considera')

pontuacao = 0
pergunta_1 = str(input('1. Mora perto da vítima?'))
if pergunta_1 == 'sim' or pergunta_1 == 'Sim':
    pontuacao = pontuacao + 1
pergunta_2 = str(input('2. Já trabalhou com a vítima?'))
if pergunta_2 == 'sim' or pergunta_1 == 'Sim':
    pontuacao = pontuacao + 1
pergunta_3 = str(input('3. Telefonou para a vítima recemente?'))
if pergunta_3 == 'sim' or pergunta_1 == 'Sim':
    pontuacao = pontuacao + 1
pergunta_4 = str(input('4. Esteve na casa de Rubens?'))
if pergunta_4 == 'sim' or pergunta_1 == 'Sim':
    pontuacao = pontuacao + 1
pergunta_5 = str(input('5. Devia dinheiro para a vítima?'))
if pergunta_5 == 'sim' or pergunta_1 == 'Sim':
    pontuacao = pontuacao + 1

if pontuacao == 5:
    print("Você é o assassino!!!")
elif pontuacao <5 and pontuacao >=3:
    print("Você é cúmplice!!!")
elif pontuacao == 2:
    print("Você é suspeito.")
else:
    print("Você está liberado!")