'''
Desenvolva um programa que leia as duas notas de um aluno,
calcule e mostre sua média. 
'''
nota1 = float(input('Digite sua primeira nota:'))
nota2 = float(input('Digite sua segunda nota:'))
nota3 = float(input('Digite sua terceira nota:'))
notas = [nota1, nota2, nota3]

print(f'Sua média final é {sum(notas)/len(notas):.2f}')
