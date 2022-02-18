from dados import produtos, pessoas, lista

# nova_lista = map(lambda x: x * 2, lista )
# nova_lista = [x * 2 for x in lista ]

def aumenta_preco(p):
    p['preço'] = round(p['preço'] * 1.05, 2)
    return p

novos_produtos = map(aumenta_preco, produtos)

for produtos in novos_produtos:
    print(produtos)

#precos = map(lambda p: p['preço'], produtos)

'''
def aumento_idade (p):
    p['nova_idade'] = round(p['idade'] * 1,2)
    return p
nomes = map(aumento_idade, pessoas)
for pessoa in nomes:
    print(pessoa)
     
'''