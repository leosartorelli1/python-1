# Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
computador = randint(0,5) # sorteia um numero
print('-=-' * 20)
print('Vou pensar em um número de 1 a 5. Tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que número em pensei?')) # Jogador tenta adivinhar
print('PROCESSANDO...')
if jogador == computador:
    print('PARABÉNS! Você me venceu')
else:
    print('GANHEI! Eu pensei no numero {} e não no número {}'.format(computador, jogador))