'''Faça um programa que use a função valorPagamento para determinar o valor a ser pago por uma prestação de uma conta. O programa deverá solicitar ao usuário o valor da prestação e o número de dias em atraso e passar estes valores para a função valorPagamento, que calculará o valor a ser pago e devolverá este valor ao programa que a chamou. O programa deverá então exibir o valor a ser pago na tela. Após a execução o programa deverá voltar a pedir outro valor de prestação e assim continuar até que seja informado um valor igual a zero para a prestação. Neste momento o programa deverá ser encerrado, exibindo o relatório do dia, que conterá a quantidade e o valor total de prestações pagas no dia. O cálculo do valor a ser pago é feito da seguinte forma. Para pagamentos sem atraso, cobrar o valor da prestação. Quando houver atraso, cobrar 3% de multa, mais 0,1% de juros por dia de atraso.'''

prestacao = ""
diasAtraso = ""
historico =[]

def valorPagamento():
    global prestacao

    while prestacao != 0:

        prestacao = float(input("Qual o valor da prestação: "))
        diasAtraso = int(input("quantos dias em atraso: "))


        if diasAtraso > 0:
            valor= (prestacao *1.03) + (prestacao*0.001*diasAtraso)
            historico.append(valor)
            print(f'''
            o Valor do pagamento é {valor}
            ''')
        else :
            valor = prestacao
            historico . append(valor)
            print(f'''
            o Valor do pagamento é {valor}''')


valorPagamento()

while 0 in historico:
    historico.remove(0)


#------ printando relatorio--------#
for i in range(len(historico)):
    print(f'''{i+1} {historico[i]}''')

print("o total é R$",sum(historico) ,"\n")

    

        