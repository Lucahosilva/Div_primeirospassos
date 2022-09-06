#Altere o programa anterior para mostrar no final a soma dos números.
a =int(input("insira o primeiro numero "))
b = int(input("insira o segundo numero"))
lista=list(range (a+1,b))

for n in range (a+1, b) :
    print (n)

print(sum(lista))