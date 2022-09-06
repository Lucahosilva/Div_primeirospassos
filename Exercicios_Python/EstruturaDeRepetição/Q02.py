"""Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações."""

usuario = ""
senha = ""

while usuario == senha  :
    usuario = input("Crie seu usuario :")
    senha = input("crie sua senha: ")
    print("Entradas iguais não permitidas, tente novamente")

print("Cadastro criado")
