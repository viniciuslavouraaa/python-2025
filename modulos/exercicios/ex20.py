'''
O mesmo professor do desafio anterior quer sortear a ordem
de apresentação de trabalhos dos alunos. Faça um programa que
leia o nome dos quatro alunos e mostre a ordem sorteda
'''
import random

alunos = []
while len(alunos) <= 3:
    alunos.append(input("Digite um nome:"))

random.shuffle(alunos)
print(f"A ordem de apresentação dos trabalhos será essa:")
for n in alunos:
    print(n) 