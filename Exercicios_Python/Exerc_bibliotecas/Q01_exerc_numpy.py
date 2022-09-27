'''Numpy
 1. Utilizando a biblioteca numpy siga as instruções abaixo:
    1. Crie um array 6x6 preenchido com zero
    2. Preencha o centro desse array com um array 4x4 preenchido com uns
    3. Preencha o centro desse array com um array 2x2 preenchido com dois
    4. Gere um segundo array 6x6 com números inteiros aleatórios entre 0 e 2.
    5. Subtraia o primeiro array pelo segundo'''

import numpy as np
a = np.zeros([6,6])
a[1:5,1:5,] = 1
a[2:4 , 2:4] =2

b =np.random.randint(low= 0 , high= 3 , size= [6 ,6])

print(f'''
primeiro array 
{a}

segundo array
{b}

a-b =
''')
print(a-b)
