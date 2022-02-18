# Tuplas não sao editaveis
# t1 = () ja é uma tupla
'''
t1 = (1, 2, 3, 'a', 5)
for v in t1:
print(t1)
'''

t1 = (1, 2, 3, 4, 5)
t1 = list(t1)
t1[1] = 300
t1 = tuple(t1)
n1, n2, *_, n_ultimo = t1

print(n_ultimo)

