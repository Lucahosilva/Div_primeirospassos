#Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.

n1 = -1 # direcionar o usuario direto pra dentro do while

while n1<0 or n1 >10 :
    n1 = int(input("numero: "))
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


        