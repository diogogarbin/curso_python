#!/usr/bin/python3
#ola = '''

#Sejam Bem Vindos

 #'''
#print(ola)

#nome = input ('Digite seu nome: ')# A função imput pausa o script e esper interação do usuário

#print(nome.lower()) #lower() deixa tudo em minúsculo tittle() deixa em formato de títuli e upper() tudo minúsculi

#Exercício Atribuir dois número em variáveis diferentes, e imprimir a soma dos dois

#num1 = 1
#num2 = 2
#soma = nm_1 + nm_2

#print(soma)

#________________________________________________________________________________________
#Comando Type mostra o tipo do arquivo
# O input pega números como se fossem string então precisa converter

#print("o primeiro numero: {} o segundo numero: {}".format(num1, num2)) printar variável no meio da frase

#Exercício Leia o nome do aluno, 2 notas e calcule a média

falta = int(input("Digite o numero de faltas"))
nome = input('Digite o nome do aluno: ')
nt1 = int(input("digite a primeira nota: "))
nt2 = int(input("digite a segunda nota: "))

md = nt1 + nt2 / 2
if md >= 7 and falta <= 4:
        print("Aprovado")
else:
        print("reprovado")
#print ('A Média do {} é: {}'.format(nome.lower(), md) )
 
#[] -> lista ou array, para adicionar usa-se o metodo .append 

#{} -> Dicionário 
# EX
# cadastr0 = {"nome":"daniel", "idade":24}
# para acessar -> cadastro ['nome']
#.strip -> retira espaço caso o usuário digite