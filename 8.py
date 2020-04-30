#Crie um programa onde o usuário possa digitar sete valores
#numéricos e cadastre-os em uma lista única que mantenha separados
#os valores pares e ímpares.
#No final, mostre os valores pares e ímpares em ordem crescente.

numeros = [[], []]

for count in range(0, 7):
    numero = int(input('Informe um número: '))
    if numero % 2 == 0:
        numeros[0].append(numero)
    else:
        numeros[1].append(numero)
numeros[0].sort()
numeros[1].sort()
print(f'Valores Pares e Impares em ordem crescente {numeros}')

        