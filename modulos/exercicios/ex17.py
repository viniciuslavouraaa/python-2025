'''
Faça um programa que leia o comprimento do cateto oposto
e do cateto adjacente de um triângulo retângulo, calcule e
mostre o comprimento da hipotenusa.
'''
import math
catetoA = float(input("Valor do cateto oposto:"))
catetoB = float(input("Valor do cateto adjacente:"))

hipotenusa = math.hypot(catetoA, catetoB)
#hipotenusa = math.sqrt((catetoA ** 2) + (catetoB ** 2))

print(f"O comprimento da hipotenusa é de {hipotenusa:.2f}")
