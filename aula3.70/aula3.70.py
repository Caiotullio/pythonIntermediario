lista = [0,1,2,3,4,5]

print(hasattr(lista,'__iter__')) # a lista é interavel
print(hasattr(lista,'__next__')) # a lista não é interador

lista = iter(lista)
print(hasattr(lista,'__next__')) # a lista agora é um interador

lista2 = [x for x in range(1000)]
print(type(lista2))
lista2 = (x for x in range(1000)) # geradores são entre ()
print(type(lista2))
