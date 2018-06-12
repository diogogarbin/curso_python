#!/usr/bin/python3
# adicionar em um determinado indice lista.insert(indice , oque inserir)

# a- Criar uma lista de pessoas e exibir uma mensagem de boas vindas para cada uma 
# b- Alterar um usuário desta lista e exibir a mensagem
# c- Adicionar novas pessoas na lista com os metodos append e insert
# d- Reduzir o tamanho da lista com metodo pop ate zerar

lista = [ "Diogo", "João", "Pedro" ]
for x in lista:
    if x == 'João':
        x = x.replace(x , "Vitor")
    print("Seja Bem vindo {}".format(x))

novo = (input("Digite o nome: "))
lista.append(novo)
print(lista)

novo = (input("Digite outro nome: "))
lista.insert(4, novo)

print(lista)

while len(lista) > 0:
    print(lista)
    lista.pop()
print(lista)
