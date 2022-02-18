'''
import vendas.calc_preco

preco = 49.90
preco_com_aumento = vendas.calc_preco.aumento(valor=preco, porcentagem=15)
print(preco_com_aumento)
'''
'''
from vendas import calc_preco

preco = 49.90
preco_com_aumento = calc_preco.aumento(valor=preco, porcentagem=15)
print(preco_com_aumento)
'''
from vendas.calc_preco import aumento, reducao
from vendas.formata import preco as preco2 # preco2 esta apelidando preco para nao sobreescrever a variavel preco =49.90

preco = 49.90
preco_com_aumento = aumento(valor=preco, porcentagem=15, formata=True)
print(preco_com_aumento)

preco_com_reducao = reducao(valor=preco, porcentagem=15, formata=True)
print(preco_com_reducao)
