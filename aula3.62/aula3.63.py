print("Explica ... ")

perguntas = {
    'Pergunta 1' : {
        'pergunta' : 'quanto é 2+2? ',
        'respostas': {'a' : '1', 'b' : '4', 'c' : '5'},
        'resposta_certa' : 'b',
    },
    'Pergunta 2' : {
        'pergunta' : 'quanto é 3*2? ',
        'respostas': {'a' : '4', 'b' : '10', 'c' : '6'},
        'resposta_certa' : 'c',
    },
}
resposta_certa = 0
for pk, pv in perguntas.items():
    print(f'{pk} : {pv["pergunta"]}')

    print('Respostas:')
    for rk , rv in pv['respostas'].items():
        print(f'[{rk}]:{rv}')

    resposta_usuario = input('Sua resposta: ')

    if resposta_usuario == pv['resposta_certa']:
            print('EHHHHH voce acertou!')
            resposta_certa += 1
    else:
            print('XIIII voce errou')

qtd_perguntas = len(perguntas)
porcentagem_acertos = resposta_certa / qtd_perguntas*100

print(f'Voce acertou {resposta_certa} respostas.')
print(f'Sua porcentagem de acertos foi de {porcentagem_acertos}%')
