'''
Faça um programa que leia um ângulo qualquer e mostre
na tela o valor do seno, cosseno e tângente desse ângulo
'''
import math

angl = float(input("Digite um ângulo qualquer:"))
# Tem que passar pra radiano, se não não funciona
seno = math.sin(math.radians(angl))
cos = math.cos(math.radians(angl))
tan = math.tan(math.radians(angl))

print(f"O ângulo {angl}, possuí os valores de:\nSeno: {seno:.2f}\nCosseno: {cos:.2f}\nTângente:{tan:.2f}")