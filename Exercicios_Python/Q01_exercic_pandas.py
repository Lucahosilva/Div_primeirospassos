
'''Crie um data frame pandas com 1000 amostras em cada uma das seguintes colunas:
   1. Idade: números inteiros aleatórios entre 0 e 100 (inclusos).
   2. Nota: Números decimais entre 0 e 1000.
   3. Sexo: Valores aleatórios de M ou F
   4. Estado: Valores aleatórios entre os estados do Brasil.'''



from random import randint , random
import pandas as pd
import numpy as np

idade = np.random.randint(low = 0 , high = 101 , size = 1000)
idades = pd.Series(idade , name = 'idades')

nota = (np.random. random(size = 1000 ))
notas = pd.Series(nota , name = "notas")*1000

sexo =["M" , "F"]
genero = np.random.choice(sexo , 1000)

estado = ['AC','AL','AP','AM','BA','CE','ES','GO','MA','MT','MS','MG','PA','PB','PR','PE','PI','RJ','RN','RS','RO','RR','SC','SP','SE','TO','DF']
estados = np.random.choice(estado, 1000)


df = pd.DataFrame({"idade" : idades , 'nota': notas , "sexo" : genero, 'estado' : estados})

print  (df)

df.to_csv("enem.csv" , index= False)