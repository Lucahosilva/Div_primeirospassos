#Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.
a =int(input("insira o primeiro numero "))
b = int(input("insira o segundo numero"))

for n in range (a+1, b) :
    print (n)