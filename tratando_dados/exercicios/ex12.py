'''
Faça um algoritmo que leia o preço de um produto e mostre
seu novo preço com 5% de desconto
'''
v_prod = float(input('Qual o valor do produto: R$ '))
desc = v_prod*(5/100)
novo_valor = v_prod - desc

print(f'O valor original do produto era de R${v_prod}, ganhando R${desc:.2f} de desconto')
print(f'O valor final ficou R${novo_valor:.2f}')