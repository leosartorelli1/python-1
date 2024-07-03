# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input('Digite o  seu salário atual: '))
salarioAtt = salario + (salario * 0.15)
print('O seu salário passará de R${:.2f} para R${:.2f} com 15% de aumento'.format(salario, salarioAtt))