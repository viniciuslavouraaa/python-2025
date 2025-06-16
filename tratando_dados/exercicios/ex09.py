'''
Faça um programa que leia um número inteiro qualquer
e mostre na tela sua tabuada 
'''
num = int(input('Digite um número:'))
n_tabu = [1, 2, 3, 4, 5, 6, 7 ,8 ,9, 10]

for n in n_tabu:
    res = num*n
    print(f'{num} x {n:2} = {res}')