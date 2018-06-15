#!/usr/bin/python3

linguage=(input(str('Digite uqual a melhor linguagem de programação: ')))
if linguage == 'python':
    print("Acertou miseravi")
elif linguage == 'bash':
    print('pode ser')
else:
    print('errrrouuuu')

######################################################################################

nm=(float(input("Insira um número: ")))
nm1=(float(input("Insira outro número: ")))

result = nm + nm1
print(result)

######################################################################################

soma = 0
for x in range(4):
    nota = float(input('Digite a nota {}: '.format(x+1)))
    soma += nota
print("A média é igual há {:.2f}".format(soma/4))