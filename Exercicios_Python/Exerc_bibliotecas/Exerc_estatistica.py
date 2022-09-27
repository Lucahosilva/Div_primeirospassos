'''Dados Numéricos
A Moda
A Mediana
A média
Os Quartis
Os 10% maiores
Os 5 % Menores
O valor máximo
O valor mínimo

Dados de Texto
A frequência absoluta
A frequência relativa
A Moda
Qual o tipo de Moda?
O valor máximo (ordem alfabética)
O valor mínimo (ordem alfabética)'''


import pandas as pd
import numpy as np

df = pd.read_csv('Exercicio_estatistica - Sheet1.csv', decimal=",")


moda_idade = df["Idade"].mode()[0]
moda_filhos = df['Filhos'].mode()[0]
moda_estado = df["Estado"].mode()[0]
moda_altura = df['Altura'].mode()[0]
moda_formaçao = df["Formação"]. mode()[0]



mediana_altura = df["Altura"].median()

quartis = df.quantile([.25 , .5 , .75])

mediana = df[['Idade' , 'Filhos' , 'Altura']].median()
media = df[['Idade' , 'Filhos' , 'Altura']].mean()

dez_maiores_idade =df.nlargest(10 , "Idade")
dez_maiores_filhos =df.nlargest(10 , "Filhos")
dez_maiores_filhos =df.nlargest(10 , "Altura")

menor_valor = df.min()
maior_valor = df.max()

frequencia_abs_nome = df["Nome"].value_counts()

desvio_pd = df.std()

print(desvio_pd)


