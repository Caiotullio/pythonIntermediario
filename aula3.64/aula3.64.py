# add (adiciona), update(atualiza), clear, discard
# union | (une)
# intersection & (todos os elementos presentes)
# difference - (elementos apenas no set da esquerda)
# symmetric_difference ^ (Elementos que estão nos dois sets, mas não em ambos)
'''
s1 = set()
s1.add('python')
s1.update('python')
print(s1)
'''
s1 = {1, 2, 3, 4, 5}
s2 = {1, 2, 3, 4, 5, 6}
s3 = s1 | s2
s4 = s1 - s2
s6 = s1 & s2
s5 = s1 ^ s2
print(s3)
print(s4)
print(s5)
print(s6)