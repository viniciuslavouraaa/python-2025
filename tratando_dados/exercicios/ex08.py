''' 
Escreva um programa que leia um valor em metros e exiba
convertido em centimetros e mílimetros
'''
metros = int(input('Digite um valor em metros:'))
cm = metros*100
mm = metros*1000

print(f'{metros} metros, são {cm} centímetros e {mm} milímetros')