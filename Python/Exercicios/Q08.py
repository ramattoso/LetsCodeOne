'''
Calcule a soma de mil termos dos inversos dos fatoriais: 1/(1!) + 1/(2!) + 1/(3!) + 1/(4!) + ...
Dica: Use três variáveis:
● um contador;
● uma variável para soma;
● e uma variável para os termos.
'''
# Com recursividade, cabe comentar que fatorial recursivo dá ruim
def fatorial(num):
    if num > 1:
        return num*fatorial(num-1)
    else:
        return 1


'''soma = 0
for i in range(1,50):
    resultado = fatorial(i)

    soma = soma + 1/resultado
print(soma)'''

### Com while
soma = 0
j = 1
N = 4
resultado = 1
for i in range(1,N):
    while j <= i:
        resultado = resultado*j
        j = j+1
    print(resultado)
    soma = soma + 1/resultado
print(soma)