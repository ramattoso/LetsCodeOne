## Estruturas condicionais 

'''
    Saber se é maior ou menor de idade
'''
idade = 10

if idade >=18:
    print('Você é maior de idade. \n')
else:
    print('Você é menor de idade. \n')


'''
    Aprovado ou reprovado
'''
media=float(input('Informe a sua média: \n'))
presenca = int(input('Dê a porcentagem de presença: \n'))

if media >=7.0 and presenca >=70:
    print('Você foi aprovado')
elif media >=5.0:
    print('Você foi para prova final')
else:
    print('Você está reprovado')