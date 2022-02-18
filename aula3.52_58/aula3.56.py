'''
def func(*args)
    print(args)
lista = [1, 2, 3, 4, 5]
n1, n2, *n = lista
print(n1, n2, n)
'''

'''
def func(*args):
    print(args)
    print(args[0])
    print(args[-1])
    print(len(args))

func(1,2,3,4,5)
'''
def func(*args, **kwargs):
    print(args)
    print(kwargs)
Lista = [1, 2, 3, 4, 5]
Lista2 = [10, 20 ,30, 40, 50]
func(*Lista, *Lista2, nome = 'Caio')