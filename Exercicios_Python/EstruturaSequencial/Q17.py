"""Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros;
misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias."""

import math

print("Olá")
m2 = float(input("qual a area em m²? "))
cobertura = m2/6
preco_lata = 80
preco_galao = 25
vLata = 18
vGalao = 3.6

soLata = math.ceil(cobertura / vLata)
soGalao = math.ceil(cobertura / vGalao)

psoLata = soLata * preco_lata
psoGalao = soGalao * preco_galao

mLata = (cobertura*1.1)//vLata
mGalao = math.ceil(((cobertura*1.1)//vLata)%vGalao)
mpreco = (mLata * preco_lata) + (mGalao * preco_galao)

print("se comprar apenas latas \nnumero de latas:" , soLata ,  "custando R$ ", psoLata,)
print("se comprar apenas galões \nnumero de Galões:" , soGalao ,  "custando R$ ", psoGalao,)
print("misturando será necessario " , mLata , "latas" , mGalao, "Galões, custando no total R$" , mpreco)
