#Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação.

z = -1 # inicia o while
a =z
b=z

while  a == b == z :

    a = int(input("digite o tamanho da primeira população"))
    b = int(input("digite o tamanho da segunda população"))

    txa = float(input("digite a taxa de crescimento da primeira população"))
    txb = float(input("digite a taxa de crescimento da segunda população"))

    anos =1

while b>a :
    a = a*txa
    b = b*txb
    anos +=1

print(f'''
==============================================================
levará {anos} anos para o pais A se igualar ou passar o pais B
==============================================================
''')