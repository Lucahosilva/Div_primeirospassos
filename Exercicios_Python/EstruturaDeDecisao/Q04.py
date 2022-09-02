#Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

print("="*200)

letra = str(input("Digite uma letra por gentileza: "))
if letra == 'a' or 'e' or 'i' or "o" or "u" :
    print("\n A letra digitada é uma vogal\n")
else: 
    print(("\n A letra digitada é uma consoante\n"))