"""Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
o produto do dobro do primeiro com metade do segundo .
a soma do triplo do primeiro com o terceiro.
o terceiro elevado ao cubo."""

print("olá \n")
n1 = int(input("Entre com o primeiro numero inteiro"))
n2 = int(input("Entre com o primeiro segundo inteiro"))
n3 = float(input("Entre com o numero real"))

a = (2*n1) * (n2/2)
b = (3*n1) + n3
c = n3**3

print ("o produto do dobro do primeiro com metade do segundo é " , a )
print("a soma do triplo do primeiro com o terceiro é " , b)
print("o terceiro elevado ao cubo é " , c)
