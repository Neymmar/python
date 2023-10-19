from pythonExercicios.ex115.lib.interface import *
from pythonExercicios.ex115.lib.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'
if not arquivoExiste(arq):
    criarArquivo(arq)
while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoas', 'Sair do Sistema'])
    if resposta == 1:
        lerArquivo(arq) # Opção de listar o conteúdo de um arquivo.
    elif resposta == 2:
        cabecalho('NOVO CADASTRO') # Opção de cadastrar uma nova pessoa.
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabecalho('Saindo do Sistema...Até logo!') # Opção de cadastrar uma nova pessoa.
        break
    else:
        print('ERRO! Digite uma opção válida!') # Digite uma opção errado no menu.
    sleep(2)
