""""Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
A mensagem "Reprovado", se a média for menor do que sete;
A mensagem "Aprovado com Distinção", se a média for igual a dez."""

print("=" * 100)
n1 = float(input("\nInsira a primeira nota: "))
n2 = float(input("Insira a segunda nota: "))
nf = (n1+n2)/2

print( "média final é de : " , nf , "\n")

if nf == 10 :
    print("Aprovado com Distinção\n")
elif nf >= 7 :
    print("Aprovado\n")
else :
    print("Reprovado\n")