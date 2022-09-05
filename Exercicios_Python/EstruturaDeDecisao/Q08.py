#Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.

print('=' * 100)
p1 = float(input("Favor informar o preço do primeiro produto : "))
p2 = float(input("Favor informar o preço do segundo produto : "))
p3 = float(input("Favor informar o preço do terceiro produto : "))

menor = min(p1, p2, p3)

print(" o menor valor é " , menor)
