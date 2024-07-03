# Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

celsius = float(input('Digite a temperatura em Celsius: '))
fahrenheit = ((9*celsius)/5)+32
print('A temperatura de {}ºC corresponde a {}ºF'.format(celsius,fahrenheit))