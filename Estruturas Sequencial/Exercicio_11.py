"""
Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
a = o produto do dobro do primeiro com metade do segundo .
b = a soma do triplo do primeiro com o terceiro.
c = o terceiro elevado ao cubo.

"""

a = int(input('Digite um numero inteiro: '))
b = int(input('Digite outro numero inteiro: '))
c = float(input('Digite um numero real: '))

resposta_a = (a*2) * (b/2)
resposta_b = (a*3) + c
resposta_c = c ** 3

print('A =', resposta_a)
print('B =', resposta_b)
print('C =', resposta_c)


