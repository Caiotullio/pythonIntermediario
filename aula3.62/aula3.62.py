#d1 = {'chave1' : 'valor da chave'}
#d1['nova chave'] = 'Valor da nova chave'

#d1 = dict(chave1 ='Valor da chave' , chave2 = 'valor da outra chave')

'''
d1 = {
    'str' : 'valor',
    123 : 'outro valor',
    (1,2,3,4) : 'Tupla'
}

d1 = {}
if d1.get('str') is not None:
    print(d1.get('str'))
'''
'''
d1 = {
    'chave1' : 'valor',
    'chave2' : 'outro valor',
    'chave3' : 'Tupla'
}
del d1['chave1']

for k, v in d1.items():
    print(k, v)
'''
d1 = {
    'cliente1' : {
        'nome' : 'Luiz',
        'sobrenome' : 'Otavio',
    }
    'cliente2' : {
        'nome' : 'Maria',
        'sobrenome' : 'moreira',
    }

}

for cliente_k, cliente_v in clientes.items():
    print(f'Exibindo {cliente_k}')
    for dados k_valor, v_valor in clientes_v.items():
        print(f'\t{dados_k} = {dados_v}')