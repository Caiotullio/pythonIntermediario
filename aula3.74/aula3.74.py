'''
ZIP - Unindo iteraveis
Zip_longest - Itertools
'''

from itertools import zip_longest, count

indice = count()
cidades = ['São Paulo', 'Belo Horizonte', 'Salvador', 'Monte Belo']
estados = ['SP', 'MG', 'BA']

cidades_estados = zip(
    indice,
    estados,
    cidades,
)

for indice, estados, cidades in cidades_estados:
    print(indice, estados, cidades)

