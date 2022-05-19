'''
Faça um programa que peça 2 números inteiros e um número real, calcule e mostre:
a) o produto entre o dobro do primeiro e a metade do segundo.
b) a soma entre o triplo do primeiro e o terceiro.
c) o terceiro elevado ao cubo.
'''

num_int_1 = int(input('Digite um número inteiro: ')) 
num_int_2 = int(input('Digite outro número inteiro: ')) 
num_float_1 = float(input('Digite um número real: ')) 

letra_a = 2*num_int_1*num_int_2
letra_b = 3*num_int_1+num_float_1
letra_c = num_float_1**3

print("a) o produto entre o dobro do primeiro e a metade do segundo é ", letra_a)
print("b) a soma entre o triplo do primeiro e o terceiro", letra_b)
print("c) o terceiro elevado ao cubo ", letra_c)