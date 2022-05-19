'''
Faça uma função que recebe uma lista de números e retorna a soma dos elementos dessa lista.
'''

def somando(lista):
    soma = 0.0
    for item in lista:
        soma = soma + int(item)
            
    return soma

lista = [];
inserir = str(input('Deseja inserir elemento na lista? (S/N) \n'))
while inserir != 'N':
    lista.append(float(input('Digite o número: ')))
    inserir = str(input('Deseja inserir elemento na lista? (S/N) \n'))

print('Sua lista é ', lista)
print(somando(lista))