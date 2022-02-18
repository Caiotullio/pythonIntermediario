#listas, tuplas e strings - sequencias - iteravel
nome = 'Luiz Otavio'
iterador = iter(nome)
gerador = (letra for letra in nome)

print(next(gerador))
print(next(gerador))
print(next(gerador))
print(next(gerador))

print('Olha o FOR')

for letra in gerador:
    print(letra)

print('Olha o outro FOR')

for letra in gerador:
    print(letra)

print(next(gerador))