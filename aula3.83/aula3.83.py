try:
    print(a)
except NameError as erro:
    print('Erro no desenvolvedor, falar com ele')
except (Indexerror, KeyError) as erro:
    print('Erro de indice ou chave')
except Exception as erro:
    print('Ocorreu um erro inesperado')

#Else:print('Seu codigo foi executado com sucesso')

finally:
    print('Finalmente')
