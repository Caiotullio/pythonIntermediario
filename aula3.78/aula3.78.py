'''
Combinations, permutations e product - Itertools
Combinação - Ordem não importa
Permutação - ordem importa
ambos não repetem valores unicos
Produtos - ordem importa e repete valores unicos
'''

from itertools import combinations, permutations, product

pessoas = ['Luiz', 'Andre', 'Eduardo', 'Leticia', 'Fabricio', 'Rose']

for grupo in product(pessoas, 2):
    print(grupo)