#Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. O usuário deve informar de qual numero ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:
'''Tabuada de 5:
5 X 1 = 5
5 X 2 = 10
...
5 X 10 = 50'''


n1 = -1 # direcionar o usuario direto pra dentro do while

while n1<0 or n1 >10 :
    n1 = int(input("Digite um numero inteiro: "))
    if n1 <0 or n1 >10:
        print('numero invalido, digite algo entre 0 e 10')
    else :
        valido = n1
        print("numero Validado\n")
        print(f'''
        =======================
          Tabuada do {valido}
        =======================
        ''')

        fator = 0
        while fator <11 :
         print(f'''{valido} X {fator} = {valido*fator}''')
         fator = fator +1
        print( "Fim!")