# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

medida = float(input('Digite uma distancia em metros: '))
cm = medida * 100
mm = medida * 1000
print('A distancia de {} em metros corresponde a {:.0f} em centimetros e {:.0f} em milimetros'.format(medida, cm, mm))
