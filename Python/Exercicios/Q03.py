'''
Crie uma função que recebe o valor do raio de um círculo como parâmetro e retorna o valor da
área desse círculo. Lembrando que a área de círculo é dada pela equação: A = ℼ r^2.
'''
import math

pi = math.pi
raio = float(input('Digite o raio: '))

area = pi*raio**2
print('A área é:', area)