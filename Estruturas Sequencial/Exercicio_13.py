"""
Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
Para homens: (72.7*h) - 58
Para mulheres: (62.1*h) - 44.7
"""
h = float(input('Digite a altura:'))
peso_para_homens = (72.7*h) - 58
peso_para_mulheres = (62.1*h) - 44.7
print('O peso ideal para homens é:', peso_para_homens, 'kg')
print('O peso ideal para mulheres é:', peso_para_mulheres, 'kg')