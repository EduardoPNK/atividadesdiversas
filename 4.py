#Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
#A) Quantos números foram digitados.
#B) A lista de valores, ordenada de forma decrescente.
#C) Se o valor 5 foi digitado e está ou não na lista.

lista_numeros = []

while True:
    numero = int(input('Informe um número: '))
    lista_numeros.append(numero)
    decisao = input('Deseja continuar informando(S/N): ')
    if decisao in 'Nn':
        break
print('-'*30)    
print('A quantidade de numeros digitados foi: {}'.format(len(lista_numeros)))
print('Os valores ordenados em ordem decrescente são: {}'.format(sorted(lista_numeros, reverse=True)))
if 5 in lista_numeros:
    print('O valor 5 está na lista')
    print('A quantidade de vezes que ele aparece é {}'.format(lista_numeros.count(5)))   
else:
    print('O valor 5 não está na lista')
        
