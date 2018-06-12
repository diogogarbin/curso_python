#!/usr/bin/python3

def boas_vindas():
    while True:
        nome = input('Digite um nome: ')
        if nome.lower() == 'sair':
            return 'saindo do loop'
        print('Seja bem vindo {}'.format(nome.title()))

print(boas_vindas)