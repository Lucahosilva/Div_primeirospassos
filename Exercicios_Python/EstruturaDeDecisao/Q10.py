#Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.
print('=' * 100)

turno = (input("qual seu turno de estudo? (M-matutino ou V-Vespertino ou N- Noturno) "))
turno = turno.upper

if turno == "M" :
    print( "Bom dia!")
elif turno == "V" :
    print("boa tarde")
elif turno == "N" :
    print("boa noite")
else : 
    print("valor invalido")






