'''
Crie um programa que leia quanto dinheiro uma pessoa tem
na carteira e mostre quantos Dólares ela pode comprar
'''
v_real = float(input('Valor em Real:'))
dolar = 5.58
v_dolar = v_real/dolar

print(f'Com R${v_real} reais, você pode comprar ${v_dolar:.2F} dolares.')