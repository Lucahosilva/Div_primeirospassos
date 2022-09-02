#Faça um Programa que leia três números e mostre o maior deles.

n1 = float(input("insira o primeiro numero: "))
n2 = float(input("insira o segundo numero: "))
n3 = float(input("insira o terceiro numero: "))

maior = n1

if n2 > maior :
    maior = n2
if n3 > maior :
    maior = n3

print(maior , "é o maior número")
