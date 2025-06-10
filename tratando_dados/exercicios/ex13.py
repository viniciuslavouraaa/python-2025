'''
Faça um algoritmo que leia o salário de um funcionário e mostre 
seu novo salário, com 15% de aumento.
'''
salario = float(input('Digite seu salário:'))
v_aumento = salario*(15/100)
novo_salario = salario+v_aumento

print(f'Seu salário atual é de R${salario}, com um aumento de 15%,')
print(f'seu salário teve um aumento de R${v_aumento}, e seu novo salário é de R${novo_salario}')