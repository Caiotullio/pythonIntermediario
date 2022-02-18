# ao executar esse codigo criaremos o arquivo abc.txt

file = open('abc.txt', 'w+') # ler e escrever # testar usar a+ para somar ao arquivos anteriores # w+ deleta o arquivo anteiror e assume um novo
file.write('Linha 1\n')
file.write('Linha 2\n')
file.write('Linha 3\n')

file.seek(0, 0)  # chama o curso para o inicio do arquivo
print('Lendo linhas: ')
print(file.read())
print('#########################')

file.seek(0, 0)
print(file.readline(), end='') # a função do end ai é para não pular linha
print(file.readline(), end='')
print(file.readline(), end='')
print('#########################')

file.seek(0, 0)
for linha in file:
    print(linha, end='')

file.close()

'''
import os                # para deletar arquivo
os.remove('abc.txt')
'''