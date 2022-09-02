#Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

print("="*200)

genero = (str(input("Gentileza informar o genero, abreviado (M/F): ")))

if genero == "M" :
    print("\nM - Masculino\n")
elif genero == "F" :
    print("\nF - Feminino\n")
else : 
    print("\nGenero invalido\n")