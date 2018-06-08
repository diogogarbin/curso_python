#!/usr/bin/python3

#letras = ['a', 'b', 'c', ['d', 'e']]

#print(letras[3][1]) # o índice 3 é a segunda lista e o 1 é a letra 'e' dentro da segunda lista

#print(letras[-1]) # -1 printa o ultimo campo -2 o pneultimo e assim por diante

#letras2 = letras[:] # para copiar uma lista preciso do [:] para especificar que é uma cópia e se quero so parte da lista coloco o indice ex: [1:3] no último sempre colocco um indice a mais do que eu quero

#numeros = list(range(100)) # Crio uma lista de números de 1-100

#numeros1 = list(range(50, 100, 5)) # Crio uma lista de 50-100 passo 5 em 5

#for x in numeros1:
 #   print(x) # vai printar todos os valores da minha lista

#Exercício para mostras os números paras de 0-10
#exercicio = list(range(10)) 
#for x in exercicio:
 #   if x % 2 == 0:
 #       print(x)

#Mesmo exercício de maneira interativa, com o usuário digitando o range para identificação dos números pares
#qtd= int(input("digite um inteiro: "))

#for i in range(qtd):
 #   if i % 2 == 0:
  #      print(z)

pessoas = [
    {'nome': 'daniel', 'idade': 24},
    {'nome': 'rafael', 'idade': 6},
    {'nome': 'renata', 'idade': 23},
    {'nome': 'yasmin', 'idade': 4},
]

#print (pessoas[2])

#for i in pessoas
 #   print(i)

for x in pessoas:
    nome = x['nome']
    idade = x['idade']

    print("O (a) {} tem {} anos".format(nome.title(), idade))