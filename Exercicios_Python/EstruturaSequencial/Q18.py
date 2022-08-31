#Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

print("olá")
t = float(input("qual o tamanho do arquivo em MB? "))
v = float(input("qual a velocidade da internet em Mbps? "))
temp = t/(v/8)
print("o tempo estimado de Download é de " , temp, " segundo(s)")
