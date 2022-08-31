"""Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
Para homens: (72.7*h) - 58
Para mulheres: (62.1*h) - 44.7
"""

print("olá \n")
h = float(input("por favor digite sua altura em metros \n"))
piHomem = (72.7*h)-58
piMulher = ((62.1*h) - 44.7)

print("Seu peso ideal é \n Homem:", piHomem ,  "Kg\n Mulher: ", piMulher, "Kg")
