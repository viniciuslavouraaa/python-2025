'''
Escreva um programa que pergunte a quantidade de Km 
percorridos por um carro alugado e a quantidade de dias 
pelos quais ele foi alugado. Calcule o preço a pagar, sabendo
que o carro custa R$60 por dia e R$0,15 por km rodadp
'''
dias =int(input("Dias que o carro ficou alugado:"))
km = float(input("Quantos Kilometros percorridos:"))

v_pagar = (dias * 60) + (km * 0.15) 
print(f"O total a pagar é de R${v_pagar:.2F}")