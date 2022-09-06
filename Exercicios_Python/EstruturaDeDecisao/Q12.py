#Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
#Desconto do IR:
#Salário Bruto até 900 (inclusive) - isento
#Salário Bruto até 1500 (inclusive) - desconto de 5%
#Salário Bruto até 2500 (inclusive) - desconto de 10%

print("=" * 200)
valorHora= float(input("Insira o valor da hora: "))
horas = float(input("horas trabalhadas no mês :"))
salario = valorHora * horas

sind = 0.03 * salario 
fgts = 0.11 * salario
inss = 0.1 * salario 

if salario <=900 :
    ir = 0
elif salario <=1500 :
    ir = salario * 0.05
elif salario <=2500 :
    ir = salario * 0.1
else : ir = salario * 0.2

print("=" * 100)
print("Salario bruto: (", valorHora ,"*" , horas , ")    : " , salario )
print("(-)IR   : " , ir)
print(f'''(-) INSS : {inss}
(-) sindicato  : {sind}

salario liqudo  {salario - ir - inss - sind}

''')




