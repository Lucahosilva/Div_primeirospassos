"""3. Crie um array com três dimensões, onde a primeira dimensão são os dias da dia (seg a dom), a segunda dimensão são as semanas do mês (considere apenas 4 para todos os meses), e a terceira são os meses do calendario (Jan a dezembro).
  1. Marque os finais de dia com a letra W
  2. Marque o começo do mês com a letra S
  3. Marque o final do mês com a letra E
  4. Marque os demais dias com a letra D
  5. Marque os feriados nacionais com a letra F
    - 01/01 - calendario novo
    - 15/04 - Paixão de Cris
PS: o enunciado está com a dimensões invertidas. ;D"""


import numpy as np
import os

dias = np.arange(1,29 , dtype=object)
mes = dias.reshape([1 , 4 ,7])

calendario = np.repeat(mes, 12 , axis = 0)

calendario[: , : , [0 , -1]] = "w"
calendario[: , 0, 0] = "S"
calendario[: , -1, -1] = "E"
calendario [: , : , [-2 , -3, -4 ,-5 , -6 ] ] = "D"
calendario[[0,3] , [0,2] , [0,0]] = "F"


 

print( calendario)
#print( dias)
#print( mes)




