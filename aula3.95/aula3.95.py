import cnpj

cnpj1 = '04.252.011/0001-10'

if cnpj.valida(cnpj1):
    print(f'{cnpj1} é validado')
else:
    print(f'{cnpj1} é invalidado')