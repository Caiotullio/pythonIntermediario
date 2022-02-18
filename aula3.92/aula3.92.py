#Mutavel : Listas, dicionarios
#Imutavel: Tuplas, strings, numeros, true, False, None ...

def lista_de_clientes(clientes_iteravel, lista=[]): # o uso do [] resulta no acumulo de listas por isso no print(clientes2) aparece clientes1
    lista.extend(clientes_iteravel)
    return lista

lista_clientes_1 = ['Fabricio']
clientes1 = lista_de_clientes(['Joao', 'Maria', 'Eduardo', lista_clientes_1])
clientes2 = lista_de_clientes(['Marcos', 'jonas', 'Zico'])
clientes3 = lista_de_clientes(['Jose'])

print(clientes1)
print(clientes2)

'''
def lista_de_clientes(clientes_iteravel, lista=None):
    if lista is None:
        lista = []
    lista.extend(clientes_iteravel)
    return lista

lista_clientes_1 = ['Fabricio']
clientes1 = lista_de_clientes(['Joao', 'Maria', 'Eduardo'])
clientes2 = lista_de_clientes(['Marcos', 'jonas', 'Zico'])
clientes3 = lista_de_clientes(['Jose'])

print(clientes1)
print(clientes2)


'''
