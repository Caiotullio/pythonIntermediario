'''
count - itertools
'''
from itertools import count

#contador = count(start=10, step=5)

contador = count(start=5, step=0.1)

for valor in contador:
    print(round(valor, 2)) #arredondar com o round

    if valor => 10:
        break