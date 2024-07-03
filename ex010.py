# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

real = float(input("Digite quantos reais você possui: "))
dolar = real / 5.61
print('com {:.2f} reais podem ser comprados {:.2f} doláres'. format(real, dolar))