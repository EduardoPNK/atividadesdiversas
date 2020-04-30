#Crie um programa que vai ler vários números e colocar em uma lista.
#Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente.
#Ao final, mostre o conteúdo das três listas geradas.

lista_principal = []
lista_impar= []
lista_par = []

while True:
    numero = input('Informe um valor númerico: ')
    if numero.isnumeric():
        int(numero)
        lista_principal.append(numero)
        escolha = input('Deseja continuar informando números?(S/N): ')
        if escolha in ('Nn'):
            break
    else:
        print('Por favor informe um número inteiro')
        
for i in lista_principal:
    if int(i) % 2 == 0:
        lista_par.append(i)
    else:
        lista_impar.append(i)
print(f'Lista principal: {lista_principal}')
print(f'Lista de números impares: {lista_impar}')
print(f'Lista de números pares: {lista_par}')