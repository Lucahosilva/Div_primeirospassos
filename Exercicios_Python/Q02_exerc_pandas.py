'''2. Utilizando pandas, realize as seguintes alterações no dataset:
   1. Transforme 20% das notas em valores nulos(None), simulando alunos que não compareceram à prova.
   2. Preencha as notas nulas com valor 0, simulando uma atribuição automática do sistema.
     `df = df.fillna(0)`
   3. Remova alunos com idades inferiores a 18 e superiores a 80, simulando uma filtragem automática do sistema para alunos com idades incosistentes.
   4. Crie um novo campo de aprovado para os alunos restantes que obtiveram nota igual ou superior a 600, com o valor 'Aprovado'. Simulando uma correção automática.
   5. Preencha o resto do campo de aprovado com 'Reprovado' para os demais alunos (preenchimento de nulo).
   `df = df[coluna].fillna('Reprovado')`
   6. Mostre a quantidade de alunos aprovados e reprovados.'''

import pandas as pd

df = pd.read_csv("./enem.csv")
ausente = df['nota'].sample(frac = 0.8) 
df['nota'] = ausente
df = df.fillna(0)

idade_min= df['idade']<18 
idade_max = df['idade']>80

filtro_idade = ~ (idade_max | idade_max)

#print(df["idade"].loc[filtro_idade])

df["situação"] = None
print(df)








