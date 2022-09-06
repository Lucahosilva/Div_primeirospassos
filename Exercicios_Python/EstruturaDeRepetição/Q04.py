"""Supondo que a população de um país A seja da ordem de 80.000 habitantes com uma taxa anual de crescimento de 3% e que a população de B seja 200.000 habitantes com uma taxa de crescimento de 1.5%.
 Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento."""

a = 80.000
b = 200.000

txa = 0.03
txb = 0.015

anos = 0

while b>=a :
    a = a*txa +a
    b = b*txb +b
    anos +=1

print(f'''levará {anos} anos para o pais A se igualar ou passar o pais B''')
