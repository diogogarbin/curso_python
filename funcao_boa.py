#!/usr/bin/python3

def alteracao(nome, origin, destino):
    with open(nome, 'r') as arquivo:
        conteudo = arquivo.readlines()
        novo_conteudo = []
        for x in conteudo:
            novo_conteudo.append(x.replace(origin, destino))
    return novo_conteudo

conteudo = alteracao('nomedoarquivoquequero', 'oquequerotrocar', 'peloqueseratrocado')
