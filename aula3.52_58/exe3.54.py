'''
def saudacao(s, nome):
    print(f'{s} {nome}')
saudacao('Ola','Joao')
'''
'''
def funcao(n1, n2, n3):
     print ( n1 + n2 + n3)
funcao(1, 2, 3)
funcao(1, 1, 1)
funcao(1, 1, 3)
'''
'''
def numeros(n1, percentual):
    return n1 * (1 +(percentual /100))
aumento = numeros(100, 10)
print(aumento)
'''
def num(n):
    if n % 3 == 0 and n % 5 == 0:
        return 'FizzBuzz'
    elif n % 5 == 0:
        return 'Buzz'
    elif n % 3 == 0:
        return 'Fizz'
    else: n
print(num(3))



