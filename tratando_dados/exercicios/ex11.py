''' 
Faça um programa que leia a largura e a altura de uma 
parede em metros, calcule a sua área e a quantidade de
tinta necessária para pinta-la, sabendo que cada litro
de tinta, pinta uma área de 2m².
''' 
larg = int(input('Qual a largura da parede em mestros:'))
alt = int(input('Qual a altura da parede em mestros:'))
area = alt*larg
litros = area/2

print(f'Com uma parede com área de {area} metros, será necessário {litros} litros\n para pintar essa parede')