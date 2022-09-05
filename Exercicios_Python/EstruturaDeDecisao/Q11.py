"""As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
salários até R$ 280,00 (incluindo) : aumento de 20%
salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
o salário antes do reajuste;
o percentual de aumento aplicado;
o valor do aumento;
o novo salário, após o aumento."""

print("=" * 200)

salario = float(input("insira o salario do colaborador: "))

if salario <= 280 : 
    novosalario = salario * 1.2
    percentual = 20
elif salario >280 and salario <=700 :
    novosalario = salario * 1.15
    percentual = 15
elif salario >700 and salario<=1500:
    novosalario = salario *1.1
    percentual = 10
elif  salario >1500:
    novosalario = salario *1.05 
    percentual = 5
print( "o salario era: " , salario)
print( "o percentual de reajuste foi: " , percentual,"%")
print(" o valor do aumento é: " , novosalario-salario)
print("o nome salario é: ", novosalario)