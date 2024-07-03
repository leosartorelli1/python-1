# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preco = float(input('Digite o valor do produto: '))
desconto = preco - (preco * 0.05)
print('O produto que custava R${:.2f} com 5% de desconto custará R${:.2f}'.format(preco, desconto))