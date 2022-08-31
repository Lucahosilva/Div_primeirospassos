"""Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total."""

print("Olá")
m2 = float(input("qual a area em m²?"))
l = m2/3
lata_GDE = 18
qtde_lata = l/lata_GDE
preco = qtde_lata * 80

print("São necessarias " , qtde_lata , " latas \n custará R$" , preco )
