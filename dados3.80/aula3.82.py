from dados import produtos,pessoas, lista
from functools import reduce

'''
acumula = 0
for item in lista:
    acumula += item
print(acumula)
'''

soma_lista = reduce(lambda ac, i: i + ac, lista, 0) # ac=acumuladores; 0=pra comecar do zero
soma_preços = reduce(lambda ac, p: p['preço'] + ac, produtos, 0) # ac=acumuladores; 0=pra comecar do zero
soma_idade = reduce(lambda ac, p: p['idade'] + ac, pessoas, 0) # ac=acumuladores; 0=pra comecar do zero
