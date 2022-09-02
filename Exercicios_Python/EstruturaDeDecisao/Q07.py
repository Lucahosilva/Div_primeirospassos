#Faça um Programa que leia três números e mostre o maior e o menor deles.

n1 = float(input("INSIRA O PRIMEIRO NUMERO: "))
n2 = float(input("INSIRA O SEGUNDO NUMERO: "))
n3 = float(input("INSIRA O TERCEIRO NUMERO: "))

maior  = n1
menor = n1

if n2 > maior :
    maior = n2
if n3 > maior :
    maior = n3

if n2 < menor :
    menor = n2
if n3 < menor :
    menor = n3

print ("O maior numero é: " , maior , "\n" "O menor número é: " , menor)