#Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
#Caso o número já exista lá dentro, ele não será adicionado.
#No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

lista_numeros = []

while True:
    print('-'*20)
    numero = input('|Informe um numero: ') 
    print('-'*20)
    if numero.isnumeric():
        int(numero)
        if numero in lista_numeros:
            print('Este valor ja existe na lista!')
            escolha = input('deseja continuar informando numeros? S/N:')
            if escolha in 'Nn':
                break
        else:
            lista_numeros.append(numero)
            print('Valor adicionado')
            escolha = input('deseja continuar informando numeros? S/N:')
            if escolha in 'Nn':
                break
    else:
        print('Por favor informe um número!')
    
lista_numeros.sort()
print('-'*20)
print(f'A lista em ordem crescente é: {lista_numeros}')