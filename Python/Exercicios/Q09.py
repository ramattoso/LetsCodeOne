'''
Crie (manualmente ou sorteando os números) uma lista de 10 números e imprima:
1. uma lista com os 4 primeiros números;
2. uma lista com os 5 últimos números;
3. uma lista contendo apenas os elementos das posições pares;
4. uma lista contendo apenas os elementos das posições ímpares;
5. a lista inversa da lista sorteada (isto é, uma lista que começa com o último elemento da
lista sorteada e termina com o primeiro);
6. uma lista inversa dos 5 primeiros números;
7. uma lista inversa dos 5 últimos números.
'''


import random
import numpy as np
random.seed(0)

lista=[]
for i in range(0,10):
    lista.append(np.random.randint(1,100))

lista_quatro_primeiros = lista[0:4]
lista_cinco_ultimos = lista[5:10]
lista_pares = lista[0:10:2]
lista_impares = lista[1:10:2]
lista_inversa = lista[::-1]
lista_cinco_primeiros_inversa = lista[-6:-11:-1]
lista_cinco_ultimos_inversa = lista[-1:-6:-1]
print("A lista com os quatro primeiros números é: ", lista_quatro_primeiros)
print("A lista com os cinco últimos números é: ", lista_cinco_ultimos)
print("A lista com os números das posições pares é: ", lista_pares)
print("A lista com os números das posições ímpares é: ", lista_impares)
print("A lista inversa é: ", lista_inversa)
print("A lista inversa dos cinco primeiros números é: ", lista_cinco_primeiros_inversa)
print("A lista inversa dos cinco últimos números é: ", lista_cinco_ultimos_inversa)
print(lista)