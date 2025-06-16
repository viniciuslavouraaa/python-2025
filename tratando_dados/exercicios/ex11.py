''' 
Faça um programa que leia a largura e a altura de uma 
parede em metros, calcule a sua área e a quantidade de
tinta necessária para pinta-la, sabendo que cada litro
de tinta, pinta uma área de 2m².
''' 
larg = float(input('Largura da parede:'))
alt = float(input('Altura da parede:'))
area = larg*alt
litros = area/2

print(f'Sua parede tem a dimensão de {larg}x{alt} e sua área é de {area}m².\nSerá necessário {litros}l para pintar essa parede')