'''
Um professor quer sortear um dos seus quatro alunos para
apagar o quadro. Faça um programa que ajude ele, lendo o
nome deles e escrevendo o nome escolhido
'''
import random

alunos = []
while len(alunos) <= 3:
    aluno = input("Digite um nome:")
    alunos.append(aluno)
    
alunoSort = random.choice(alunos)

print(f"O aluno escolhido para apagar a lousa foi {alunoSort}")