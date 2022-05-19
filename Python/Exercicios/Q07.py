'''
Faça um programa que leia as coordenadas de 2 (dois) pontos em um plano cartesiano 2D: a
coordenada x do primeiro ponto (x_1), a coordenada y do primeiro ponto (y_1), a coordenada x do
segundo ponto (x_2) e a coordenada y do segundo ponto (y_2). Em seguida, calcule a distância
euclidiana entre os pontos, utilizando a equação abaixo:
'''

from cmath import sqrt


x_1 = float(input('Digite a primeira abscissa: '))
y_1 = float(input('Digite a primeira ordenada: '))
x_2 = float(input('Digite a segunda abscissa: '))
y_2 = float(input('Digite a segunda ordenada: '))

d = (sqrt((x_1-x_2)**2+(y_1-y_2)**2))

print('A distância entre os pontos é ',d)