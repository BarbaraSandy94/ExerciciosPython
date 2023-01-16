#Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
#C = 5 * ((F-32) / 9).

F = float(input('Digite a temperatura em graus Fahrenheit: '))
C = 5 * ((F-32) / 9)

print('a temperatura corresponde em graus Celsius:', C)