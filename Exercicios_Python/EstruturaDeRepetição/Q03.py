#WorkInProgress

"""Faça um programa que leia e valide as seguintes informações:
Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd';"""

nome = input("Digite o nome : ")
while len(nome) <= 3 :
    print("Nome menor que 3 caracteres, digite outro: ")
    nome = input("Digite o nome : ")

idade = int(input("Digite a idade "))

while idade <=0 or idade >=150 :
    print("idade invalida, digite outra por favor: ")
    idade = int(input("Digite a idade "))

salario = float(input("Digite o salario: "))    
while salario <= 0 :
    print("salario invalido")
    salario = float(input("Digite o salario: "))  

sexo = input("Sexo: ")
while not (sexo == "M" or sexo == "F") :
    print("Sexo invalido, por favor digite M ou F ")
    sexo = input("Sexo: ")

estadoCivil = input( "estado civil: ")
while  not estadoCivil in ('s', 'c', 'v', 'd') :
    print("estado civil não aceito , por favor digite 's', 'c', 'v', 'd' : ")
    estadoCivil = input( "estado civil: ")

print(f'''
    =========
    dados aceitos 

    Nome: {nome};
    Idade: {idade};
    Salário: {salario};
    Sexo: {sexo};
    Estado Civil: {estadoCivil}    
    
    ''')
