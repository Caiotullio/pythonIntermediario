lista = [
    ['P1', 13],
    ['P2', 6],
    ['P3', 7],
    ['P4', 50],
    ['P5', 8]
]
'''
def func(item):
    return item[1]
lista.sort(key=func, reverse=True)
print(lista)
'''
#lista.sort(key=lambda item: item[1]) o uso da função lambda substitui o codigo anterior
#print(sorted(lista, key=lambda i: i[1]))
