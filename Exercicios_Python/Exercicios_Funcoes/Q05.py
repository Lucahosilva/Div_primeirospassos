#Faça um programa com uma função chamada somaImposto. 
# A função possui dois parâmetros formais: taxaImposto,
#  que é a quantia de imposto sobre vendas expressa em porcentagem 
# e custo, que é o custo de um item antes do imposto. 
# A função “altera” o valor de custo para incluir o imposto sobre vendas.

taxaImposto = float(input(" insira a aliquota  em  % "))
custo = float(input("insira o custo "))

def somaImposto(taxaImposto , custo):

    custo = custo *(taxaImposto/100) + custo

    print(f"o valor final será {custo}")
somaImposto(taxaImposto , custo)



