#!/usr/bin/python3

def soma(x, y):
    return x + y

print(soma('daniel' , 'prata'))

#__________________________________________________________

def boas_vindas(nome):

    return 'Seja bem vindo {}'.format(nome.title())

print(boas_vindas('daniel'))

#_________________________________________________________

def ler_arquivo(nome):
    with open(nome, 'r') as arquivo:
        conteudo = arquivo.read()
    return conteudo

print(ler_arquivo('frutas.txt'))

#___________________________________________________

def troca(nome)
    nome = nome.replace('a' , '@')
    return 'Seja bem vindo {}'.format(nome.title())
    print(troca(nomes))