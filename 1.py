#Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
#No final, mostre qual foi o maior e o menor valor digitado
#e as suas respectivas posições na lista.

num = []

for count in range(0, 5):
    lista = int(input('Informe um número: '))
    num.append(lista)


maior = max(num)
menor = min(num)
maior_index = num.index(maior)
menor_index = num.index(menor)

print('O maior número da lista é {} na posição {}, E o menor número da lista é {} na posição {}.'.format(maior, maior_index, menor, menor_index))