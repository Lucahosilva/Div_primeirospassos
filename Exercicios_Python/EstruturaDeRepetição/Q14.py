#Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares.

n01 = int(input("Digite o primeiro numero inteiro: "))
n02 = int(input("Digite o segundo numero inteiro: "))
n03 = int(input("Digite o terceiro numero inteiro: "))
n04 = int(input("Digite o quarto numero inteiro: "))
n05 = int(input("Digite o quinto numero inteiro: "))
n06 = int(input("Digite o sexto numero inteiro: "))
n07 = int(input("Digite o setimo numero inteiro: "))
n08 = int(input("Digite o oitavo numero inteiro: "))
n09 = int(input("Digite o nono numero inteiro: "))
n10 = int(input("Digite o decimo numero inteiro: "))

lista = [n01, n02 , n03 , n04 , n05 , n06 , n07 , n08 , n09 , n10]
par = 0
impar = 0

for i in lista :
    if i%2 == 0:
        par +=1
    else: impar+=1

print(f''' {par} numeros pares''')
print(f''' {impar} numeros impares''')
