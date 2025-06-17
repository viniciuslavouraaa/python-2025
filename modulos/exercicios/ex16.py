'''
Crie um programa que leia um número Real qualquer
pelo teclado e mostre na tela sua porção inteira
'''
import math

num = float(input("Digite um número:"))
numInt = math.trunc(num)
print(f"O número {num} tem a parte inteira {numInt}")