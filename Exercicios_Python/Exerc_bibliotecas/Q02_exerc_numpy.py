'''2. Crie um array de duas dimensões, no formato 9x9, com números de 0 a 80 ordenados de modo crescente e selecione:
  1. Os números ímpares
  2. Os números pares
  3. Os múltiplos de sete
  4. Os múltiplos de 10
  5. Os números 32,33,42,43'''

import numpy as np

a = np.arange(81)
a = a.reshape([9,9])
#print(a)

impar = a[a%2== 1]
par = a[a%2 == 0]

multi7 = a[a%7 == 0]
multi10 = a[a%10 == 0]

b = a[[3 , 3 , 4 , 4] , [5 , 6 , 6 , 7]]

print (multi7)