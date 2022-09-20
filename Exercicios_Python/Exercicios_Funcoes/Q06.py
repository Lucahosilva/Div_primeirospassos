# Faça um programa que converta da notação de 24 horas para a notação de 12 horas.
# Por exemplo, o programa deve converter 14:25 em 2:25 P.M. 
# A entrada é dada em dois inteiros. 
# Deve haver pelo menos duas funções: uma para fazer a conversão e uma para a saída. 
# Registre a informação A.M./P.M. como um valor ‘A’ para A.M. e ‘P’ para P.M. 
# Assim, a função para efetuar as conversões terá um parâmetro formal para registrar se é A.M. ou P.M. 
# Inclua um loop que permita que o usuário repita esse cálculo para novos valores de entrada todas as vezes que desejar.

print('''olá,
bem vindo ao conversor de horas
''')

tipo= int(input("\n Qual conversor deseja  0 - 24 p 12/ 1 - 12 p 24 "))

hour = int(input("insira as horas : "))
minute = int(input("insira os minutos: "))
h = str(input("Digite A para AM / e P para PM ")).upper

def paraAmpm():

    global hour
    global minute
    
    if hour<12 :
       print(f'''No formato 12h, a notação fica assim {hour}:{minute} A.M.''')
       pass
    else:
        hour = hour - 12
    print(f'''No formato 12h, a notação fica assim {hour}:{minute} P.M.''')
    

def deAMpm():

    global hour
    global minute
    global h

    if h == "A" :

       print(f'''No formato 24h, a notação fica assim {hour}:{minute}''')
    
    else:
        hour = hour + 12
        print(f'''No formato 24h, a notação fica assim {hour}:{minute}''')
    
if tipo == 0:
    paraAmpm()
elif tipo ==1 :
    deAMpm()
else:
    print("formato invalido")
    tipo= input("\n Qual conversor deseja  0 - 24 p 12/ 1 - 12 p 24 ")



