#Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
#Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

expressao = input('Informe uma expressão entre parenteses: ')
contador = []
for caractere in expressao:
    if caractere == '(':
        contador.append('(')
    elif caractere == ')':
        if len(contador) > 0:
            contador.pop()
        else:
            contador.append(')')
            break
if len(contador) > 0:
    print('Sua expressão está errada')
else:
    print('Sua expressão está certa')

