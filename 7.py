#Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
#A) Quantas pessoas foram cadastradas.
#B) Uma listagem com as pessoas mais pesadas.
#C) Uma listagem com as pessoas mais leves.

dados = []
pessoas = []
peso = []
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    pessoas.append(dados[:])
    peso.append(dados[1])
    dados.clear()
    resp = str(input('Deseja continuar? [S/N] '))
    if resp in 'Nn':
        break
print(f'Você cadastrou {len(pessoas)} pessoas')
print(f'O maior peso foi de {max(peso):.2f}Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == max(peso):
        print(f'{p[0]} ', end='')
print(f'\nO menor peso foi de {min(peso):.2f}Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == min(peso):
        print(f'{p[0]} ', end='')